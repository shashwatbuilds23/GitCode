
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    z = list(logs['num'].values)
    it = []
    if len(z) > 0:
        c =  1
        for i in range(1, len(z)):
            if z[i] == z[i-1]:
                c += 1
            else:
                c = 1
            if c == 3:
                it.append(z[i-1])

    df = pd.DataFrame({'ConsecutiveNums': [*list(set(it))]})
        
    return df