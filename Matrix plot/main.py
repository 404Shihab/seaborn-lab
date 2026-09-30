import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# print(tips)

tc =tips.corr(numeric_only=True)

sns.heatmap(tc)

plt.show()

