# Ejemplo básico del uso de seaborn
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips)
plt.show()