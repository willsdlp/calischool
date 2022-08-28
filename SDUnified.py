import pandas as pd
import matplotlib.pyplot as plt

# download csv file from Transparent-california.com
# df = pd.read_csv('chula-vista-elementary-2020.csv')
df = pd.read_csv('transparentCaliforniaData/san-diego-unified-2021.csv')

# Find all employees that are teachers
teachers = df[df["Job Title"].str.contains("Regular Teacher")]
# remove hourly teachers
teachers = teachers[teachers["Job Title"].str.contains("Hrly") == False]
# remove special teachers
teachers = teachers[teachers["Job Title"].str.contains("Deaf") == False]
teachers = teachers[teachers["Job Title"].str.contains("Spec Educ") == False]

# teachers with salaries greater than startPay
startPay = 35000
teachersFT = teachers[teachers["Base Pay"] >= startPay]
teacherTypes = teachersFT["Job Title"].unique()

teachersFTi = teachersFT.describe()

print('following teacher types are considered')
print(teacherTypes)

print('average base pay of teachers')
print(teachersFTi.loc["mean", "Base Pay"])
print('average total pay and benefits of teachers')
netPayMean = teachersFTi.loc["mean", "Total Pay & Benefits"]
netPayMedian = teachersFT["Total Pay & Benefits"].median()
print(netPayMean)

# plot the distribution
teachersFT.plot.hist(column=["Total Pay & Benefits"], bins=30)
plt.xlabel("Pay $")
plt.axvline(x=netPayMean, color='r', label='Mean: {:10.2f}'.format(netPayMean))
plt.axvline(x=netPayMedian, color='k', label='Median: {:10.2f}'.format(netPayMedian))
plt.legend()
plt.title("San Diego Unified")
plt.show()
