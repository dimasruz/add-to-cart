# 🛒 Add to Cart – Automated Test Suite (Selenium + Pytest)

Automated UI test suite for e-commerce "Add to Cart" functionality, built with
**Python**, **Selenium WebDriver**, and **Pytest**, following the **Page Object Model (POM)**
design pattern.

Target application under test: [saucedemo.com](https://www.saucedemo.com) — a demo
e-commerce site built by Sauce Labs specifically for test automation practice.

---

## 📌 What This Project Demonstrates

- Page Object Model (POM) architecture for maintainable test code
- Pytest fixtures for browser setup/teardown
- Data-driven testing with `@pytest.mark.parametrize`
- Explicit waits (no `time.sleep`)
- HTML test reports
- Clean separation of test logic vs. page interaction logic
- Test markers for smoke vs. regression runs

---

## 🗂️ Project Structure

```
add-to-cart-testing/
├── README.md
├── requirements.txt
├── pytest.ini
├── conftest.py                 # Shared fixtures (driver setup/teardown)
├── pages/
│   ├── __init__.py
│   ├── base_page.py             # Common reusable Selenium actions
│   ├── login_page.py            # Login page locators + actions
│   ├── inventory_page.py        # Product listing / Add to Cart actions
│   └── cart_page.py             # Cart page locators + actions
├── tests/
│   ├── __init__.py
│   └── test_add_to_cart.py      # All Add to Cart test cases
├── utils/
│   └── driver_factory.py        # WebDriver instantiation logic
└── reports/                     # Generated HTML test reports (git-ignored)
```

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/add-to-cart-testing.git
cd add-to-cart-testing
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> No need to manually download ChromeDriver — `webdriver-manager` handles it automatically.

---

## ▶️ Running the Tests

Run the full suite:
```bash
pytest
```

Run only smoke tests:
```bash
pytest -m smoke
```

Run with an HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

Run headless (CI-friendly):
```bash
pytest --headless
```

---

## 🧪 Test Cases Covered

| ID | Test Case | Marker |
|----|-----------|--------|
| TC01 | Add a single product to the cart | smoke |
| TC02 | Add multiple products to the cart | regression |
| TC03 | Cart badge count updates correctly | smoke |
| TC04 | "Add to Cart" button changes to "Remove" after adding | regression |
| TC05 | Remove a product from the cart | regression |
| TC06 | Product added appears with correct name/price in cart | regression |
| TC07 | Add to cart for all products (data-driven/parametrized) | regression |

---

## 🔧 Tech Stack

- Python 3.10+
- Selenium WebDriver
- Pytest
- pytest-html (reporting)
- webdriver-manager (auto driver management)

---

## 🚀 Next Steps (Ideas for Extending This Project)

- Add to `.github/workflows/tests.yml` to run tests on every push (CI/CD with GitHub Actions)
- Add checkout flow tests
- Add cross-browser testing (Chrome/Firefox) via parametrized fixtures
- Add Allure reporting instead of pytest-html
- Convert to API testing layer using `requests` for backend cart validation
