import numpy as np
from scipy.optimize import curve_fit

# Provided data (replace with your actual data)
deltaF_over_delta_data = np.array([0.439424711,
0.615142795,
0.67371549,
0.73030267,
0.878223543,
1.038057507,
1.115492595,
1.29518171,
1.626762728,
1.731101546,
])

physiological_response = np.array([1.076414424,
1.588873984,
1.759693837,
1.930513691,
2.272153397,
2.613793103,
2.784612957,
3.126252663,
3.638712223,
3.801767537,
])

# Define a function to fit to your data
def model_function(deltaF_over_delta, a, b, c):
    # Example of a quadratic model (replace with appropriate model)
    return a * deltaF_over_delta**2 + b * deltaF_over_delta + c

# Fit the model to your data
popt, _ = curve_fit(model_function, deltaF_over_delta_data, physiological_response)

# Function to infer light intensity from ΔF/F0 peak value
def infer_light_intensity(deltaF_over_delta, popt):
    a, b, c = popt
    # Inverse function based on your fitted model
    # Example: Solve quadratic equation for light_intensity
    light_intensity = np.roots([a, b, c - deltaF_over_delta])[0]
    return light_intensity

# Example ΔF/F0 peak value from your experimental data
measured_deltaF_over_delta = 1.0  # Replace with your actual measured deltaF over delta value

# Infer light intensity
inferred_light_intensity = infer_light_intensity(measured_deltaF_over_delta, popt)

# Output the inferred light intensity
print(f"Measured ΔF/F0 Peak: {measured_deltaF_over_delta}")
print(f"Inferred Light Intensity: {inferred_light_intensity:.2f} mW/mm²")

# Optionally, you can return the light intensity data used in the model fitting
# Replace this with your actual light intensity data if available
light_intensity_data = np.linspace(0.1, 10.0, 100)  # Example: linearly spaced values for demonstration

# Print or use light_intensity_data as needed
print("Light Intensity Data:")
print(light_intensity_data)
