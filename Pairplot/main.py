import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")


# print(tips)

# sns.pairplot(tips)
sns.pairplot(tips, hue="smoker")

plt.show()