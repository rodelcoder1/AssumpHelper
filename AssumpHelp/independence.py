import statsmodels.api as sm

from .hypothesis import Hypothesis
from .utilities import prepare_vars, interpret_dw, plot_assump, load_output


class Independence:  
    """
    Independence checker using:
    - Durbin-Watson statistic
    - Residuals vs Order plot
    """
    def fit(self):
        self.fitted, self.residuals = prepare_vars(self.model, self.x, self.y)    
    
    def test_independence(self):
        """
        Perform Durbin-Watson autocorrelation test.
        """
        self.fit()
        dw_stat = durbin_watson(self.resid)
        self.result = dw_stat
        print("Durbin-Watson Test for Independence")
        print(f"DW-statistic: {dw_stat:.4f}")
        print("\nInterpretation:\n")
        interpretation = interpret_dw(dw_stat)
        print("\n" + interpretation)
   
    def plot_independence(self):
        """
        Plot residuals vs observation order.
        """
        plot_assump(self.fitted,self.residuals, "independence")
        print("\nInterpretation:\n")
        print(load_output("indepplot_interpretation_guide.txt"))