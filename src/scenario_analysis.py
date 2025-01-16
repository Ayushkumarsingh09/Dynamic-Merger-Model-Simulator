import pandas as pd

def run_dynamic_scenario(companies, scenario):
    """
    Adjust financials dynamically based on the scenario.
    """
    for col, factor in scenario["adjustments"].items():
        companies[col] *= factor
    return companies
