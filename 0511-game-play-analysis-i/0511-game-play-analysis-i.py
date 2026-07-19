import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Group by player_id and find the minimum event_date
    df = activity.groupby('player_id')['event_date'].min().reset_index()
    
    # Rename the column to match the required output
    df.rename(columns={'event_date': 'first_login'}, inplace=True)
    
    return df