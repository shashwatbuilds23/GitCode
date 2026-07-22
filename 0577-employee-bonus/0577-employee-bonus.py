import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Left join Employee with Bonus on empId
    df = employee.merge(bonus, on='empId', how='left')
    
    # Filter for bonus < 1000 or missing bonus (NaN)
    condition = (df['bonus'] < 1000) | (df['bonus'].isna())
    
    # Select only 'name' and 'bonus' columns
    return df.loc[condition, ['name', 'bonus']] 