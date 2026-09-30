import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# print(tips.head().to_string())

# ------- Bar Plot -------

# sns.barplot(x="day", y="total_bill", data=tips, estimator=sum)
# sns.barplot(x="day", y="smoker", data=tips, estimator=sum)

# ------- Box Plot -------

# sns.boxplot(x="day", y="total_bill", data=tips)
# sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker")

# ------- Violin Plot -------

# sns.violinplot(x="day", y="total_bill", data=tips, hue="smoker", split=True)

# ------- Cat Plot -------

# sns.catplot(x="day", y="total_bill", data=tips, kind="bar")
sns.catplot(x="day", y="total_bill", data=tips, kind="violin")

plt.show()