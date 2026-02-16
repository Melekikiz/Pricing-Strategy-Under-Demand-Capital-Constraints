from sqlalchemy import create_engine
import pandas as pd

def get_engine():
    """Returns a SQLAlchemy engine for PostgreSQL."""
    return create_engine('postgresql://postgres:""@localhost:5432/forecasting&revenue')



def fetch_sales_data(engine):
    """Fetches raw sales and promotion data from the database."""
    query = """
        SELECT 
          o.region, p.category, p.product_id,
          date_trunc('week', o.order_date)::date as sales_week,
          AVG(oi.unit_price) as weekly_avg_price,
          SUM(oi.quantity) as total_qty,
          SUM(oi.unit_price * oi.quantity) as total_revenue,
          MAX(CASE WHEN pr.promo_id IS NOT NULL THEN 1 ELSE 0 END) as has_promotion
        FROM order_items oi
        JOIN orders o ON oi.order_id = o.order_id
        JOIN products p ON oi.product_id = p.product_id
        LEFT JOIN promotions pr ON o.region = pr.region 
            AND o.order_date::date BETWEEN pr.start_date AND pr.end_date
        GROUP BY 1, 2, 3, 4
        ORDER BY 1, 2, 3, 4;
    """
    return pd.read_sql(query, engine)