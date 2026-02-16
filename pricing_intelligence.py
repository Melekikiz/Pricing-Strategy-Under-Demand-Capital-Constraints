import pandas as pd
import numpy as np
import statsmodels.api as sm

def calculate_elasticity_matrix(df):
    """Calculates price elasticity for each Category-Region pair."""
    matrix_results = []
    for region in df['region'].unique():
        for category in df['category'].unique():
            subset = df[(df['region'] == region) & 
                        (df['category'] == category) & 
                        (df['has_promotion'] == 0)].copy()
            if len(subset) > 5:
                X = sm.add_constant(np.log(subset['weekly_avg_price']))
                y = np.log(subset['total_qty'])
                model = sm.OLS(y, X).fit()
                matrix_results.append({
                    'Region': region, 'Category': category,
                    'Elasticity': round(model.params.iloc[1], 3)
                })
    return pd.DataFrame(matrix_results).pivot(index='Category', columns='Region', values='Elasticity')
