import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from itertools import product

# Data for ChroME2f (provided)
irradiance_1p = np.abs(np.array([-0.133811937, -0.285329021, -0.345634606, -0.161432626, -0.381335054]))
current_1p = np.abs(np.array([0.01831372, 0.469307388, 0.972508906, 1.002046634, 0.750938527]))

power_2p = np.abs(np.array([-0.039671018, -0.062386379, -0.095235842, -0.080626192, -0.040504112]))
current_2p = np.abs(np.array([0.017954882, 0.225418517, 0.492782039, 0.759697007, 0.998009278]))

# Calculate 2P irradiance assuming a spot diameter of 0.1 mm
spot_diameter_mm = 0.1
spot_area = np.pi * (spot_diameter_mm / 2) ** 2
irradiance_2p = np.abs(power_2p / spot_area)

# Define transformation functions
def identity(x):
    return x

def square(x):
    return x ** 2

def sqrt(x):
    return np.sqrt(x)

def log(x):
    return np.log(x)

fns_and_invs = [
    (identity, identity),
    (np.log, np.exp),
    (np.sqrt, square),
    (square, np.sqrt),
]

def f_lin(x, m):
    return x * m

def opt(irr, I):
    opt = curve_fit(f_lin, irr, I, [1], full_output=True)
    m = opt[0][0]
    percent_resid2 = np.sum(opt[2]["fvec"] ** 2) / np.sum(I ** 2)
    return m, percent_resid2

best_res = np.inf
best_r2 = -np.inf
for (f_irr, f_irr_inv), (f_I, f_I_inv) in product(fns_and_invs, fns_and_invs):
    try:
        irr_1p_transformed = f_irr(irradiance_1p)
        irr_2p_transformed = f_irr(irradiance_2p)
        I_1p_transformed = f_I(current_1p)
        I_2p_transformed = f_I(current_2p)

        m1p, percent_resid2_1p = opt(irr_1p_transformed, I_1p_transformed)
        m2p, percent_resid2_2p = opt(irr_2p_transformed, I_2p_transformed)
        tot_res = np.mean([percent_resid2_1p, percent_resid2_2p])

        I_hat_1p = f_I_inv(m1p * irr_1p_transformed)
        r2_1p = 1 - np.sum((I_hat_1p - current_1p) ** 2) / np.sum((current_1p - np.mean(current_1p)) ** 2)

        I_hat_2p = f_I_inv(m2p * irr_2p_transformed)
        r2_2p = 1 - np.sum((I_hat_2p - current_2p) ** 2) / np.sum((current_2p - np.mean(current_2p)) ** 2)

        mean_r2 = np.mean([r2_1p, r2_2p])

        if mean_r2 > best_r2:
            best_r2 = mean_r2
            best_f_irr = f_irr
            best_f_I = f_I
            best_I_hat_1p = I_hat_1p
            best_I_hat_2p = I_hat_2p

    except Exception as e:
        print(f"An error occurred: {e}")

print(f"best_f_irr: {best_f_irr.__name__}")
print(f"best_f_I: {best_f_I.__name__}")
print(f"best mean r2: {best_r2}")

fig, ax = plt.subplots()
ax.semilogx(best_f_irr(irradiance_1p), best_f_I(current_1p), 'o', c="xkcd:carmine", label="1P data")
ax.plot(best_f_irr(irradiance_1p), best_I_hat_1p, 'xkcd:carmine', linestyle="--", label="1P model")
ax.plot(best_f_irr(irradiance_2p), best_f_I(current_2p), 'o', c="k", label="2P data")
ax.plot(best_f_irr(irradiance_2p), best_I_hat_2p, 'k', linestyle="--", label="2P model")
ax.set(
    xlabel="Irradiance (mW/mm^2)",
    ylabel="Photocurrent (nA)",
    title="ChroME2f Power Sensitivity"
)
ax.legend()
plt.grid(True)
plt.show()
