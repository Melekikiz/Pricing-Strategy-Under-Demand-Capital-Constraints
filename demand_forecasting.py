from statsmodels.tsa.seasonal import seasonal_decompose

def generate_pricing_aware_forecast(ts_data, unit_drop_rate=0.0435):
    """Generates 12-week forecast adjusted by pricing strategy impact."""
    decomposition = seasonal_decompose(ts_data['total_qty'], model='additive', period=12)
    seasonal_pattern = decomposition.seasonal.iloc[-12:].values
    trend_value = decomposition.trend.iloc[-12:].mean()
    
    forecasts = []
    for i in range(12):
        base_val = trend_value + seasonal_pattern[i]
        forecasts.append(base_val * (1 - unit_drop_rate))
    return forecasts