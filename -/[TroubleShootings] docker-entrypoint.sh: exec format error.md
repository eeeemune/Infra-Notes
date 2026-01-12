# 😵 Error Situation

## Error Message

```bash
exec /usr/local/bin/docker-entrypoint.sh: exec format error
```

# 🤔 Why was it Happened?

## Reason

### The problematic code

```tsx
exec /usr/local/bin/docker-entrypoint.sh: exec format error                
                                                                             
stream closed: EOF for infra/chartmetric-master-rabbitmq-54d97bf5bb-nbd2c(master-ra...)
```

# 😋 Solution

<aside>

💚 **Key Takeaway**

Architecture mismatch. Check if the image is running in proper architecture on your terminal

</aside>

```bash
# Check the image's architecture
docker inspect rabbitmq@sha256:9cfb7e92ae7d296aec4d1ae799e431209f7ed57d55f9c929d95667d0ccf1c920 --format '{{.Architecture}}'
```
