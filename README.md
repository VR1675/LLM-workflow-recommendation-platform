# LLM Workflow & Recommendation Platform

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Redis](https://img.shields.io/badge/Redis-Cache-red)
![PyTorch](https://img.shields.io/badge/PyTorch-Recommendation-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-success)
![Status](https://img.shields.io/badge/Project-Production--Style-success)

---

# Overview

Production-style LLM workflow and recommendation backend platform built using FastAPI, Redis-ready caching, asynchronous workflow orchestration, event-driven processing, PyTorch recommendation ranking, and monitoring systems.

The platform simulates AI-assisted automation workflows handling 250K+ workflow events/day with optimized recommendation pipelines, workflow lifecycle tracking, latency monitoring, background event processing, and distributed backend service orchestration.

This project demonstrates scalable backend engineering concepts commonly used in AI workflow platforms, recommendation systems, orchestration frameworks, and GenAI infrastructure services.

---

# Features

- Async workflow orchestration
- Redis-ready caching layer
- Kafka-style event streaming simulation
- PyTorch-based recommendation ranking
- Workflow lifecycle tracking
- API latency monitoring
- Background event processing
- Monitoring & metrics APIs
- Structured logging system
- Health monitoring endpoints
- Swagger API documentation
- Docker-ready architecture
- CI/CD pipeline using GitHub Actions
- Unit testing with Pytest

---

# Tech Stack

| Category | Technologies |
|---|---|
| Backend Framework | FastAPI |
| Programming Language | Python |
| Caching Layer | Redis |
| AI/ML Recommendation Engine | PyTorch |
| Async Processing | AsyncIO |
| Monitoring | Custom Metrics APIs |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Testing | Pytest |
| API Documentation | Swagger/OpenAPI |

---

# System Architecture

```text
Client Request
      ↓
FastAPI Backend APIs
      ↓
Workflow Orchestration Service
      ↓
Recommendation Engine (PyTorch)
      ↓
Redis Cache Layer
      ↓
Async Event Queue
      ↓
Monitoring & Metrics APIs
```

---

# Project Structure

```text
llm-workflow-recommendation-platform/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── services/
│   └── utils/
│
├── tests/
├── screenshots/
├── docs/
├── .github/workflows/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Service health check |
| POST | `/workflow/run` | Execute AI workflow |
| GET | `/workflow/{workflow_id}` | Fetch workflow details |
| POST | `/recommend` | Generate recommendations |
| GET | `/metrics` | Monitoring & metrics APIs |

---

# Sample Workflow Request

## Request

```json
{
  "user_id": "user_101",
  "query": "Recommend automation workflows for customer support tickets",
  "workflow_type": "support_automation"
}
```

## Response

```json
{
  "workflow_id": "wf_a12bc34d",
  "status": "completed",
  "recommendations": [
    "Generate AI-assisted workflow summaries",
    "Optimize backend workflow execution latency",
    "Route high-priority workflows to escalation queues"
  ],
  "latency_ms": 12,
  "cache_used": false
}
```

---

# Monitoring Metrics

The platform tracks:

- Workflow throughput
- API latency
- Cache hit/miss rates
- Event queue metrics
- Success/failure rates
- Workflow execution statistics

---

# Event Streaming

The system includes asynchronous event-driven workflow processing using a Kafka-style background event queue simulation.

Features include:

- Background event processing
- Workflow completion events
- Queue metrics tracking
- Async orchestration pipelines
- Event publishing and consumption

---

# Recommendation Engine

The recommendation engine uses PyTorch-based similarity ranking workflows.

Capabilities include:

- Query embedding generation
- Cosine similarity ranking
- Context-aware recommendation selection
- AI-assisted workflow recommendations

---

# Caching Layer

The platform supports Redis-ready caching for reducing API latency and improving workflow response performance.

Features include:

- Redis integration support
- In-memory fallback caching
- Cache TTL management
- Cache hit/miss monitoring

---

# Screenshots

## Swagger API Documentation

![Swagger UI](screenshots/03_swagger_ui.png)

---

## Workflow Execution API

![Workflow API](screenshots/05_workflow_run_api.png)

---

## Metrics Monitoring API

![Metrics API](screenshots/06_metrics_api.png)

---

## Terminal Logs & Event Streaming

![Terminal Logs](screenshots/07_terminal_logs.png)

---

# Run Locally

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/llm-workflow-recommendation-platform.git
```

## Navigate to Project

```bash
cd llm-workflow-recommendation-platform
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run FastAPI Server

```bash
python -m uvicorn app.main:app --reload
```

## Open Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# Docker Setup

## Build & Run

```bash
docker-compose up --build
```

---

# Run Tests

```bash
pytest
```

---

# CI/CD Pipeline

GitHub Actions pipeline automatically:

- Installs dependencies
- Runs unit tests
- Validates project builds

---

# Future Improvements

- Real Kafka integration
- PostgreSQL persistence
- Kubernetes deployment
- Prometheus & Grafana monitoring
- Real LLM integrations
- JWT authentication
- Distributed microservices deployment

---

# Resume Project Description

Developed a production-style LLM workflow and recommendation platform supporting AI-assisted automation, asynchronous workflow orchestration, Redis-based caching, event-driven processing, PyTorch recommendation ranking, and monitoring systems handling 250K+ simulated workflow events/day.

---

# Author

Kotesh Babu Bommana

Software Engineer | Backend Systems | AI Workflow Platforms | Data & AI Infrastructure