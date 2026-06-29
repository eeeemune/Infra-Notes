# 💚 AWS Spot Instance Data Feed

# 💚 AWS Spot Instance Data Feed
## 💛 What it is
A resource that turns on AWS's Spot Instance data feed.
Once enabled, **EC2 delivers a gzipped CSV to an S3 bucket you own**, ~once per hour, with one row per running spot instance per hour.
```hcl
resource "aws_spot_datafeed_subscription" "default" {
  bucket = aws_s3_bucket.spot_datafeed.id   # where AWS delivers the CSVs
  prefix = "spot-feed"                       # key prefix inside the bucket
}
```
## 💛 What's in each file
→ It's the authoritative record of what your spot instances really cost, instance-by-instance, hour-by-hour.
## 💛 Why we(Chartmetric) need it
- We’re about to adopt OpenCost to analysis the actual cost we need to run each DAGs/Airflow Tasks
- Spot has no fixed list price, it floats. OpenCost reads this feed from S3 to learn the realized spot price per instance.
- Without it, OpenCost falls back to on-demand list price, overstating every DAG ~60–70% (the airflow-task pool is 100% spot).
## 💛 Good to know
- **One per account, account-wide.** Can't have two
  - This covers all spot instances in the account.
- **It’s Free.** You only pay trivial S3 storage
  - A 30-day lifecycle rule in will keep it near-zero.
- Not retroactive. Data starts only after enabling; first file can take a few hours, so OpenCost's spot accuracy kicks in shortly after apply, not instantly.
