import statsmodels.api as sm

from .hypothesis import Hypothesis
from .utilities import prepare_vars, interpret_pval, plot_assump, load_output


class Linearity(Hypothesis):
    """
    Linearity assumption checker using:
    - Ramsey RESET test
    - Residuals vs Fitted plot
    """
    def fit(self):
        self.fitted, self.residuals = prepare_vars(self.model, self.x, self.y)
   
    def test_linearity(self):
        """
        Perform Ramsey RESET test for linearity.
        """
        self.fit()
        reset_model = sm.OLS(self.y,self.x_cons).fit()
        self.result = sm.linear_reset(reset_model, power=3,test_type="fitted")
        result_fstat, result_pval, df1, df2 = self.result
        print("RESET Test for Linearity")
        print(f"F-statistic: {result_fstat:.4f}      p-value: {result_pval:.4f}")
        print("\nInterpretation:\n")
        interpretation = interpret_pval(result_pval, "linearity")
        print("\n" + interpretation)
  
    def plot_linearity(self):
        
        """
        Plot linearity diagnostics.
        """
        
        plot_assump(self.fitted, self.residuals,"linearity")
        print("Interpretation Guide:\n")
        print(load_output("linplot_interpretation_guide.txt"))
   