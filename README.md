# IoT-Based Smart Home Automation using AWS IoT Core

## 📌 Project Overview

This project demonstrates a **Smart Home Automation System** powered by **AWS IoT Core**, enabling users to remotely control virtual devices such as smart lights, fans, locks, and air conditioners through MQTT messages. The system is built entirely on AWS cloud services **without any physical hardware**, showcasing how IoT and serverless technologies can be integrated for a scalable and cost-effective solution.

---

## 🧠 Key Features

- Virtual IoT device simulation
- MQTT-based message communication
- Real-time command processing using AWS Lambda
- Device state tracking using DynamoDB
- SMS and Email alerts via Amazon SNS
- Fully cloud-native and serverless architecture

---

## 🛠️ AWS Services Used

- **AWS IoT Core**: Acts as the central MQTT broker for managing devices and handling message flows.
- **AWS Lambda**: Executes backend logic in response to incoming MQTT messages.
- **Amazon DynamoDB**: Stores the current state and activity logs of smart devices.
- **Amazon SNS**: Sends real-time alerts to users via SMS and email.
- **IAM (Identity and Access Management)**: Controls secure service-to-service access.

---

## 🔄 Project Workflow

### Step 1: Register IoT Things
Created 4 virtual IoT Things in AWS IoT Core:
- `smart_light_01`
- `smart_fan_01`
- `smart_lock_01`
- `smart_ac_01`

### Step 2: Set Up MQTT Communication
- Subscribed to a topic named `smartHome/actions` using the MQTT Test Client.
- Used this topic to simulate device commands with JSON payloads.

### Step 3: Create AWS Lambda Function
- Developed a function named `ProcessSmartHomeActions`.
- It processes MQTT messages and updates the device state in DynamoDB.
- Also triggers SNS alerts for every action received.

### Step 4: Configure IAM Permissions
- Created an IAM Role with attached policies:
  - `AWSIoTFullAccess`
  - `AmazonDynamoDBFullAccess`
  - `AmazonSNSFullAccess`
- Attached this role to the Lambda function.

### Step 5: Set Up DynamoDB
- Created a table `SmartHomeData` with `device_id` as the primary key.
- Stores each device's `action`, `timestamp`, and `status`.

### Step 6: Configure SNS for Alerts
- Created a topic `SmartHomeAlerts`.
- Subscribed an email and a mobile number for notifications.
- Confirmed both subscriptions via received messages.

### Step 7: Publish Device Commands
- Sent messages like:
```json
{
  "device_id": "smart_light_01",
  "action": "TURN_ON"
}
```
---
## 🎓 Learning Outcomes

* Gained hands-on experience with AWS IoT Core and MQTT protocol.
* Learned to integrate serverless logic using AWS Lambda.
* Understood the use of DynamoDB for storing IoT state.
* Implemented real-time alerts via Amazon SNS.
* Built a functional cloud-native IoT solutionwithout hardware.
* Strengthened problem-solving skills while working in a cloud ecosystem.

---
## ✅ Conclusion
This project illustrates how to build an end-to-end smart home automation system using only AWS services. It leverages MQTT-based messaging, serverless computing, and event-driven architecture to offer a scalable and modular framework for future expansion. The use of cloud-only resources provides a fast, secure, and cost-efficient way to prototype and develop IoT applications.
---
## 📚 References
- [1] AWS IoT Core Documentation: https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html
- [2] AWS Lambda Documentation: https://docs.aws.amazon.com/lambda
- [3] AWS DynamoDB: https://docs.aws.amazon.com/amazondynamodb
- [4] Amazon SNS: https://docs.aws.amazon.com/sns
- [5] MQTT Protocol: https://mqtt.org
---
## 💡 Author
### Manojkumar Sanda | Third-year B.Tech Student @ KL University

Passionate about Full Stack Development & Cloud-Based Projects
---


