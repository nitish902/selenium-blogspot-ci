# Selenium UI Automation with CI/CD using GitHub Actions

![CI](https://github.com/YOUR_GITHUB_USERNAME/selenium-blogspot-ci/actions/workflows/selenium.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Selenium](https://img.shields.io/badge/selenium-automation-green)
![CI/CD](https://img.shields.io/badge/CI-CD%20Pipeline-orange)

---

## Project Overview

This project demonstrates **UI automation testing** using Selenium WebDriver with Python and integration with **CI/CD pipeline using GitHub Actions**.

The automation script interacts with web elements such as form fields, dropdowns, alerts, tables, and drag-and-drop components.

Tests run automatically whenever code is pushed to GitHub.

---

## Application Under Test

Practice website:

https://testautomationpractice.blogspot.com/

---

## Features Automated

The automation script covers:

- Form input automation
- Radio button selection
- Checkbox selection
- Dropdown handling
- Date picker input
- Alert handling
- Web table validation
- Drag and drop action
- Headless browser execution (for CI/CD)

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager
- GitHub Actions
- CI/CD

---

## Project Structure

selenium-blogspot-ci
│
├── tests
│ └── test_form.py
│
├── requirements.txt
├── .gitignore
│
└── .github
└── workflows
└── selenium.yml

---

## How Tests Work

The Selenium script:

1. Opens browser in headless mode
2. Navigates to practice website
3. Enters user data
4. Selects dropdown values
5. Handles alerts
6. Validates table data
7. Performs drag and drop
8. Closes browser

Assertions ensure correct functionality of UI elements.

---

## CI/CD Pipeline

GitHub Actions automatically runs test cases on every push.

Workflow steps:

1. Checkout repository
2. Setup Python
3. Install dependencies
4. Run Selenium tests using pytest
5. Display test results

Workflow file location:
.github/workflows/selenium.yml

---

## Run Locally

Install dependencies:
pip install -r requirements.txt

Run tests:
python -m pytest -v

---

## Learning Outcome

- UI automation using Selenium
- Element identification strategies
- Handling alerts and dropdowns
- Web table validation
- Drag and drop automation
- Headless browser testing
- CI/CD pipeline integration
- GitHub Actions workflow setup

---

## Author

Nitish Shukla
