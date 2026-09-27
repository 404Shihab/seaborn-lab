import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# sns.jointplot(x='total_bill', y='tip', data=tips)

# sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex') # hexagonal bins

sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde') # KDE distribution
 
plt.show()