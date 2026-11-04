import math
import pandas as pd
import matplotlib.pyplot as plt

#importing the csv file
data = pd.read_csv("pandas and matplotlib combined/Messy_Employee_dataset.csv")

#cleaning the dataset
data[["Department", "Region"]] = data["Department_Region"].str.split("-", expand=True) # Split and assign directly to new columns in `data`
epl_dept = data.groupby(data["Department"])
epl_reg = data.groupby(data["Region"])
data = data.drop(columns=["Department_Region"])


mean_age = data["Age"].mean()
mean_age = math.floor(mean_age)
data = data.fillna({'Age' : mean_age})

data["Join_Date"] = pd.to_datetime(data["Join_Date"], format="mixed")
data = data.drop_duplicates()

#Across employee demographics
age_dis = data.groupby("Age") #Age distribution of employees
dept = data.groupby("Department") #Employee distribution in departments
age_mode = data["Age"].mode()
ag_dis = age_dis["Employee_ID"].count() #Stores the amount of employees in each age group
max_group = ag_dis.max() #stores the value of the age group with the most employees

avg_sal = data["Salary"].mean()
#Average salary across all departments
for name, group in dept:
    print(f"--- {name} Department Salaries ---")
    print(group["Salary"].mean())


#providing the output after doing some EDA
#Employee Data
# print("Average age of employee : ", mean_age)
# print("The age distribution : ", ag_dis)
# print("The age group with the most employees : ", max_group, '-', "32 y.o")
# print("Employees in each department \n", dept["Employee_ID"].count())

#Salary analysis
print("Average salary : ", avg_sal)