# 💚 How to Use requirements.txt in Python

## 💛 What is requirements.txt?

It’s a plain text file that lists **all the Python packages your project needs** — one per line.

Example:

```
requests==2.31.0
flask>=2.0
numpy
```

## 💛 Install Packages from requirements.txt

Use `pip` to install all packages listed:

```bash
pip install -r requirements.txt
```

## 💛 Create Your Own requirements.txt

If you've already installed packages in a **virtual environment**:

```bash
pip freeze > requirements.txt
```

This will save **exact versions** of all installed packages.

## 💛 4. Use with Virtual Environments

It’s a good practice to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate 

pip install -r requirements.txt
```

## 💛 Best Practices

- Pin versions (`==`) for production
- Use comments to explain packages

```
# Web framework
flask==2.3.3
```

## 💛 References

- [pip docs - requirements files](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
- [Python Packaging Guide](https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/)
