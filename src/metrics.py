"""
Metrics module — compute return-based metrics on price data.

>>> Partner B owns this module. <<<

Same layout as ingest.py: each function has a docstring (the contract) and
TODO comments telling you how to implement it.

You are DONE with this module when this runs green:

    pytest tests/test_metrics.py -v

Do not edit tests/test_metrics.py.

Read  max_drawdown  at the bottom of this file BEFORE you write your own
functions — it is already implemented, and it shows you the pattern to follow.
"""

import numpy as np
import pandas as pd


def daily_returns(prices):
    """
    Compute daily simple returns from a price series.

        r_t = (p_t - p_{t-1}) / p_{t-1}

    The first row has no previous price → it comes out as NaN. Drop it.

    Parameters
    ----------
    prices : pandas.Series
        Price series (any index).

    Returns
    -------
    pandas.Series
        Daily returns. Length is  len(prices) - 1  after dropping the leading NaN.
    """
    # pandas computes (p_t / p_{t-1}) - 1 directly for each row, so the first
    # value is NaN because there is no previous price to compare against.
    returns = prices.pct_change()

    # Drop the leading NaN introduced by the first comparison and return the result.
    return returns.dropna()


def cumulative_returns(returns):
    """
    Compute cumulative returns from a series of daily returns.

        cum_t = (1 + r_1) * (1 + r_2) * ... * (1 + r_t)  -  1

    Interpretation:  cum_t = 0.15  means you're up 15% since day 0.

    Parameters
    ----------
    returns : pandas.Series
        Daily returns.

    Returns
    -------
    pandas.Series
        Cumulative returns.
    """
    # Compound the daily growth factors to obtain cumulative wealth growth and
    # subtract the initial 1.0 baseline to express it as a return.
    return (1 + returns).cumprod() - 1


def annualized_volatility(returns, periods_per_year=252):
    """
    Annualized volatility of a daily returns series.

        vol_annual = std(daily_returns) * sqrt(252)

    252 is the standard trading-day count per year.

    Parameters
    ----------
    returns : pandas.Series
    periods_per_year : int
        Trading periods per year (252 for daily, 12 for monthly, etc.).

    Returns
    -------
    float
    """
    # Daily volatility is the standard deviation of the return series. Scaling it
    # by the square root of the number of periods per year annualizes it.
    daily_vol = returns.std()
    return float(daily_vol * np.sqrt(periods_per_year))


def sharpe_ratio(returns, risk_free_rate=0.02, periods_per_year=252):
    """
    Annualized Sharpe ratio.

        annual_mean_return = returns.mean() * 252
        annual_vol         = returns.std()  * sqrt(252)
        SR                 = (annual_mean_return - risk_free_rate) / annual_vol

    Parameters
    ----------
    returns : pandas.Series
    risk_free_rate : float
        Annual risk-free rate (0.02 = 2% per year).
    periods_per_year : int

    Returns
    -------
    float
    """
    # Annualize the mean return and the volatility, then compute the excess-
    # return Sharpe ratio relative to the chosen risk-free rate.
    annual_mean = returns.mean() * periods_per_year
    annual_vol = annualized_volatility(returns, periods_per_year)
    return float((annual_mean - risk_free_rate) / annual_vol)


def max_drawdown(cum_returns):
    """
    Maximum drawdown — the largest peak-to-trough decline in cumulative wealth.

    Returned as a NEGATIVE number:  -0.15  means a 15% drawdown.

    >>> THIS FUNCTION IS ALREADY WRITTEN. <<<
    Read it. It is exactly the pattern you should use in your own functions:
    small pandas operations, one per line, with a comment saying WHY.

    Parameters
    ----------
    cum_returns : pandas.Series
        Cumulative returns (e.g. output of cumulative_returns()).

    Returns
    -------
    float
        The maximum drawdown, in (-1.0, 0.0].
    """
    # Turn cumulative returns into "wealth" — starting at 1.0
    wealth = 1 + cum_returns

    # Running peak: the highest wealth seen up to each date
    running_peak = wealth.cummax()

    # Drawdown at each date: how far below the running peak we are
    drawdown = (wealth - running_peak) / running_peak

    # Max drawdown is the LOWEST (most negative) point of the drawdown series
    return float(drawdown.min())
