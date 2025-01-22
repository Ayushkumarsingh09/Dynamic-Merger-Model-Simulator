import pytest
from src.financial_metrics import calculate_synergies, calculate_valuation
from src.scenario_analysis import run_dynamic_scenario
import pandas as pd

# Sample data
companies = pd.DataFrame({
    "Company": ["A", "B", "C"],
    "Revenue": [1000, 1500, 1200],
    "Cost": [800, 1100, 950],
    "Operational Efficiency": [0.85, 0.9, 0.8],
    "Valuation": [1200, 1700, 1400]
})

scenario = {
    "cost_synergy": 0.2,
    "revenue_synergy": 0.3,
    "operational_synergy": 0.15,
    "adjustments": {
        "Revenue": 1.1,
        "Cost": 0.9
    }
}

def test_calculate_synergies():
    synergies = calculate_synergies(companies, scenario)
    assert synergies["Cost Synergy"].iloc[0] > 0
    assert synergies["Revenue Synergy"].iloc[0] > 0
    assert synergies["Operational Synergy"].iloc[0] > 0

def test_calculate_valuation():
    synergies = calculate_synergies(companies, scenario)
    valuation = calculate_valuation(companies, synergies)
    assert valuation["Merged Valuation"].iloc[0] > companies["Valuation"].sum()

def test_run_dynamic_scenario():
    adjusted_companies = run_dynamic_scenario(companies.copy(), scenario)
    assert (adjusted_companies["Revenue"] > companies["Revenue"]).all()
    assert (adjusted_companies["Cost"] < companies["Cost"]).all()
