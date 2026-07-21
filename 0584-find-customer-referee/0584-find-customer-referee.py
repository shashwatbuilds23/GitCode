import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where referee_id is not equal to 2 OR referee_id is NaN (null)
    condition = (customer['referee_id'] != 2) | (customer['referee_id'].isna())
    
    # Return only the 'name' column as a DataFrame
    return customer.loc[condition, ['name']]