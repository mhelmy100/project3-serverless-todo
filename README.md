# Serverless REST API with DynamoDB & API Gateway

## 📌 Project Overview
This project is a **serverless REST API** for managing a simple to-do list.  
It uses **AWS Lambda**, **Amazon API Gateway**, and **Amazon DynamoDB** to handle CRUD operations without managing any servers.  
The frontend is hosted on **Amazon S3**.

---

## 🏗 Architecture
- **Amazon API Gateway** – Exposes REST API endpoints.
- **AWS Lambda** – Handles backend logic for CRUD operations.
- **Amazon DynamoDB** – NoSQL database to store items.
- **AWS IAM** – Manages roles and permissions for security.
- **Amazon CloudWatch** – Logs and monitoring.
- **Amazon S3** – Static website hosting for the frontend.

---

## 🚀 Features
- Create, Read, Update, and Delete (CRUD) operations.
- Serverless, pay-per-use architecture.
- NoSQL database with high scalability.
- Static frontend for interaction.

---

## 📂 Project Structure
```
project3-serverless-todo/
│── backend/
│   ├── src/              # Lambda function source code
│   ├── requirements.txt  # Python dependencies
│── frontend/
│   ├── index.html         # Main HTML page
│   ├── app.js             # JavaScript logic
│── template.yaml          # AWS SAM template
│── postman_collection.json # API test collection
```

---

## ⚙ Deployment
### 1. Deploy Backend with AWS SAM
```bash
sam build
sam deploy --guided
```

### 2. Deploy Frontend to S3
```bash
aws s3 cp frontend/ s3://your-bucket-name --recursive
```

---

## 📄 License
This project is open source under the MIT License.
