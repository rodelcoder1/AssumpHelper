# AssumpHelper
# Overview
This Library provides a comprehensive framework for testing the fundamental assumptions of linear regression models. It implements automated diagnostic tools to check whether your regression model meets the statistical requirements necessary for valid inference and prediction.
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
---

## 📌 Purpose

Linear regression relies on several statistical assumptions (linearity, normality, homoscedasticity, independence, etc.). Many students and early researchers struggle with:

* Knowing **which tests** to apply
* Guide for interpreting **statistical results**
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

---

## 📂 Project Structure

```
assumphelper/
├── __init__.py                         # Package initializer and public API
├── check.py                            # Central controller to run assumption checks
├── exceptions.py                       # Custom exceptions and error handling
├── utilities.py                        # Shared helper functions
│
├── normality.py                        # Normality tests and plots
├── normplot_interpretation_guide.txt
│
├── homoscedasticity.py                 # Homoscedasticity tests and plots
├── homplot_interpretation_guide.txt
│
├── linearity.py                        # Linearity diagnostics and plots
├── linplot_interpretation_guide.txt
│
├── independence.py                     # Independence (Durbin–Watson) diagnostics
├── indepplot_interpretation_guide.txt
│
├── hypothesis.py                       # Hypothesis testing utilities
└── test/ # Test scripts and validation files
```

---

## ⚙️ Installation

Install the required packages using pip:

```bash
pip install assumphelper
```

---

## 🚀 Basic Usage

```python
# code here
```
<img width="578" height="455" alt="image" src="https://github.com/user-attachments/assets/718688f0-4694-44e0-95d0-b04e8131a09d" />

---

## 📊 Outputs

AssumpHelper provides:

* Test statistics and their p‑values
* Plain‑language interpretation (Pass / Violation)
* Diagnostic plots (residuals vs fitted, Q‑Q plots, etc.)
* Structured interpretation guides for reports and presentations

---

## 🎓 Intended Users

* Students learning **linear regression**
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

## 📜 License

This project is released under the **MIT License**.

---

## 👤 Author

# Developers
**[Kirsten Roise G. Moog]** 

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


