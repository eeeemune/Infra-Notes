# 💚 How to Set Up AWS Resource Notification

# 💚 How to Set Up AWS Resource Notification
## 💛 Configure AWS Chatbot with Slack
1. Click "Configure new client" → Select Slack
  1. Authorize AWS Chatbot in your Slack workspace
  1. For us, we already have a Slack workspace
1. Click "Configure new channel"
  1. Configuration name
  1. Slack channel: select the channel (e.g., #ecs-alerts)
  1. Permissions: Choose "Channel IAM role" → Create new role
### 🤍 Subscribe Topics
- Edit configuration
- Add `Notifications`
## 💛 Create SNS Topic
## 💛 Amazon EventBridge (Event Detection)
**EventBridge **
How it works:
- AWS services automatically emit events when things happen (task started, task stopped, file uploaded, etc.)
- EventBridge lets you create rules that filter for specific events
- When a matching event occurs, it routes it to a target (SNS, Lambda, etc.)
In our case:
- ECS emits a "Task State Change" event whenever a task stops
- Our rule filters for events where stopCode = "SpotInterruption"
- When matched, it sends the event to SNS
