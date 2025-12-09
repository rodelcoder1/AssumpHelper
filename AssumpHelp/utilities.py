"""
Utility Functions for AssumpHelp
"""
import numpy as np
import scipy.stats as sp
from scipy.stats import f
import statsmodels.api as sm
import matplotlib.pyplot as plt
import sklearn as sk
import os

def prepare_vars(model, x, y):
    """
    Prepares fitted and residual values
    """ 
    
    y_predictions = model.predict(x) #fitted
    residuals = y - y_predictions
    
    return y_predictions, residuals

def interpret_pval(pval, assump):
    if pval > 0.05:
        return f"If alpha = 0.05 and p-value > 0.05: Assumption of {assump.capitalize()} is NOT VIOLATED.\n"
    else:
        return f"If alpha = 0.05 and p-value > 0.05: Assumption of {assump.capitalize()} is VIOLATED.\n"

def plot_assump(fitted, residuals,assumption):

    # Linearity: Residuals vs Fitted
    if assumption.lower() == "linearity":
        plt.figure(figsize=(8,6))
        plt.scatter(fitted, residuals, alpha=0.5)
        plt.xlabel("Fitted Values")
        plt.ylabel("Residuals")
        plt.title("Residuals vs Fitted Plot")
        plt.show()

    # Homoscedasticity: Scale-Location Plot
    elif assumption.lower() == "homoscedasticity":
        std_resid = residuals / np.std(residuals)
        plt.figure(figsize=(8,6))
        plt.scatter(fitted, np.sqrt(np.abs(std_resid)), alpha=0.5)
        plt.xlabel("Fitted Values")
        plt.ylabel("Sqrt(|Standardized Residuals|)")
        plt.title("Scale-Location Plot (Homoscedasticity Check)")
        plt.show()

    # Normality: Q-Q Plot
    elif assumption.lower() == "normality":
        sm.qqplot(residuals, line='s')
        plt.title("Q-Q Plot")
        plt.show()

    # Independence: 
    elif assumption.lower() == "independence":
        order = np.arange(1, len(residuals) + 1)
        plt.figure(figsize=(8, 6))
        plt.scatter(order, residuals, alpha=0.5)
        plt.xlabel("Observation Order")
        plt.ylabel("Residuals")
        plt.title("Residuals vs Order Plot")
        plt.show()

    else:
        raise ValueError("Invalid Assumption. Please double-check spelling.")

def interpret_dw(dw_stat):
    """
    For Durbin-Watson Stat Comparitson
    """
    if 1.5 <= dw_stat <= 2.5:
        return("DW statistic close to 2 indicates no autocorrelation assumption NOT VIOLATED.")
    elif 1.5 > dw_stat:
        return("DW statistic significantly less than 2 indicates positive autocorrelation VIOLATED.")
    elif dw_stat > 2.5:
        return("DW statistic significantly greater than 2 indicates negative autocorrelation VIOLATED.")


def load_output(path):
    with open(path, "r") as f:
        return f.read()