# 💚 Add a New GitHub Member with Terraform

## 💛 Go to the Files

```bash
cd code/chartmetric/infra/github/terraform

# teams.terraform → defines GitHub teams
# membership.terraform → defines who’s in each team
```

## 💛 Add a New Member

```hcl
# membership.tf  
  merge(var.member, {
    username = "github_user_id"
    teams    = ["front-end", "back-end"]
  }),
```

## 💛 Apply Terraform

```bash
terraform init
terraform plan
terraform apply
```

## 💛 Commit the Change & Create a PR

```bash
git add .
git commit -m "new: add Eunhye as a front-end, back-end team member"
git push origin
```
