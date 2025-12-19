# AssumHelper
# Overview
This Library provides a comprehensive framework for testing the fundamental assumptions of linear regression models. It implements automated diagnostic tools to check whether your regression model meets the statistical requirements necessary for valid inference and prediction.
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
---

## 📌 Purpose

Linear regression relies on several statistical assumptions (linearity, normality, homoscedasticity, independence, etc.). Many students and early researchers struggle with:

* Knowing **which tests** to apply
* Interpreting **statistical results** correctly
* Presenting **clear diagnostics and plots**

**AssumpHelper** addresses these challenges by offering a structured, reusable workflow that checks regression assumptions and explains the results in a clear and organized way.

---

## ✨ Features

* Automated **linear regression assumption testing**
* Built‑in **statistical tests** with interpretation guides
* **Visualization support** for diagnostics
* Beginner‑friendly design with clear outputs
* Modular structure for easy extension
* Suitable for academic, research, and learning purposes

### Supported Assumption Checks

* **Linearity** (e.g., Ramsey RESET Test)
* **Homoscedasticity** (Breusch–Pagan Test)
* **Normality of Residuals** (Shapiro–Wilk Test)
* **Independence of Errors** (Durbin–Watson Test)
* **Model Summary & Diagnostics**

---

## 📂 Project Structure

```
AssumpHelper/
├── assumphelper/          # Core library modules
│   ├── __init__.py
│   ├── linear_model.py
│   ├── assumption_tests.py
│   ├── diagnostics.py
│   └── visualizations.py
├── examples/              # Usage examples and demos
├── tests/                 # Unit tests
├── DOCS/                  # Documentation files
├── requirements.txt       # Dependencies
├── setup.py               # Package setup
└── README.md & License            # Project documentation
```

---

## ⚙️ Installation

Install the required packages using pip:

```bash
pip install AssumpHelper
```

---

## 🚀 Basic Usage

```python
from assumphelper.linear_model import LinearModel

# X = independent variables
# y = dependent variable
model = LinearModel(X, y)

# Fit linear regression model
model.fit()

# Automatically checks:
# - Linearity
# - Normality of residuals
# - Homoscedasticity
# - Independence of errors
model.check_assumptions()

# Displays statistical tests, p-values, interpretations, and plots
model.summary()

```

The output includes statistical test results, interpretations, and diagnostic plots.

---

## 📊 Outputs

AssumpHelper provides:

* Test statistics and p‑values
* Plain‑language interpretation (Pass / Violation)
* Diagnostic plots (residuals, Q‑Q plots, etc.)
* Structured summaries for reports and presentations

---

## 🎓 Intended Users

* Students learning **linear regression**
* Researchers conducting **quantitative analysis**
* Educators teaching **statistics and econometrics**
* Beginners who want clarity without losing rigor

---

## 🧠 Inspiration

This project is inspired by common regression workflows in:

* Statistics & Econometrics courses
* Python libraries such as `statsmodels` and `scikit‑learn`
* The need for **simpler interpretation** of assumption tests

---

## 🔧 Requirements

* Python **3.7+**
* numpy
* pandas
* scipy
* statsmodels
* matplotlib
* seaborn

(See `requirements.txt` for the full list.)

---

## 📈 Future Improvements

* More regression models (e.g., logistic regression)
* Exportable reports (PDF / HTML)
* GUI or dashboard support
* Expanded visualization options

---

## 📜 License

This project is released under the **MIT License**.

---

## 👤 Author

# Developers
**[Kirstine Roise G. Moog]** 

Our distinguish Leader &  Inceptionist & Structural Design 

**[Rodel P. Badilla]**

Our Assistant Leader
# Leaders Roles
- Designed clean separation of concerns  
- Implementing codes engine  
- Created visualization tools
- Enhanced plotting capabilities 

**[Hannah Dennisse Y. Aque]**

**[James Walte C. Prollo]**

**[Zell Caamino]**

# Roles

Back (support)
- Built comprehensive test suite  
- Wrote user documentation.
- Quality assurance

Note: This diagnostic framework helps ensure the validity of your regression analysis by systematically checking fundamental statistical assumptions. Regular use of these tools will improve the reliability and interpretability of your regression models.


