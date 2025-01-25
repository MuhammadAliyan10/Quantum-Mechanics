import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student: pd.DataFrame = students.loc[students['student_id'] == 101]
    return student[['name','age']]