import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# print(tips.head().to_string())

# -------barplot------

# sns.barplot(x='day', y='total_bill', data=tips, estimator=sum)
# sns.barplot(x='day', y='smoker', data=tips, estimator=sum)

# -------boxplot----
# sns.boxplot(x='day',y='total_bill',data=tips)

# sns.boxplot(x='day',y='total_bill',data=tips, hue='smoker')

# ---------voilinplot----------

sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker', split=True)

plt.show()