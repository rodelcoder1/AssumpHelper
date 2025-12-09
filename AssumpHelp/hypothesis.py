import numpy as np
import statsmodels.api as sm

class Hypothesis: # #Store the regression model and data
    """
    Initialize base hypothesis class.
    Stores the model and converts x, y to numpy arrays.
    """
    def __init__(self,model,x,y):
        self.model = model
        self.x = np.asarray(x)    # Convert x to numpy array
        self.y = np.asarray(y)    # Convert y to numpy array
        self.x_cons = sm.add_constant(self.x)  # Add constant column for statsmodels OLS