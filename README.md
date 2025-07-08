# 🍕 Pizza Ordering Chatbot – AWS Project

An intelligent, interactive chatbot named **PizzaBuddy** that allows users to order pizzas through natural conversation. Built using **Amazon Lex**, **AWS Lambda**, and **Amazon DynamoDB**, this chatbot processes user input, stores order details, and offers full-cycle order management.

---

## 📌 Features

- Place new pizza orders
- Cancel existing orders
- Greet users and handle undefined inputs gracefully
- Store order data in DynamoDB
- Backend logic with AWS Lambda (Python)
- Fully integrated with Amazon Lex

---

## 🧰 Technologies Used

- **Amazon Lex** – Natural language chatbot interface
- **AWS Lambda** – Backend logic processing (Python 3.13)
- **Amazon DynamoDB** – Persistent order data storage
- **Amazon CloudWatch** – Monitoring and troubleshooting
- **IAM Roles & Policies** – Secure access control for Lambda and DynamoDB

---

## ⚙️ Setup Instructions

### Step 1: AWS Console Setup
- Log into AWS Management Console
- Navigate to Lex, Lambda, DynamoDB, and IAM services

### Step 2: Lex Bot Creation
- **Bot Name**: `PizzaBuddy`
- **Description**: _“An interactive chatbot that makes pizza ordering fun and effortless!”_
- Language: English (US)
- Create intents and slot types

### Step 3: Intents
- `PizzaOrder` – Take new orders
- `CancelOrder` – Cancel placed orders
- `WelcomeIntent` – Greets users
- `FallbackIntent` – Handles unrecognized input

### Step 4: Slots for PizzaOrder
| Slot Name        | Description                     |
|------------------|----------------------------------|
| `PizzaSize`      | Small, Medium, Large             |
| `CrustType`      | Thin, Thick, Cheese Burst        |
| `Toppings`       | User’s selected toppings         |
| `CustomerName`   | User’s name                      |
| `DeliveryAddress`| Address for delivery             |
| `PhoneNumber`    | User's contact number            |

### Step 5: Lambda Function
- Name: `PizzaOrderHandler`
- Runtime: Python 3.13
- Stores order in DynamoDB table `PizzaOrders`
- IAM Role: `PizzaOrderHandler-role`
    - Permissions: `dynamodb:PutItem`, `logs:PutLogEvents`, etc.

### Step 6: DynamoDB Table
- **Table Name**: `PizzaOrders`
- **Partition Key**: `orderId` (String)
- Mode: On-Demand capacity

### Step 7: TestBotAlias Configuration
- Use built-in alias `TestBotAlias`
- Connect to Lambda and Lex version

---

## 🧪 Sample Conversation

**Ordering a Pizza**  
```
User: I want to order pizza  
Bot: What size of pizza would you like?  
User: Medium  
Bot: What crust would you prefer?  
User: Cheese Burst  
Bot: What toppings would you like?  
User: Onions and olives  
Bot: May I have your name?  
User: Kelly  
Bot: Delivery address, please.  
User: 123 Main Street, Kalikapur, Kolkata  
Bot: Contact number?  
User: 9856124567  
Bot: Thank you Kelly! Your Medium pizza with Cheese Burst crust and onions, olives will be delivered to 123 Main Street, Kolkata.
```

**Canceling an Order**  
```
User: Cancel my order  
Bot: What is your Order ID?  
User: 49c5xxxx-xxxx  
Bot: Your order with ID 49c5xxxx-xxxx has been successfully canceled.
```

---

## 📈 Monitoring

- **Amazon CloudWatch Logs** used to monitor Lambda execution and troubleshoot errors
- Logs include request and response tracking from Lex

---

## 🔒 IAM Roles and Policies

- `PizzaOrderHandler-role` grants:
  - `AmazonDynamoDBFullAccess`
  - `AWSLambdaBasicExecutionRole`

---

## 👤 Author

**Triparna**  
Pizza ordering automation using AWS Lex, Lambda, and DynamoDB.

---

## 📄 License

This project is built for learning and demonstration purposes. Modify freely as needed.
