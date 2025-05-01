# SauceDemo Web Automation

This project automates two scenarios on the [SauceDemo](https://www.saucedemo.com) e-commerce website using Selenium and Pytest in Python.

---

## Automated Scenarios

1. Login with valid credentials.
   Tests that a user can successfully log in using valid username and password

2. Sort products by price (Low to High).
   Ensures that the product sorting feature correctly arranges items in ascending order of price

---


## Tools & Technologies 

| Type       | Tool / Language               |
|------------|-------------------------------|
| Language   | Python 3.10                   |
| Framework  | Selenium WebDriver            |
| Test Runner| Pytest                        |
| Structure  | Page Object Model (POM)       |
---


## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/walidaud/yassir_assessment_part2.git
```
---


### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
cd yassir_assessment_part2
```
---


### Install dependencies

```bash
pip install -r requirements.txt
```
---


### Run Tests

```bash
pytest
```



