# 💚 Athena and CUR (AWS Cost and Usage Report)

## 💛 What are they?
Two AWS pieces that team up to answer "where is my AWS money going?"
- **CUR (Cost and Usage Report)**: the **most detailed billing data** AWS produces.
  - One row per resource per hour (or per line item), dumped as files into an S3 bucket.
- **Athena**: a **serverless SQL engine** that queries files sitting in S3 directly.
  - No database to run, no servers to manage.
  - You point it at S3, write SQL, pay per query.
Put together: CUR drops giant billing files in S3, and Athena lets you run SQL over them to slice your costs.
## 💛 Why do we need them?
The AWS Billing console is fine for a quick glance, but it can't answer detailed questions like:
- "How much did this one team's EC2 instances cost last month, by tag?"
- "Which S3 buckets drove our data-transfer bill?"
- "What did we spend per Kubernetes namespace?"
The CUR has that detail (it is line-item level), but it is far too big to open in a spreadsheet. Millions of rows. Athena is how you actually query it without loading it into a real database.
This is the backbone of most **FinOps** (cloud cost) work on AWS.
### 🤍 Real-world use case
Finance asks "why did our bill jump 30% in March?" You run one Athena query against the CUR grouped by service and usage type, and you have the answer in seconds, with no infrastructure to set up.
## 💛 How does it work?
- `CUR` delivers files to S3 on a schedule.
- `Athena` reads those files in place using a table definition (the schema) stored in the **Glue Data Catalog**.
You never move the data into Athena. Athena just reads S3.
### 🤍 Request Flow
```javascript
AWS Billing
  |
  | writes CUR files (CSV / Parquet) on a schedule
  v
S3 bucket (your CUR data)
  |
  | table schema lives in Glue Data Catalog
  v
Athena (serverless SQL over S3)
  |
  v
You / BI tool (QuickSight, Grafana, dashboards)
```
Key idea: Athena is **query-on-read**. The data stays as files in S3. Athena scans them when you run a query, and you pay for the bytes scanned.
### 🤍 Example: set up CUR (CLI)
```bash
# Create a Cost and Usage Report delivered to an S3 bucket.
# Athena integration + Parquet keeps queries cheap and fast.
aws cur put-report-definition --report-definition '{
  "ReportName": "my-cur",
  "TimeUnit": "HOURLY",
  "Format": "Parquet",
  "Compression": "Parquet",
  "AdditionalSchemaElements": ["RESOURCES"],
  "S3Bucket": "my-cur-bucket",
  "S3Prefix": "cur/",
  "S3Region": "us-east-1",
  "AdditionalArtifacts": ["ATHENA"],
  "ReportVersioning": "OVERWRITE_REPORT"
}'
```
### 🤍 Example: query costs with Athena (SQL)
```sql
-- Total unblended cost by service for a given month
SELECT
  line_item_product_code        AS service,
  SUM(line_item_unblended_cost) AS cost
FROM my_cur_database.my_cur
WHERE year = '2026' AND month = '3'
GROUP BY line_item_product_code
ORDER BY cost DESC
LIMIT 20;
```
```sql
-- Cost split by your own cost-allocation tag (e.g. "team")
SELECT
  resource_tags_user_team       AS team,
  SUM(line_item_unblended_cost) AS cost
FROM my_cur_database.my_cur
WHERE year = '2026' AND month = '3'
GROUP BY resource_tags_user_team
ORDER BY cost DESC;
```
## 💛 Cost gotcha (Athena bills you too)
- Athena charges **per terabyte scanned**, not per query.
  - A `SELECT *` over a year of CUR can scan a lot and cost real money.
- Use **Parquet** (columnar) for the CUR, not CSV. Athena then reads only the columns you select, scanning far less.
- Always filter on the **partition columns** (`year`, `month`).
  - Without that, Athena scans every file in the bucket…
- Cost-allocation tags must be **activated** in the Billing console before they show up as `resource_tags_user_*` columns. Untagged resources show blank.
## 💛 Gotcha
- The CUR is **append/overwrite on a schedule** (a few times a day), so it is not real-time. Today's costs are still settling.
- `unblended` vs `blended` vs `amortized` cost are different columns and mean different things. For "what did this actually cost", `line_item_unblended_cost` is the usual starting point; use amortized when you want Reserved Instance / Savings Plan cost spread out.
- Newer accounts may use **Data Exports (CUR 2.0)** instead of the classic CUR, but the Athena-over-S3 pattern is the same.
## 💛 References
- AWS Docs: Cost and Usage Reports: https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html
- AWS Docs: Query CUR with Athena: https://docs.aws.amazon.com/cur/latest/userguide/cur-query-athena.html
- AWS Docs: Amazon Athena: https://docs.aws.amazon.com/athena/latest/ug/what-is.html
