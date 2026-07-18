import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Convert recordDate to datetime objects
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    
    # Create a copy representing "yesterday" by shifting the date forward by 1 day
    yesterday = weather.copy()
    yesterday['recordDate'] = yesterday['recordDate'] + pd.Timedelta(days=1)
    
    # Merge today's weather data with yesterday's weather data
    merged = weather.merge(yesterday, on='recordDate', suffixes=('', '_prev'))
    
    # Filter where today's temperature is greater than yesterday's temperature
    result = merged[merged['temperature'] > merged['temperature_prev']]
    
    # Return only the 'id' column as a DataFrame
    return result[['id']] 