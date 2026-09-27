import seaborn as sns
import matplotlib.pyplot as plt

# print(sns.__version__)

tips = sns.load_dataset("tips")

# print(tips)
# print(tips.head())

sns.displot(tips["total_bill"], kde=True, bins=30)

plt.show()