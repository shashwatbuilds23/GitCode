import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # 1. Drop duplicate salaries to get unique values
    unique_salaries = employee['salary'].drop_duplicates()
    
    # 2. Sort salaries in descending order
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    
    # 3. Handle edge cases: if N is invalid or exceeds available unique salaries
    if N <= 0 or N > len(sorted_salaries):
        # Return None/Null wrapped in the expected column format
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # 4. Get the N-th highest salary (using N-1 due to 0-based indexing)
    nth_salary = sorted_salaries.iloc[N - 1]
    
    # 5. Return the result as a DataFrame
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})