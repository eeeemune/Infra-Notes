# 💚 How to Run a Command on a Docker Image Stored in AWS ECR

## 💛 Authenticate Docker with ECR

```jsx
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com
```

### 🤍 Example

```bash
aws ecr get-login-password --region us-west-2 --profile eunhye \
  | docker login --username AWS --password-stdin 897744604563.dkr.ecr.us-west-2.amazonaws.com
```

## 💛 Pull the Image From ECR

```jsx
docker pull <account_id>.dkr.ecr.<region>.amazonaws.com/<repository>:<tag>
```

## 💛 Run the Image With a Command

Use docker run followed by the command you want to execute inside the container.

```jsx
docker run --rm <account_id>.dkr.ecr.<region>.amazonaws.com/<repository>:<tag> <command>
```

## 💛 Start an Interactive Shell

```jsx
docker run -it --rm <account_id>.dkr.ecr.<region>.amazonaws.com/<repository>:<tag> /bin/bash
```

or if Alpine-based:

```jsx
docker run -it --rm <account_id>.dkr.ecr.<region>.amazonaws.com/<repository>
```
