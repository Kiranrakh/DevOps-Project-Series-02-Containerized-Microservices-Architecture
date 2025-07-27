# 🚀 DevOps Project Series 02: Containerized Microservices Architecture (Flask + Redis)

This project showcases a **containerized microservice architecture** using **Flask**, **Redis**, and **Docker Compose**. The goal is to demonstrate a lightweight yet functional user registration system with **caching** capabilities using Redis.

It’s part of my hands-on DevOps journey at **LinuxWorld Informatics Pvt Ltd** under the mentorship of **Vimal Daga Sir**.

---

## 📌 Project Use Case

> “Build a simple user management API service where users can be registered and queried. To optimize repeated access, cache the user details using Redis.”

---

## 🏗️ Architecture Overview

```

```
                ┌────────────┐
                │   Client   │
                └────┬───────┘
                     │ HTTP Requests
                     ▼
              ┌──────────────┐
              │ Flask User   │
              │  Microservice│
              └────┬───────┬─┘
                   │       │
    Redis Cache ◄──┘       └──► In-Memory Store (Dict)
```

```

- 👤 Client sends requests to register or fetch user
- 🐍 Flask handles API logic and caches user data in Redis
- ⚡ Redis serves faster responses for repeated requests

---

## 🧰 Tech Stack

| Layer        | Tool                  |
|--------------|------------------------|
| Backend API  | Flask (Python 3.11)    |
| Caching      | Redis 7.0              |
| Containerization | Docker & Docker Compose |
| Orchestration | Docker Compose         |
| System       | Linux-based Docker Engine |

---

## 📂 Folder Structure

```


├── docker-compose.yml
├── userapp/
│   ├── app/
│   │   ├── **init**.py      # App factory and Redis setup
│   │   ├── config.py        # Redis config
│   │   ├── routes.py        # API routes
│   │   └── utils.py         # JSON response helpers
│   ├── Dockerfile
│   ├── requirements.txt
│   └── run.py               # Entry point
├── redis.tar                # Redis image (offline use)
├── python.tar               # Python image (offline use)
└── README.md

````

---

## ⚙️ Prerequisites

- ✅ Docker Desktop installed and running
- ✅ Git Bash, PowerShell, or Terminal
- ✅ (Optional) Preloaded Redis and Python images for offline use

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Kiranrakh/DevOps-Project-Series-02-Containerized-Microservices-Architecture.git
cd DevOps-Project-Series-02-Containerized-Microservices-Architecture
````

### 2️⃣ Build and Start Services

```bash
docker-compose build
docker-compose up
```

This will:

* Build the Flask app Docker image
* Start the `userapp` and `redis` services
* App runs at: `http://localhost:5000`

---

## 📮 API Endpoints

### 📤 Register a User

```bash
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "kiran", "email": "kiran@example.com"}'
```

✅ Response:

```json
{
  "message": "User 'kiran' registered successfully!",
  "data": {
    "username": "kiran",
    "email": "kiran@example.com"
  }
}
```

---

### 📥 Get User Info

```bash
curl http://localhost:5000/user/kiran
```

✅ Response (from Redis cache):

```json
{
  "message": "User 'kiran' found in cache.",
  "data": {
    "username": "kiran",
    "email": "kiran@example.com"
  }
}
```

---

## 🧪 Testing in Browser

You can open:

```
http://localhost:5000/user/kiran
```

And see the cached response.

---

## 🧼 Stop Services

```bash
docker-compose down
```

---

## 🧠 Key Concepts Demonstrated

* ✅ Microservice containerization using Docker
* ✅ API state caching using Redis
* ✅ Multi-container orchestration using Docker Compose
* ✅ Error handling, modular Python app design
* ✅ curl-based testing without Postman

---

## 🔧 Troubleshooting

### ❗ Pull Error (Redis or Python image)

If Docker fails to pull images:

```bash
# On a machine with internet
docker pull redis:7.0.0
docker save redis:7.0.0 -o redis.tar

docker pull python:3.11-slim
docker save python:3.11-slim -o python.tar

# On your local machine
docker load -i redis.tar
docker load -i python.tar
```

---



## 👨‍💻 Maintainer

**Kiran Rakh**
DevOps Engineer | AWS & Cloud Enthusiast
LinuxWorld Informatics Pvt Ltd (DevOps Internship)
📍 Pune, India
📧 [kiranrakh155@gmail.com](mailto:kiranrakh155@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/kiran-rakh)
🔗 [GitHub](https://github.com/kiranrakh)

---

## ⭐ Star & Fork

If this helped you, consider giving it a ⭐ and sharing with fellow DevOps learners!

```

---

