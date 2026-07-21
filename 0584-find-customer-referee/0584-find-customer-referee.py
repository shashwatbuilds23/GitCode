import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer 
    result = df[(
        (df["referee_id"] != 2) | (df["referee_id"].isna())
    )
    ][["name"]]
    return result