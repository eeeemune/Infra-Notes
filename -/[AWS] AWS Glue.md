# 💚 AWS Glue

# 💚 AWS Glue
## 💛 What is it?
**AWS Glue** is a **serverless data integration service**.
It does two big jobs:
- **Catalog**: keeps track of what data you have and what shape it is (the schema of your files/tables).
  - This is the **Glue Data Catalog**.
- **ETL**: runs jobs that **E**xtract, **T**ransform, and **L**oad data from one place to another
  - for example, raw S3 files into clean Parquet, or S3 into Redshift.
Simple way to think about it: Glue is the **glue between your data sources**. It figures out the schema of your messy files, remembers it, and runs the pipelines that move and reshape the data. No servers to manage.
## 💛 Why do we need it?
Raw data is usually messy and scattered: CSVs in one S3 bucket, JSON logs in another, a database over here. Before you can query or analyze it, you need to know its structure and often clean it up.
Glue solves the annoying parts:
- **No schema by hand.** A **Crawler** scans your S3 files and figures out the columns and types automatically, then writes them into the Data Catalog.
- **One shared catalog.** Athena, Redshift Spectrum, and EMR all read the same Glue Data Catalog. Define a table once, query it from many tools.
- **No cluster to run.** Glue ETL jobs run on managed Spark. You do not provision or babysit servers.
### 🤍 Real-world use case
You dump raw JSON logs into S3 every day. A Glue Crawler discovers their schema and registers a table. A Glue job then converts them to partitioned Parquet (cheaper and faster to query). Athena queries the Parquet. All serverless.
## 💛 How does it work?
Three pieces do most of the work:
- **Crawler**: points at a data store (usually S3), infers schema, and creates/updates tables in the Data Catalog.
- **Data Catalog**: the metadata store. Databases and tables that describe where your data lives and its schema. It does NOT hold the data itself, just the description.
- **Job**: a script (PySpark or Python shell) that reads, transforms, and writes data. Triggered on a schedule, on demand, or by an event.
### 🤍 Request Flow
```javascript
Raw data in S3 (CSV / JSON / logs)
  |
  | Crawler scans + infers schema
  v
Glue Data Catalog  (databases + tables = metadata only)
  |
  | Glue ETL Job (managed Spark) reads via catalog,
  | transforms, writes back
  v
Clean data in S3 (partitioned Parquet)
  |
  v
Athena / Redshift Spectrum / EMR  (query using the same catalog)
```
Key idea: the **Catalog is metadata, not data**. The actual bytes stay in S3. The Catalog just tells query engines what is there and how to read it.
### 🤍 Example: run a crawler (CLI)
```bash
# Create a crawler that scans an S3 path and writes tables
# into the "logs_db" database in the Data Catalog.
aws glue create-crawler \
  --name my-logs-crawler \
  --role AWSGlueServiceRole-mycrawler \
  --database-name logs_db \
  --targets '{"S3Targets": [{"Path": "s3://my-bucket/raw-logs/"}]}'

# Kick it off. When it finishes, tables appear in logs_db.
aws glue start-crawler --name my-logs-crawler
```
### 🤍 Example: a Glue ETL job (PySpark)
```python
# Read a catalog table, convert to Parquet, write partitioned output.
import sys
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glue = GlueContext(SparkContext.getOrCreate())

# Read from the Data Catalog (schema comes from the crawler)
dyf = glue.create_dynamic_frame.from_catalog(
    database="logs_db",
    table_name="raw_logs",
)

# Write out as partitioned Parquet
glue.write_dynamic_frame.from_options(
    frame=dyf,
    connection_type="s3",
    connection_options={"path": "s3://my-bucket/clean-logs/", "partitionKeys": ["dt"]},
    format="parquet",
)
```
## 💛 Gotcha
- **Catalog vs data.** Deleting a table in the Catalog does not delete the S3 files, and deleting S3 files does not update the Catalog. They are separate. A crawler re-sync keeps the Catalog honest.
- **Crawlers cost money and take time.** Do not run them constantly. Schedule them, or only re-crawl when new partitions land. For known schemas you can skip crawlers and register tables directly.
- **Glue jobs bill per DPU-hour** with a minimum runtime. Great for real ETL, overkill for tiny transforms. For a few MB, a Lambda may be cheaper.
- **DynamicFrame vs DataFrame.** Glue adds `DynamicFrame` (schema-flexible) on top of normal Spark `DataFrame`. You can convert between them with `.toDF()` / `.fromDF()` when you want plain Spark.
## 💛 References
- AWS Docs: What is AWS Glue: https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html
- AWS Docs: Glue Data Catalog: https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html
- AWS Docs: Crawlers: https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html
