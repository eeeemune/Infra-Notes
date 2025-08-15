## 💚 How to set a team as Auto-Assigned Reviewers

### 💛 Make Sure You Have a GitHub Team

- Go to your organization’s **Teams** section.
- Create a team (or use an existing one), e.g., `@my-org/backend-team`.
- Ensure the team has **Write** or **Maintain** access to the repository.

### 💛 Create or Edit a `CODEOWNERS` File

- Place it in one of these locations:
    - `.github/CODEOWNERS`

Example:

```
# All `.py` files will be reviewed by the backend team
*.py    @my-org/backend-team

# All files in the frontend folder will be reviewed by the frontend team
/frontend/    @my-org/frontend-team
```

### 💛 Enable CODEOWNERS Auto-Assignment in Settings

1. Go to **Repository → Settings → Pull Requests**.
2. Under **Code review**, check:
    - "Require review from Code Owners"
    - **"Automatically request reviews from Code Owners"**

### 💛 Things to Note

- **Team mentions** must be in the form `@org/team-name`, not just `@team-name`.
- The team must have repository access.
- Rules are matched **top to bottom** in CODEOWNERS; the last matching line applies.
