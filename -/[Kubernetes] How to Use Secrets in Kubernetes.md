# 💚 How to Use Secrets in Kubernetes

## 💛 Create a Secret

```bash
kubectl create secret generic <name>  \
    --from-literal=username=admin \
    --from-literal=password='S!B\*d$zDsb='
```

- You can create secrets for `kubectl` command in bash
- Once you succeed, you will see the output like:
    
    ```bash
    secret/XXX created
    ```
    

## 💛 Check The Secret

### 🤍 List Up Secrets

```bash
kubectl get secrets
```

- Example
    
    ```bash
    NAME              TYPE       DATA      AGE
    db-user-pass      Opaque     2         51s
    ```
    

### 🤍 See The Value for Secret

1. View the contents of the Secret you created:
    
    ```bash
    kubectl get secret db-user-pass -o jsonpath='{.data}'
    ```
    
2. The output is similar to:
    
    ```bash
    { **"password"**: "UyFCXCpkJHpEc2I9", **"username"**: "YWRtaW4=" }
    ```
    
3. Decode the `password` data:
    
    ```bash
    echo 'UyFCXCpkJHpEc2I9' | base64 --decode
    ```
    
    The output is similar to:
    
    ```
    S!B\*d$zDsb=
    ```
    

## 💛 References

https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/
