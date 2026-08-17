# Enterprise AI Support & Incident Resolution Platform
## Project Learning Summary — Checkpoint 1

### 1. Project Goal
We are building a real-world, end-to-end AI Support & Incident Resolution Platform for enterprise IT support.

The system should help support engineers:
- understand incoming support tickets
- classify the problem
- predict priority
- find similar historical incidents
- search the company knowledge base
- recommend a resolution
- identify tickets related to the same incident
- keep a human support engineer in control of final actions

This is NOT a simple chatbot or Kaggle ML demo.

### 2. Main Project Flow
Employee
  -> creates ticket
  -> FastAPI backend
  -> database + AI engine
  -> classification
  -> priority prediction
  -> similar-ticket search
  -> knowledge-base/RAG search
  -> resolution recommendation
  -> support engineer
  -> resolve or escalate

Important principle:
AI recommends; humans remain in control for important actions.

### 3. Main Support Categories
1. Network
2. Email
3. Authentication
4. Hardware
5. Software
6. Database
7. Cloud
8. Security
9. Application
10. Access Management

Priority levels:
- Low
- Medium
- High
- Critical

Ticket statuses:
- OPEN
- ASSIGNED
- IN_PROGRESS
- WAITING_FOR_USER
- RESOLVED
- CLOSED
- ESCALATED

### 4. Ticket vs Incident
A ticket is a report from a user.

An incident is an underlying problem that can affect many tickets.

Example:
INC001 = VPN Authentication Failure
  -> T001
  -> T002
  -> T003

This allows the project to detect related/duplicate incidents.

### 5. Data Strategy
We will use a hybrid data strategy:
- public support-ticket data where the license permits
- synthetic enterprise data that we generate ourselves
- our own technical knowledge-base documents

We will NOT depend on one perfect dataset.

Initial target:
- start with a small dataset for development
- then expand to thousands of tickets
- eventually work toward 20,000+ realistic records if useful

We will separate:
data/raw
data/processed
data/external

We will avoid data leakage when creating ML train/validation/test sets.

### 6. Database Concepts Learned
Primary Key:
- uniquely identifies a row
- example: user_id

Foreign Key:
- connects one table to another
- example: users.department_id -> departments.department_id

One-to-many:
- one department can have many users
- one user can create many tickets
- one incident can affect many tickets

JOIN:
- combines related information from multiple tables.

### 7. Current Database
MySQL 8.0.45 is installed and working.

Database:
enterprise_support

Current tables:
1. departments
2. users
3. services
4. categories
5. tickets
6. incidents
7. resolutions
8. knowledge_articles
9. ai_predictions
10. feedback

Important relationships:

departments
  -> users

departments
  -> services

users
  -> tickets

services
  -> tickets

categories
  -> tickets

services
  -> incidents

incidents
  -> tickets

tickets
  -> resolutions

tickets
  -> ai_predictions

tickets
  -> feedback

categories
  -> knowledge_articles

users
  -> knowledge_articles

### 8. Current Database Schema
departments:
- department_id PK
- department_name
- description

users:
- user_id PK
- name
- email UNIQUE
- department_id FK
- role
- created_at

services:
- service_id PK
- service_name UNIQUE
- description
- owner_department_id FK
- status

categories:
- category_id PK
- category_name UNIQUE
- description

tickets:
- ticket_id PK
- user_id FK
- service_id FK
- category_id FK
- incident_id FK/nullable
- title
- description
- priority
- status
- created_at
- updated_at
- resolved_at

incidents:
- incident_id PK
- service_id FK
- title
- description
- severity
- status
- started_at
- resolved_at

resolutions:
- resolution_id PK
- ticket_id FK
- root_cause
- resolution_text
- resolved_by FK
- created_at

knowledge_articles:
- article_id PK
- title
- content
- category_id FK
- created_by FK
- status
- created_at
- updated_at

ai_predictions:
- prediction_id PK
- ticket_id FK
- model_name
- predicted_category
- predicted_priority
- confidence
- recommended_resolution
- created_at

feedback:
- feedback_id PK
- ticket_id FK
- user_id FK
- rating
- comment
- created_at

### 9. Project Folder Structure
Project location:
Desktop/enterprise-ai-support-platform

Current planned structure:

enterprise-ai-support-platform/
├── backend/
├── database/
│   ├── schema/
│   ├── seed/
│   └── migrations/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── knowledge_base/
├── ml/
│   ├── notebooks/
│   ├── src/
│   ├── models/
│   └── experiments/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── api/
├── docs/
└── scripts/

Tools currently available:
- Python 3.13.5
- Git 2.51.0
- MySQL 8.0.45
- PowerShell
- VS Code

A Python virtual environment named .venv is active.

### 10. Planned Technology Stack
- Python
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- scikit-learn
- sentence-transformers / Transformers
- FAISS
- Ollama for local LLMs
- Git/GitHub
- pytest
- Docker later

Goal: build the project with ₹0 cost using local/open-source tools.

### 11. AI Components Planned
1. Ticket classification
2. Priority prediction
3. Similar-ticket semantic search
4. Knowledge-base retrieval / RAG
5. Resolution recommendation
6. Related-incident detection
7. AI confidence and evaluation
8. Human-in-the-loop workflow
9. Later: controlled AI agent with tools

### 12. Learning Method
We are NOT copy-pasting a finished project.

Process:
Explain concept
  -> understand
  -> user implements
  -> test
  -> review/debug
  -> improve
  -> move to next module

The goal is to be able to explain every important component in an interview.

### 13. Current Progress
Completed:
- project folder created
- Python virtual environment created/activated
- MySQL verified
- Git verified
- enterprise_support database created
- departments table created and populated
- users table created with foreign key
- services table created
- categories table created
- tickets table created
- incidents table created
- tickets -> incidents foreign key added
- resolutions table created
- knowledge_articles table created
- ai_predictions table created
- feedback table created

### 14. Next Step
Do NOT start AI yet.

Next:
1. Verify/insert sample data
2. Learn useful SQL queries with our real project data
3. Create a Python data generator
4. Generate realistic synthetic enterprise tickets
5. Build the data-cleaning pipeline
6. Prepare the ML dataset
7. Then start the AI/ML components

### 15. Key Rule
Build the foundation first:
Database -> Data -> Backend -> ML -> RAG -> LLM -> Agent -> Testing/Deployment

Never jump directly to the LLM.

