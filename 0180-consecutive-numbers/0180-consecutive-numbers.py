import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # Sort by id to ensure proper chronological/consecutive order
    logs = logs.sort_values(by='id')
    
    # Get the numbers from the next row and the row after next
    next_num = logs['num'].shift(-1)
    next_next_num = logs['num'].shift(-2)
    
    # Filter where current, next, and next-next values match
    is_consecutive = (logs['num'] == next_num) & (logs['num'] == next_next_num)
    
    # Extract unique values and format the output DataFrame
    unique_nums = logs.loc[is_consecutive, 'num'].unique()
    
    return pd.DataFrame({'ConsecutiveNums': unique_nums}) 