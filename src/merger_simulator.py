import pandas as pd
from src.financial_metrics import calculate_synergies, calculate_valuation
from src.scenario_analysis import run_dynamic_scenario
from src.visualization import plot_synergy_chart, plot_valuation_chart

def main():
    # Load data
    companies = pd.read_csv("data/companies.csv")
    scenarios = pd.read_json("data/scenarios.json")

    # Iterate over scenarios
    for scenario in scenarios["scenarios"]:
        print(f"Running scenario: {scenario['name']}")
        
        # Simulate merger
        synergies = calculate_synergies(companies, scenario)
        merged_valuation = calculate_valuation(companies, synergies)

        # Save results
        synergies.to_csv("data/outputs/synergy_report.csv", index=False)
        merged_valuation.to_csv("data/outputs/merged_company.csv", index=False)

        # Visualize results
        plot_synergy_chart(synergies, f"data/outputs/charts/synergy_chart_{scenario['name']}.png")
        plot_valuation_chart(merged_valuation, f"data/outputs/charts/valuation_chart_{scenario['name']}.png")

if __name__ == "__main__":
    main()
