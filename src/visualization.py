import matplotlib.pyplot as plt

def plot_synergy_chart(synergies, filepath):
    """
    Plot synergy contributions.
    """
    synergies.plot(kind="bar", figsize=(10, 6))
    plt.title("Synergy Contributions")
    plt.xlabel("Type")
    plt.ylabel("Amount")
    plt.grid(True)
    plt.savefig(filepath)

def plot_valuation_chart(valuation, filepath):
    """
    Plot valuation post-merger.
    """
    valuation.plot(kind="bar", figsize=(10, 6))
    plt.title("Merged Valuation")
    plt.xlabel("Metric")
    plt.ylabel("Value")
    plt.grid(True)
    plt.savefig(filepath)
