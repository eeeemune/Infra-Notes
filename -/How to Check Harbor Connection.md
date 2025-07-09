# 💚 How to Check Harbor Connection

## 💛 Background

- When your harbor registry returns `500` errors like this:
    
    ```bash
    error: unexpected status from HEAD request to http://10.1.10.198:30001/v2/chartmetric/shipit/blobs/...: 500 Internal Server Error
    ```
    
- You can inspect the healthy state of your registry

## 💛 How to check

### 🤍 Command

```bash
curl -k http://<registry_ip>/api/v2.0/health
```

### 🤍 Succeed

- Once it succeed, your terminal will say…

```bash
{"components":[{"name":"core","status":"healthy"},{"name":"database","status":"healthy"},{"name":"jobservice","status":"healthy"},{"name":"portal","status":"healthy"},{"name":"redis","status":"healthy"},{"name":"registry","status":"healthy"},{"name":"registryctl","status":"healthy"},{"name":"trivy","status":"healthy"}],"status":"healthy"}
```

### 🤍 Failure

```bash
404 page not found
```
