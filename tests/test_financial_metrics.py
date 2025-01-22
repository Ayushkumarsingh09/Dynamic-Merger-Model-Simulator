import pytest
from src.financial_metrics import calculate_synergies
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
    "cost_synergy": 0.1,
    "revenue_synergy": 0.2,
    "operational_synergy": 0.1
}

def test_calculate_synergies():
    synergies = calculate_synergies(companies, scenario)
    assert synergies["Cost Synergy"].iloc[0] > 0
    assert synergies["Revenue Synergy"].iloc[0] > 0
    assert synergies["Operational Synergy"].iloc[0] > 0
