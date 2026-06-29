# 💚 OLTP and OLAP

## 💛 What are they?
Two different jobs a database can do:
- **OLTP** (Online Transaction Processing): the **day-to-day operations** database. Lots of small, fast reads and writes.
- **OLAP** (Online Analytical Processing): the **analytics** database. Big, heavy queries that scan tons of rows to answer business questions.
Quick mental model:
- OLTP runs the business. "Place this order. Update this balance."
- OLAP studies the business. "What were total sales by region last quarter?"
## 💛 Why do we need both?
Because the two workloads pull a database in opposite directions, and one engine can't be great at both.
- An app needs to insert one order in milliseconds, thousands of times a second. That is OLTP.
- An analyst needs to sum 500 million rows for a dashboard. If you run that on the app's database, you slow down or lock up the live app. That is why OLAP lives separately.
So companies usually keep an OLTP database for the app, then copy that data into an OLAP system for analytics.
### 🤍 Real-world examples
- **OLTP**: PostgreSQL, MySQL behind a web app. An e-commerce checkout writing an order.
- **OLAP**: Snowflake, BigQuery, Redshift, ClickHouse. A finance dashboard summing a year of revenue.
## 💛 How are they different under the hood?
The big technical split is **row storage vs column storage**.
- **OLTP = row-based.** All columns of one record are stored together. Grabbing or updating one full record (one order, one user) is fast.
- **OLAP = column-based.** Each column is stored together. Summing one column across millions of rows is fast, because you only read that column, not the whole table.
### 🤍 Row vs Column storage
```javascript
ROW store (OLTP)
  [id=1, name=Kim, price=100][id=2, name=Lee, price=200]...
  Great for: "give me the whole row where id = 2"

COLUMN store (OLAP)
  id:    [1, 2, 3, ...]
  name:  [Kim, Lee, ...]
  price: [100, 200, ...]
  Great for: "SUM(price) over all rows" (reads only the price column)
```
### 🤍 Side by side
## 💛 How they connect (the pipeline)
In practice OLTP feeds OLAP. You don't pick one, you use both.
### 🤍 Data Flow
```javascript
App
  |
  v
OLTP database (PostgreSQL)     <- live transactions
  |
  | ETL / ELT (Airflow, Fivetran, CDC)
  v
OLAP warehouse (Snowflake)     <- analytics, dashboards
  |
  v
BI tool (Looker, Tableau)
```
The ETL/ELT step is the bridge. It moves data out of the operational database so heavy analytics never touches the live app.
## 💛 Gotcha
- Don't run big analytics directly on your OLTP database. A full-table aggregate can lock rows or starve the app of resources. Move that data to an OLAP system first.
- OLAP data is usually **slightly stale**. It's loaded on a schedule (every few minutes or hours), so it is not real-time. That is fine for reporting, not fine for "show the user their current balance."
- Column stores are bad at single-row updates. That is why you don't use Snowflake as your app database.
## 💛 References
- Snowflake: OLAP vs OLTP: https://www.snowflake.com/guides/oltp-vs-olap/
- Google Cloud: OLAP vs OLTP: https://cloud.google.com/learn/what-is-olap
- PostgreSQL docs (a classic OLTP engine): https://www.postgresql.org/docs/
