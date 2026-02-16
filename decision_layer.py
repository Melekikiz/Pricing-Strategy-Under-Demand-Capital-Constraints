import pandas as pd 

def generate_inventory_decisions(categories_data, avg_price=120):
    """Generates final inventory and revenue recommendations."""
    decisions = []
    for region, cat, forecast, strategy, elasticity in categories_data:
        bias = "Under-Forecast" if elasticity > -0.5 else "Over-Forecast"
        stock_rec = int(forecast * 1.10) if bias == "Under-Forecast" else int(forecast * 0.85)
        stock_msg = "Aggressive Stock-Up" if bias == "Under-Forecast" else "Lean Stocking"
        
        decisions.append({
            'Market': f"{region}-{cat}",
            'Stock_Rec': stock_rec,
            'Inventory_Strategy': stock_msg,
            'Trade_off': "Margin > Volume" if abs(elasticity) < 1 else "Market Share > Margin"
        })
    return pd.DataFrame(decisions)