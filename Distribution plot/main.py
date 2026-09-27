import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# print(tips)

# sns.rugplot(tips["total_bill"])

sns.displot(tips["total_bill"], kde=True)

plt.show()