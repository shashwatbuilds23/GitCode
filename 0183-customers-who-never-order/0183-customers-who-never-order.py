import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    a = customers[~customers['id'].isin(orders['customerId'])][['name']]
    a.rename(
        columns={'name': 'Customers'},
        inplace=True
    )
    return a