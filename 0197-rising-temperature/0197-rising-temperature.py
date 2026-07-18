import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather["recordDate"] = pd.to_datetime(weather["recordDate"])
    weather = weather.sort_values("recordDate")
    yesterday_date = weather["recordDate"].shift(1)
    yesterday_temperature = weather["temperature"].shift(1)
    mask = (yesterday_date == weather["recordDate"] - pd.Timedelta(days=1)) & (yesterday_temperature < weather["temperature"])
    return weather.loc[mask][["id"]]