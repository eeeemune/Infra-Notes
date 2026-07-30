# 💚 Kubernetes Job

## 💛 What is it?
A **Job** runs one or more pods until they **finish successfully**, then stops. It is how Kubernetes runs a task that has an end, not a service that runs forever.
Contrast with a Deployment: a Deployment keeps pods running and restarts them whenever they exit. A Job is the opposite, it wants the pod to exit, and it considers the work done once the pod succeeds.
## 💛 Why do we need it?
A Deployment assumes "this should always be up." Plenty of work is not like that:
- Database migrations before a release
- A one-off data backfill or cleanup
- Sending a batch of emails
- Processing a queue of files
For these you want something that runs to completion, tracks success or failure, retries on failure, and then is finished. That is a Job.
### 🤍 Real-world use case
Before your app rolls out, a Job runs `python manage.py migrate` once. If it succeeds, the deploy proceeds. If it fails, the Job is marked Failed and you notice before shipping broken schema.
## 💛 How does it work?
- The Job creates a pod and watches it.
- The pod's `restartPolicy` must be `Never` or `OnFailure`. `Always` is rejected, because that is for services that should never stop.
- If the pod exits 0, the Job counts one **completion**.
- If the pod fails, the Job retries by creating a new attempt, up to `backoffLimit` times, with exponential backoff.
- Once the required number of completions is reached, the Job is **Complete**.
### 🤍 Key fields
- `completions`: how many successful pods you need (default 1).
- `parallelism`: how many pods may run at the same time.
- `backoffLimit`: how many failures before the Job is marked Failed (default 6).
- `activeDeadlineSeconds`: a hard wall-clock timeout for the whole Job.
- `ttlSecondsAfterFinished`: auto-delete the Job and its pods this many seconds after it finishes.
### 🤍 Lifecycle Flow
```javascript
Job created
  |
  v
create pod  ->  run to completion
  |
  +-- exit 0     -> completion counted
  |                   |
  |                   v
  |              enough completions? -> Job Complete
  |
  +-- non-zero   -> retry with a new pod, up to backoffLimit
                        |
                        v
                  backoffLimit reached -> Job Failed
```
### 🤍 Example: a one-off migration Job
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migrate
spec:
  backoffLimit: 3
  ttlSecondsAfterFinished: 300     # auto-delete 5 min after finishing
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: myapp:1.4.2
          command: ["python", "manage.py", "migrate"]
```
### 🤍 Example: a parallel batch Job
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: resize-images
spec:
  completions: 10     # 10 items must succeed in total
  parallelism: 3      # up to 3 pods running at once
  backoffLimit: 6
  template:
    spec:
      restartPolicy: OnFailure
      containers:
        - name: worker
          image: image-resizer:latest
```
### 🤍 Handy commands
```bash
kubectl apply -f job.yaml
kubectl get jobs
kubectl logs job/db-migrate      # logs from the Job's pod
kubectl delete job db-migrate    # also deletes its pods
```
## 💛 Job vs CronJob
A **CronJob** creates Jobs on a schedule using cron syntax. It is essentially a Job factory.
- Use a **Job** for "run this once, now" (a migration, a backfill).
- Use a **CronJob** for "run this every night at 2am" (a nightly report, a cleanup).
Each time a CronJob fires, it creates a fresh Job, which in turn creates pods.
## 💛 Gotcha
- **restartPolicy cannot be Always.** Use `Never` or `OnFailure`. With `Never`, each retry is a brand-new pod, so you can inspect every failed attempt. With `OnFailure`, the container restarts inside the same pod, which hides the earlier failures. `Never` is usually easier to debug.
- **Finished Jobs are not auto-cleaned by default.** Completed Jobs and their pods linger, which is handy for reading logs but piles up over time. Set `ttlSecondsAfterFinished`, or delete them yourself.
- **backoffLimit is a ceiling, not infinity.** A crash-looping Job stops retrying once it hits `backoffLimit` and is marked Failed. It does not retry forever.
- **completions vs parallelism.** `completions` is the total number of successes required; `parallelism` is how many run concurrently. For a shared work queue you often set only `parallelism` and let workers drain the queue.
- **Deleting a Job deletes its pods and their logs.** Grab the logs before cleanup if you need them.
## 💛 References
- Kubernetes docs: Jobs: https://kubernetes.io/docs/concepts/workloads/controllers/job/
- Kubernetes docs: CronJob: https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/
- Kubernetes docs: automatic cleanup (TTL) for finished Jobs: https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/
