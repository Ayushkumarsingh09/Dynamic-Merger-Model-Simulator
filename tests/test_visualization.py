import pytest
from src.visualization import plot_synergy_chart, plot_valuation_chart
import pandas as pd
import os

def test_plot_synergy_chart():
    synergies = pd.DataFrame({
        "Cost Synergy": [500],
        "Revenue Synergy": [300],
        "Operational Synergy": [200]
    })
    filepath = "test_synergy_chart.png"
    plot_synergy_chart(synergies, filepath)
    assert os.path.exists(filepath)
    os.remove(filepath)

def test_plot_valuation_chart():
    valuation = pd.DataFrame({"Merged Valuation": [4500]})
    filepath = "test_valuation_chart.png"
    plot_valuation_chart(valuation, filepath)
    assert os.path.exists(filepath)
    os.remove(filepath)
