# 💚 How to Sign in Docker with AWS SSO

# 💚 Command
```bash
aws ecr get-login-password --region <region> --profile <profile_name> | docker login --username AWS --password-stdin <repository_url>
```
# 💚 Explain
## 💛 Sign in Docker with Terminal
```bash
 docker login --username <your_id> --password-stdin <your_repository_URL>
```
- `--password-stdin`: receive password from terminal input (stdin)
## 💛 Sign in Docker by AWS Profile
```bash
 docker login --username aws --password <credential_key> <your_repository_URL>
```
- `username`: aws
- `password`: your `login-password`
  - You can get `login-password` by this command:
```bash
 aws ecr get-login-password --region <your_region> --profile <profile_name>
```
  - **chartmetric region is **`us-west-2`
# 💚 Reference
https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html
https://docs.docker.com/reference/cli/docker/login/
