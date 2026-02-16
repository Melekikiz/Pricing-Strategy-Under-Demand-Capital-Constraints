import numpy as np
import pandas as pd

def run_optimization(elasticity_matrix):
    """Finds the optimal price increase for max revenue."""
    price_steps = np.linspace(0, 0.30, 31)
    results = []
    for category in elasticity_matrix.index:
        for region in elasticity_matrix.columns:
            e = elasticity_matrix.loc[category, region]
            revenue_changes = [(1+p) * (1 + (e*p)) - 1 for p in price_steps]
            max_idx = np.argmax(revenue_changes)
            results.append({
                'Category': category, 'Region': region, 'Elasticity': e,
                'Optimal_Increase_%': round(price_steps[max_idx] * 100, 1),
                'Max_Revenue_Gain_%': round(revenue_changes[max_idx] * 100, 2)
            })
    return pd.DataFrame(results)