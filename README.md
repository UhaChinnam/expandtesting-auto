# 🧪 Expand Testing - Automated Test Suite

Automated end-to-end test scripts built with **Python**, **Playwright**, and **Pytest** for the [Practice Expand Testing](https://practice.expandtesting.com/) website. Integrated with **GitHub Actions** and **Jenkins** CI/CD pipelines.

---

## 📁 Project Structure

```
expandtesting-auto/
├── .github/
│   └── workflows/
│       └── playwright.yml        # GitHub Actions CI/CD pipeline
├── tests/
│   ├── test_login.py             # Login validation (success & failure)
│   ├── test_inputs.py            # Form input validation
│   ├── test_broken_elements.py   # Broken images & links detection
│   ├── test_ui_assertions.py     # Dynamic UI assertions
│   ├── test_radio_buttons.py     # Radio button interactions
│   ├── test_drag_and_drop.py     # Drag and drop functionality
│   ├── test_file_upload.py       # File upload workflow
│   └── test_add_remove_elements.py # Dynamic add/remove elements
├── reports/
│   └── screenshots/              # Screenshot proofs from test runs
├── Jenkinsfile                   # Jenkins CI/CD pipeline
├── requirements.txt              # Python dependencies
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Tool        | Purpose                        |
|-------------|--------------------------------|
| Python 3.11+| Programming language           |
| Playwright  | Browser automation framework   |
| Pytest      | Test runner and assertions      |
| GitHub Actions | Cloud CI/CD pipeline        |
| Jenkins     | On-premise CI/CD pipeline      |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher installed
- Git installed

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/UhaChinnam/expandtesting-auto.git
   cd expandtesting-auto
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   **Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\activate
   ```

   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install Playwright browsers**
   ```bash
   playwright install
   ```

---

## ▶️ Running Tests

### Run all tests
```bash
pytest
```

### Run a specific test file
```bash
pytest tests/test_login.py
```

### Run a specific test function
```bash
pytest tests/test_login.py::test_login_success
```

### Run with verbose output
```bash
pytest -v
```

### Run and generate JUnit XML report
```bash
pytest --junitxml=reports/results.xml
```

---

## 📋 Test Coverage

| # | Test File                     | Scenario                                    | URL Tested |
|---|-------------------------------|---------------------------------------------|------------|
| 1 | `test_login.py`              | Successful and failed login validation       | `/login`   |
| 2 | `test_inputs.py`             | Form inputs: number, text, password, date    | `/inputs`  |
| 3 | `test_broken_elements.py`    | Detects broken images and HTTP 404 links     | `/broken-images`, `/status-codes` |
| 4 | `test_ui_assertions.py`      | Dynamic controls: checkbox remove, input enable/disable | `/dynamic-controls` |
| 5 | `test_radio_buttons.py`      | Radio button selection and mutual exclusion  | `/radio-buttons` |
| 6 | `test_drag_and_drop.py`      | Drag column A to column B and verify swap    | `/drag-and-drop` |
| 7 | `test_file_upload.py`        | Upload a file and verify confirmation        | `/upload`  |
| 8 | `test_add_remove_elements.py`| Dynamically add and remove DOM elements      | `/add-remove-elements` |

---

## 📸 Screenshot Proofs

Every test automatically captures a screenshot at the end of execution and saves it to `reports/screenshots/`. This provides visual evidence that each test scenario completed successfully.

---

## ⚙️ CI/CD Integration

### GitHub Actions
Tests run automatically on every `push` or `pull request` to the `main` branch via `.github/workflows/playwright.yml`.

### Jenkins
A `Jenkinsfile` is included for on-premise Jenkins pipelines. To set it up:
1. Create a new **Pipeline** job in Jenkins
2. Set **Definition** to *Pipeline script from SCM*
3. Set **Repository URL** to `https://github.com/UhaChinnam/expandtesting-auto.git`
4. Set **Branch Specifier** to `*/main`
5. Save and click **Build Now**

---

## 👤 Author

**Uha Chinnam** — [GitHub](https://github.com/UhaChinnam)

---

## 📄 License

This project is for educational and practice purposes.
