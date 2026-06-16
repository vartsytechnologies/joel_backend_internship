# Joel_backend_internship
# Electricity Bill Predictor API

## Internship Project Overview

**Intern:** Joel

The Electricity Bill Predictor API is a backend application built using Django and Django REST Framework (DRF). The project is designed to help users estimate their monthly electricity bills based on appliance power ratings, daily usage patterns, and electricity tariff rates.

Throughout this internship project, you will gain hands-on experience in backend development, API design, database modeling, authentication, testing, documentation, and deployment best practices.

---

# Project Objectives

The system will allow users to:

* Register and manage accounts
* Authenticate securely using token-based authentication
* Add and manage electrical appliances
* Record appliance usage data
* Predict monthly electricity bills
* Access administrative functionality through Django Admin
* Interact with well-documented REST APIs

---

# Expected Deliverables

By the end of the internship, the project should include:

## Core Features

### User Management

* User registration
* User login
* User profile management

### Authentication & Security

* Authentication-protected APIs
* User-specific data access
* Permissions and access control

### Appliance Management

* Add appliances
* Update appliances
* Delete appliances
* View appliance information

### Usage Tracking

* Record appliance usage hours
* View usage history
* Update usage records

### Electricity Bill Prediction

* Calculate estimated monthly consumption
* Calculate estimated monthly electricity cost
* Apply configurable tariff rates
* Generate prediction results through API endpoints

### Administration

* Django Admin dashboard
* User management
* Appliance management
* Usage record management

### Documentation & Testing

* API documentation
* Unit tests
* Integration tests
* README documentation

### Deployment Readiness

* Environment-based settings
* Production-ready configuration
* Secure secret management
* Requirements file

---

# Internship Learning Goals

By the end of the one-month internship, you should be able to:

1. Build a Django project from scratch.
2. Design relational database models.
3. Create REST APIs using Django REST Framework.
4. Use serializers for validation and data transformation.
5. Implement authentication and permissions.
6. Connect users with their related data.
7. Write business logic using services and utility functions.
8. Test APIs effectively.
9. Document APIs professionally.
10. Present and explain a complete backend project.

---

# Git Workflow Guidelines

Joel must create a separate branch for every assigned task.

## Step 1: Pull Latest Changes

```bash
git checkout main
git pull origin main
```

## Step 2: Create a New Branch

Branch naming convention:

```bash
feature/task-name
```

Examples:

```bash
git checkout -b feature/user-registration
git checkout -b feature/appliance-management
git checkout -b feature/bill-prediction
```

## Step 3: Complete the Task

Make code changes and test the implementation.

## Step 4: Commit Changes

```bash
git add .
git commit -m "Implement user registration API"
```

Commit messages should clearly describe the work completed.

## Step 5: Push the Branch

```bash
git push origin feature/user-registration
```

## Step 6: Create a Pull Request (PR)

After pushing:

1. Open the repository on GitHub.
2. Create a Pull Request from the feature branch to `main`.
3. Add a meaningful PR title.
4. Provide a clear description of the changes made.

Example:

**Title**

```text
Implement User Registration API
```

**Description**

```text
Implemented user registration endpoint using Django REST Framework.

Features:
- User serializer
- Registration endpoint
- Validation logic
- Unit tests
```

## Step 7: Assign Reviewer

For every Pull Request:

* Assign the designated supervisor or mentor as reviewer.
* Wait for review comments.
* Address requested changes.
* Push updates to the same branch.
* Obtain approval before merging.

## Important Rules

* Never commit directly to `main`.
* Every task must have its own branch.
* Every branch must have a Pull Request.
* Every Pull Request must have a reviewer assigned.
* Ensure tests pass before requesting review.

---

# Daily Reporting Requirements

You must submit a daily report at the end of each workday using the template below.

## Daily Report Template

**Date:**

**Today's Task:**

**What I completed:**

**What I learned:**

**Challenges I faced:**

**How I solved them:**

**What is left:**

**Questions for my supervisor:**

---

# Final Project Success Criteria

The internship will be considered successful when you can:

* Build and structure a Django backend project independently.
* Create secure REST APIs.
* Implement authentication and permissions.
* Design database relationships correctly.
* Apply business logic for electricity bill prediction.
* Write and execute tests.
* Document APIs professionally.
* Demonstrate proper Git workflow practices.
* Present the completed project confidently.
* Explain architectural and implementation decisions clearly.

---

# Technology Stack

* Python 3.x
* Django
* Django REST Framework
* SQLite/PostgreSQL
* Git & GitHub
* Swagger/OpenAPI (optional)
* Pytest or Django Test Framework

---

# Project Outcome

At the end of this internship, you will have developed a fully functional Electricity Bill Predictor API that demonstrates practical backend engineering skills, industry-standard development workflows, and readiness for larger software development projects.

