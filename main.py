from database_connector import get_engine, fetch_sales_data
from pricing_intelligence import calculate_elasticity_matrix
from pricing_simulation import run_optimization
from demand_forecasting import generate_pricing_aware_forecast
from forecast_risk_analysis import calculate_financial_risks
from decision_layer import generate_inventory_decisions

def run_pipeline():
    engine = get_engine()
    df = fetch_sales_data(engine)
    print("✅ Step 1: Data ingested from PostgreSQL.")

    elasticity_matrix = calculate_elasticity_matrix(df)
    print("✅ Step 2: Elasticity matrix calculated.")

    opt_report = run_optimization(elasticity_matrix)
    print("✅ Step 3: Pricing optimization complete.")

   
    ts_data = df.groupby('sales_week').agg({'total_qty': 'sum'}).reset_index()
    forecast_results = generate_pricing_aware_forecast(ts_data)
    print("✅ Step 4: Demand forecasting successful.")

   
    categories_data = [
        ('APAC', 'Electronics', 48500, 'Aggressive (+15%)', -0.14),
        ('US', 'Fashion', 32000, 'Defensive (0%)', -1.78)
    ]
    risk_df = calculate_financial_risks(categories_data)
    print("✅ Step 5: Financial risks analyzed.")

    final_decisions = generate_inventory_decisions(categories_data)
    print("\n--- FINAL EXECUTIVE DECISIONS ---")
    print(final_decisions)

if __name__ == "__main__":
    run_pipeline()