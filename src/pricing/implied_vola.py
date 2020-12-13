import traceback
from scipy.optimize import brentq
from scipy.stats import norm
from math import sqrt, log

n = norm.pdf
N = norm.cdf

MIN_IMPLIED_VOLA = 1e-5
MAX_IMPLIED_VOLA = 2.5
DEFAULT_IMPLIED_VOLA = 0.0


def bs_implied_vola(K: float, T: float, F: float, option_type: str, target_value: float):
    """
    Calculate Black-Scholes implied vola for a given option premium
    ======
    param K: strike
    param T: volatility time in years
    param F: forward at maturity
    param option_type: "Call" or "Put
    param target_value: option premium
    ======
    returns implied vola
    returns zero when an error occurs
    """
    def objective(vol):
        return _bs_price(K, T, F, option_type, vol) - target_value
    try:
        solution = brentq(objective, a=MIN_IMPLIED_VOLA, b=MAX_IMPLIED_VOLA)
    except ValueError as e:
        # print(f"Error when implying vola using brentq with stack {traceback.format_exc()}")
        solution = DEFAULT_IMPLIED_VOLA
    return solution


def _bs_price(K: float, T: float, F: float, option_type: str, sigma: float):
    """
    Calculate Black-Scholes price for a given option
    ======
    param K: strike
    param T: volatility time in years
    param F: forward at maturity
    param option_type: "Call" or "Put
    param sigma: volatility
    ======
    returns BS price
    """
    sigma_sqrt_T = sigma * sqrt(T)
    d1 = (log(F/K)+ 0.5 * sigma_sqrt_T**2)/sigma_sqrt_T
    d2 = d1-sigma_sqrt_T
    if option_type == 'Call':
        price = F*N(d1)-K*N(d2)
    else:
        price = K*N(-d2)-F*N(-d1)
    return price
