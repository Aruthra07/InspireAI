<div align="center">

# 🚀 InspireAI

### An Always-On AI Motivation Agent Powered by AWS

<p>
  <img src="https://img.shields.io/badge/AWS-Bedrock-FF9900?style=for-the-badge&logo=amazonaws" />
  <img src="https://img.shields.io/badge/AWS-Lambda-F90?style=for-the-badge&logo=awslambda" />
  <img src="https://img.shields.io/badge/Amazon-SES-232F3E?style=for-the-badge&logo=amazonaws" />
  <img src="https://img.shields.io/badge/EventBridge-Scheduler-7B42BC?style=for-the-badge&logo=amazonaws" />
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
</p>

**An autonomous AI agent that generates and delivers motivational emails every morning using Amazon Bedrock, AWS Lambda, Amazon EventBridge Scheduler, and Amazon SES.**

---

*Built for the AWS Builder Weekend Agent Challenge 2026*

</div>

---

# 📖 Overview

InspireAI is a **serverless, event-driven AI agent** designed to inspire users every morning with an AI-generated motivational message.

Unlike traditional AI applications that wait for user interaction, InspireAI works **autonomously**. Every day at **6:30 AM IST**, the agent wakes up, generates a motivational message using **Amazon Bedrock (Nova Lite)**, and sends it directly to the user's inbox using **Amazon SES**.

Once deployed, the entire workflow runs automatically without requiring any manual intervention.

---

# ✨ Features

- 🤖 AI-powered motivational content
- ⏰ Fully automated daily execution
- ☁️ Serverless architecture
- 📧 Automatic email delivery
- ⚡ Event-driven workflow
- 🔐 Secure IAM-based permissions
- 💰 Cost-efficient using AWS managed services

---

# 🛠 AWS Services Used

| Service | Purpose |
|----------|---------|
| Amazon EventBridge Scheduler | Triggers the workflow every morning |
| AWS Lambda | Executes the application logic |
| Amazon Bedrock (Nova Lite) | Generates AI-powered motivational content |
| Amazon SES | Sends the motivational email |
| AWS IAM | Manages secure permissions |

---

# 🏗 Architecture

```text
                    Amazon EventBridge Scheduler
                                │
                                ▼
                        AWS Lambda Function
                                │
                                ▼
                 Amazon Bedrock (Nova Lite)
                                │
                  Generates AI Motivation
                                │
                                ▼
                     Amazon Simple Email Service
                                │
                                ▼
                     Motivation Delivered Daily
```

---

# 🔄 Workflow

1. Amazon EventBridge Scheduler triggers the Lambda function every morning.
2. AWS Lambda invokes Amazon Bedrock.
3. Amazon Bedrock generates motivational content.
4. Lambda formats the email.
5. Amazon SES delivers the email automatically.
6. The user receives a fresh motivational message every morning.

---

# 📂 Repository Structure

```text
InspireAI
│
├── README.md
├── requirements.txt
├── lambda_function.py
├── LICENSE
│
├── images
│   ├── inspireai-cover.png
│   └── architecture.png
│
└── screenshots
    ├── 01-bedrock.png
    ├── 02-lambda.png
    ├── 03-lambda-success.png
    ├── 04-ses.png
    ├── 05-eventbridge.png
    └── 06-email-output.png
```

---

# 🚀 Getting Started

## Prerequisites

- AWS Account
- Amazon Bedrock enabled
- Amazon SES verified email identity
- Python 3.x
- boto3

Install dependencies:

```bash
pip install boto3
```

Deploy:

- Create an AWS Lambda function.
- Copy the contents of `lambda_function.py`.
- Attach IAM permissions for Bedrock and SES.
- Configure Amazon EventBridge Scheduler.
- Verify your email in Amazon SES.
- Test the Lambda function.

---

# 📸 Project Screenshots

## Amazon Bedrock

_Add screenshot here_

---

## AWS Lambda

_Add screenshot here_

---

## Lambda Test

_Add screenshot here_

---

## Amazon SES

_Add screenshot here_

---

## EventBridge Scheduler

_Add screenshot here_

---

## Email Output

_Add screenshot here_

---

# 💡 Challenges

During development, I learned how to:

- Configure Amazon Bedrock model access
- Manage IAM permissions securely
- Verify identities using Amazon SES
- Build event-driven workflows
- Connect multiple AWS managed services together

---

# 📚 What I Learned

This project strengthened my understanding of:

- Serverless application development
- Event-driven architecture
- Generative AI using Amazon Bedrock
- Email automation with Amazon SES
- AWS IAM permissions
- Autonomous AI agents

---

# 🚀 Future Enhancements

- Personalized motivational messages
- Multi-language support
- HTML email templates
- User subscriptions
- Weather-aware inspiration
- Calendar-aware productivity suggestions
- Amazon DynamoDB integration
- Amazon SNS notifications
- Voice output using Amazon Polly

---

# 💻 Source Code

Clone the repository:

```bash
git clone https://github.com/Aruthra07/InspireAI.git
```

---

# 👨‍💻 Author

**Aruthra S M**

Electronics & Communication Engineering Student

AWS Builder Challenge 2026

GitHub: https://github.com/Aruthra07

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

⭐ If you found this project interesting, consider giving it a star!

</div>
