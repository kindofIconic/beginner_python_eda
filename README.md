# \# beginner\_python\_eda

# 

# \## Sample dataset

# 

# This repository includes a beginner-friendly synthetic CSV dataset for exploratory data analysis:

# 

# `data/student\_performance.csv`

# 

# The dataset contains fictional student performance records that can be used to practise loading, checking and exploring data with pandas.

# 

# \### Columns

# 

# \- `student\_id`: Unique fictional student ID

# \- `class\_group`: Fictional class group

# \- `study\_hours\_per\_week`: Study hours per week

# \- `attendance\_pct`: Attendance percentage

# \- `homework\_completed\_pct`: Homework completion percentage

# \- `math\_score`: Math score out of 100

# \- `reading\_score`: Reading score out of 100

# \- `writing\_score`: Writing score out of 100

# 

# \### Example

# 

# ```python

# import pandas as pd

# 

# df = pd.read\_csv("data/student\_performance.csv")

# 

# print(df.head())

# print(df.describe())

# print(df.groupby("class\_group")\[\["math\_score", "reading\_score", "writing\_score"]].mean())

