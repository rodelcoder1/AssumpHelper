import statsmodels.api as sm

from .hypothesis import Hypothesis
from .utilities import prepare_vars, interpret_pval, plot_assump, load_output

class Homoscedasticity(Hypothesis):
    """
    Homoscedasticity checker using:
    - Breusch-Pagan test
    - Scale-Location plot
    """
    def fit(self):
        self.fitted, self.residuals = prepare_vars(self.model, self.x, self.y)
   
    def test_homoscedasticity(self):
        """
        Perform Breusch-Pagan test.
        """
        self.fit()
        bp_test = het_breuschpagan(self.resid, self.x)
        bp_stat, bp_pval, _, _ = bp_test
        self.result = bp_pval
        print("Breusch-Pagan Test for Homoscedasticity")
        print(f"BP-statistic: {bp_stat:.4f}      p-value: {bp_pval:.4f}")
        print("\nInterpretation:\n")
        interpretation = interpret_pval(result_pval, "homoscedasticity")
        print("\n" + interpretation)

    def plot_homoscedasticity(self):
        """
        Plot homoscedasticity diagnostics.
        """
        plot_assump(self.fitted, self.residuals, "homoscedasticity")
        print("Interpretation Guide:\n")
        print(load_output("homplot_interpretation_guide.txt"))

