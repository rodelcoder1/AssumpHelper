import statsmodels.api as sm

from .hypothesis import Hypothesis
from .utilities import prepare_vars, interpret_pval, plot_assump, load_output

class Normality(Hypothesis): 
    """
    Normality checker using:
    - Shapiro-Wilk test
    - Q-Q plot
    """
    def fit(self):
        self.fitted, self.residuals = prepare_vars(self.model, self.x, self.y)
   
    def test_normality(self):
        """
        Perform Shapiro-Wilk test.
        """
        self.fit()
        shapiro_stat, shapiro_pval = sp.shapiro(self.residuals)
        self.result = shapiro_pval
        print("Shapiro-Wilk Test for Normality")
        print(f"W-statistic: {shapiro_stat:.4f}      p-value: {shapiro_pval:.4f}")
        print("\nInterpretation:\n")
        interpretation = interpret_pval(result_pval, "normality")
        print("\n" + interpretation)
        
    
    def plot_normality(self):
        """
        Plot Q-Q plot.
        """
        plot_assump(self.fitted, self.residuals, "normality")
        print("Interpretation Guide:\n")
        print(load_output("normplot_interpretation_guide.txt"))
