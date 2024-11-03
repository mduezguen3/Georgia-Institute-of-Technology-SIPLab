import numpy as np
from scipy.optimize import curve_fit
from attrs import define, field
import matplotlib.pyplot as plt

@define(eq=False)
class ExcitationModel:
    """Base class for excitation models."""
    pass

@define(eq=False)
class LightExcitation(ExcitationModel):
    """Models light-dependent excitation using a Hill function"""
    
    A: float = field(init=False)
    Kd: float = field(init=False)
    n: float = field(init=False)
    baseline: float = field(default=0.0, init=False)  # Adding baseline field with default value
    
    def hill_function(self, Irr_pre, A, Kd, n, baseline):
        return baseline + A * (Irr_pre ** n) / ((Kd ** n) + (Irr_pre ** n))

    def fit_excitation(self, light_intensities, responses):
        # Fit Hill function to the light intensity vs response data
        popt, _ = curve_fit(self.hill_function, light_intensities, responses, maxfev=10000, p0=[1.0, 1.0, 1.0, 0.0])
        self.A, self.Kd, self.n, self.baseline = popt

    def __call__(self, Irr_pre):
        return self.hill_function(Irr_pre, self.A, self.Kd, self.n, self.baseline)

@define(eq=False)
class GECI:
    """Base class for GECIs"""
    light_dependent: bool = field(default=False)

@define(eq=False)
class LightDependent:
    """Base class for light-dependent behavior"""
    pass

@define(eq=False)
class LightDependentGECI(GECI, LightDependent):
    """Light-dependent calcium indicator"""
    exc_model: LightExcitation = field(kw_only=True)

def gcamp6f(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def gcamp6s(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def gcamp3(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def ogb1(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def gcamp6rs09(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def gcamp6rs06(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def jgcamp7f(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def jgcamp7s(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def jgcamp7b(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def jgcamp7c(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def jgcamp8f(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def jgcamp8m(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def jgcamp8s(light_dependent=False, exc_model=None):
    return LightDependentGECI(light_dependent=light_dependent, exc_model=exc_model if light_dependent else None)

def fit_light_dependence_curves(indicators, light_intensities, responses_dict):
    """
    Fit light dependence curves for multiple indicators.

    Parameters
    ----------
    indicators : list
        List of indicator functions (e.g., [gcamp6f, gcamp6s, gcamp3, ...]).
    light_intensities : np.ndarray
        Array of light intensity values.
    responses_dict : dict
        Dictionary where keys are indicator names and values are arrays of responses to light intensities.
    """
    fitted_indicators = {}
    plt.figure(figsize=(14, 10))
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(indicators)))  # Generate colors for each curve
    
    for i, indicator_fn in enumerate(indicators):
        indicator_name = indicator_fn.__name__
        if indicator_name in responses_dict:
            responses = responses_dict[indicator_name]
            exc_model = LightExcitation()
            geci_model = indicator_fn(light_dependent=True, exc_model=exc_model)
            geci_model.exc_model.fit_excitation(light_intensities, responses)
            fitted_indicators[indicator_name] = geci_model
            
            # Plotting the results
            plt.subplot(4, 4, i + 1)
            plt.scatter(light_intensities, responses, label='Data', color='brown')
            fitted_responses = geci_model.exc_model(light_intensities)
            plt.plot(light_intensities, fitted_responses, label='Fitted curve', color=colors[i])
            plt.title(indicator_name)
            plt.xlabel('Light Intensity (mW/mm^2)')
            plt.ylabel('Response')
            plt.legend()
        else:
            print(f"No response data for {indicator_name}")
    
    plt.tight_layout()
    plt.show()
    return fitted_indicators

# Example usage
indicators = [gcamp6f, gcamp6s, gcamp3, ogb1, gcamp6rs09, gcamp6rs06, jgcamp7f, jgcamp7s, jgcamp7b, jgcamp7c, jgcamp8f, jgcamp8m, jgcamp8s]
light_intensities = np.array([0.16452872, 0.18718561, 0.26935816, 0.26997261, 0.74285427, 1.42167679,
 1.49459703, 2.30448815, 3.14298585, 3.4631732])  # Include 0.0 for x=0
responses_dict = {
    "jgcamp8f": np.array([1.076414424,
1.588873984,
1.759693837,
1.930513691,
2.272153397,
2.613793103,
2.784612957,
3.126252663,
3.638712223,
3.801767537])
}

fitted_indicators = fit_light_dependence_curves(indicators, light_intensities, responses_dict)
