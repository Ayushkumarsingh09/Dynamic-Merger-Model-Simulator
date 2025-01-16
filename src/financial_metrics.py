import pandas as pd

def calculate_synergies(companies, scenario):
    """
    Calculate synergies for the merger.
    """
    cost_synergy = scenario["cost_synergy"] * companies["Cost"].sum()
    revenue_synergy = scenario["revenue_synergy"] * companies["Revenue"].sum()
    operational_synergy = scenario["operational_synergy"] * companies["Operational Efficiency"].mean()

    synergies = {
        "Cost Synergy": cost_synergy,
        "Revenue Synergy": revenue_synergy,
        "Operational Synergy": operational_synergy
    }
    return pd.DataFrame([synergies])

def calculate_valuation(companies, synergies):
    """
    Calculate valuation post-merger.
    """
    base_valuation = companies["Valuation"].sum()
    total_synergy = synergies.sum(axis=1).iloc[0]
    merged_valuation = base_valuation + total_synergy

    return pd.DataFrame({"Merged Valuation": [merged_valuation]})
