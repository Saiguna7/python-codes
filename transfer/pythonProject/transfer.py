import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the numerator and denominator coefficients
numerator_coeffs = [2, 0, 4]  # Coefficients for s^0.63 and constant term
denominator_coeffs = [2, 3.8, 2.6, 2.5, 1.5]  # Coefficients for s^3.501, s^2.42, s^1.798, s^1.31, and constant term

# Create the transfer function G(s)
sys = signal.TransferFunction(numerator_coeffs, denominator_coeffs)
print(sys)