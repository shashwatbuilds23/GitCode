import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 1. Find the maximum salary for each department
    employee['max_salary'] = employee.groupby('departmentId')['salary'].transform('max')
    
    # 2. Filter employees who earn the maximum salary in their department
    highest_earners = employee[employee['salary'] == employee['max_salary']]
    
    # 3. Merge with Department dataframe to get department names
    result = highest_earners.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    
    # 4. Rename columns and select the specific output fields
    result = result.rename(columns={
        'name_dept': 'Department',
        'name_emp': 'Employee',
        'salary': 'Salary'
    })
    
    return result[['Department', 'Employee', 'Salary']]