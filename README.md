# Data Integrity & Backend Persistence Testing - Python, SQLite & Pytest

## 📌 Project Overview
This project contains an automated data integrity and backend persistence test suite built using **Python**, **SQLite**, and **Pytest**. It validates that business data processed via APIs or interfaces is accurately stored, retrieved, and updated in the database without corruption or loss.

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Testing Framework:** Pytest
* **Database Engine:** SQLite (Relational Database)
* **IDE:** Visual Studio Code (VS Code)

## 🧪 Automated Test Scenarios (`test_db_integrity.py`)
1. **`test_user_persistence_in_database` (Create & Read Validation):** Simulates a user creation payload, inserts the record into the database, executes an automated `SELECT` query, and asserts that the stored name and job title match perfectly.
2. **`test_user_update_persistence_in_database` (Update & State Validation):** Inserts an initial record, simulates a data update (similar to a `PUT` request), executes a database modification query, and asserts that the backend data state correctly reflects the updated values.

## 🚀 How to Run This Project Locally
1. Clone this repository:
   ```bash
   git clone [https://github.com/Ivan60524/data-integrity-testing.git](https://github.com/Ivan60524/data-integrity-testing.git)
