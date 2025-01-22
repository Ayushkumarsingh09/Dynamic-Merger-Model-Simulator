import pytest
from src.scenario_analysis import run_dynamic_scenario
import pandas as pd

# Sample data
companies = pd.DataFrame({
    "Company": ["A", "B"],
    "Revenue": [1000, 1500],
    "Cost": [800, 1100],
    "Operational Efficiency": [0.85, 0.9],
    "Valuation": [1200, 1700]
})

scenario = {
    "adjustments": {
        "Revenue": 1.1,
        "Cost": 0.9
    }
}

def test_run_dynamic_scenario():
    adjusted_companies = run_dynamic_scenario(companies.copy(), scenario)
    assert (adjusted_companies["Revenue"] > companies["Revenue"]).all()
    assert (adjusted_companies["Cost"] < companies["Cost"]).all()
