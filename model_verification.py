import numpy as np

# Constants
alpha = 5.0
a0 = 1.2e-10  # m/s^2
k = 1.3
Tc = 2.725    # Kelvin

def calc_susceptibility(T, a_proper):
    # The Modified Ginzburg-Landau Equation
    if T >= Tc:
        return 0.0
    
    numerator = alpha * (1 - (T / Tc)**2)
    denominator = 1 + (a_proper / a0)**k
    return numerator / denominator

# Scenarios
scenarios = {
    "Earth Lab": {"a": 9.8, "T": 10e-3}, # Cryogenic on Earth
    "Satellite (Warm)": {"a": 10e-6, "T": 300}, # MICROSCOPE
    "ISS (Cold BEC)": {"a": 10e-6, "T": 10e-9}, # Fuentes
    "Halo": {"a": 10e-11, "T": 2.7},
}

print(f"{'Scenario':<20} | {'Signal (Delta a/a)':<20}")
print("-" * 45)

for name, params in scenarios.items():
    chi = calc_susceptibility(params["T"], params["a"])
    print(f"{name:<20} | {chi:.2e}")
