# 💚 Data-Driven Design Pattern

## 💛 What is Data-Driven Design Pattern?

<aside>

Behavior is controlled by data, not hard-coded logic

</aside>

Instead of writing many `if/else` or `switch` statements, you define rules/configurations in data (JSON, DB, config files) and let the program read it.

- Define configuration data in one place, and implement settings references the data configuration file.
- On `chartmetric-infra` repo, you can see how this pattern is applied.

## 💛 Why Use It?

- Less hardcoding
- Easier to change behavior without modifying code
- More flexible and scalable
- Good for configs, rules, and dynamic systems

## 💛 Example

- Let’s say we’re granting different access levels depends on the user role…

### 🤍 Traditional (Hard-coded)

```python
if user.role == "admin":
    access_level = 10
elif user.role == "guest":
    access_level = 1
```

### 🤍 Data-Driven

```python
ROLE_CONFIG = {
    "admin": 10,
    "guest": 1
}
access_level = ROLE_CONFIG[user.role]
```

## 💛 Summary

- Data-driven == "Let data control behavior"
- Reduce code changes
- Increase flexibility
