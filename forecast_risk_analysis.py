import pandas as pd

def calculate_financial_risks(categories_data, unit_cost=50, avg_price=120):
    """Calculates financial loss risk based on forecast bias."""
    impacts = []
    for region, cat, forecast, strategy, elasticity in categories_data:
        uncertainty = 0.05 + (abs(elasticity) * 0.15)
        err_units = forecast * uncertainty
        bias = "Over-Forecast" if elasticity < -1 else "Under-Forecast"
        loss = err_units * unit_cost if bias == "Over-Forecast" else err_units * (avg_price - unit_cost)
        
        impacts.append({
            'Category': f"{region}-{cat}",
            'Uncertainty': f"±{round(uncertainty*100, 1)}%",
            'Financial_Risk_Value': f"${int(loss):,}",
            'Bias_Trend': bias
        })
    return pd.DataFrame(impacts)