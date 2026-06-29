# 💚 How to Test RDS Connection on Mac

# 💚 How to Test RDS Connection on Mac
Using `psql`
## 💛 Install PostgreSQL
```bash
brew install postgresql
```
## 💛 Test
### 🤍 basic connectivity
```bash
pg_isready -h cm-rds-postgres.cni52ceaa2ty.us-west-2.rds.amazonaws.com -p 5432
```
### 🤍 Test with credentials
```bash
psql -h prod2.cluster-cni52ceaa2ty.us-west-2.rds.amazonaws.com \
       -p 5432 \
       -U eunhye \
       -d chartmetric \
       -c "SELECT version();"
```
