# 💚 AWS CUR (Cost and Usage Report)

## 💛 What is it?
The **CUR (Cost and Usage Report)** is AWS's **most ****detailed billing data**. It is the raw, line-item record of everything you spent, dumped as files into an **S3 bucket**.
Think of it as the **itemized receipt** for your whole AWS account. The Billing console shows you the total and a few charts. The CUR shows you every single line: this instance, this hour, this much money.
One row is one usage line item, often **one resource per hour**. A busy account produces millions of rows per month.
## 💛 Why do we need it?
The Billing dashboard and Cost Explorer are great for a quick look, but they round off and group things. They can't answer sharp questions like:
- "What did each team spend, broken down by our own tags?"
- "Which exact resource caused the data-transfer spike?"
- "What is our cost per customer / per environment / per Kubernetes namespace?"
The CUR has that level of detail because it is line-item level and includes your **cost-allocation tags** as columns. This is the raw material for almost all serious **FinOps** (cloud cost management) work on AWS.
### 🤍 Real-world use case
You tag every resource with `team` and `env`. With the CUR you can produce a monthly report of "cost per team per environment" that Cost Explorer alone cannot give you at that precision.
## 💛 How does it work?
You define a report once. AWS then writes the data to your S3 bucket on a schedule and keeps updating it through the month.
- **Delivery**: files land in S3 (CSV or Parquet), organized by month.
- **Freshness**: updated a few times a day, not real-time. Numbers keep changing until the month closes and finalizes.
- **Consumption**: because it is just files in S3
  - You can query it with **Athena(← Chartmetric does this)**
  - Load it into **QuickSight** or Redshift, or point BI tools at it.
### 🤍 Request Flow
```javascript
AWS Billing system
  |
  | writes line-item usage on a schedule (a few times/day)
  v
S3 bucket  (CUR files: CSV or Parquet, partitioned by month)
  |
  +--> Athena      (query with SQL)
  +--> QuickSight  (dashboards)
  +--> Redshift / BI tools
```
### 🤍 Example: create a CUR (CLI)
```bash
# Define a report delivered to S3, in Parquet, with per-resource detail,
# and pre-wired for Athena.
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
## 💛 Key columns to know
The CUR has hundreds of columns. The ones you actually use most:
- `line_item_product_code`: which service (EC2, S3, RDS, ...).
- `line_item_usage_type`: the specific usage (e.g. `BoxUsage:t3.medium`, data transfer).
- `line_item_unblended_cost`: what it actually cost. The usual starting point.
- `line_item_usage_start_date`: when the usage happened.
- `resource_tags_user_*`: your own cost-allocation tags, one column per activated tag key.
### 🤍 unblended vs blended vs amortized
- **unblended**: the real rate you were charged for that line. Default for "what did this cost."
- **blended**: an averaged rate across a consolidated-billing org. Mostly ignore unless finance asks.
- **amortized**: spreads upfront Reserved Instance / Savings Plan payments across the hours they cover. Use this to see the effective cost of commitments over time.
## 💛 Gotcha
- **Tags must be activated first.** A tag only becomes a `resource_tags_user_<key>` column after you activate it in Billing, and it is **not retroactive**. Turn on your cost-allocation tags early.
- **Not real-time and not final.** Mid-month numbers keep moving. Only the finalized report at month close is stable.
- **The files are HUGE.** Do not try to open them directly.
  - Always query through Athena/QuickSight, and filter by the month partition so you do not scan everything.
- **CUR 2.0 / Data Exports** is the newer version AWS steers you toward. It has a cleaner schema and is set up via the Data Exports console, but the idea (line-item files in S3, queried by Athena) is the same.
## 💛 References
- AWS Docs: What are Cost and Usage Reports: https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html
- AWS Docs: CUR data dictionary (columns): https://docs.aws.amazon.com/cur/latest/userguide/data-dictionary.html
- AWS Docs: Data Exports (CUR 2.0): https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html
