import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("dataset.csv")
df.head()

#Any missing values?
print("missing values:", df.isnull().values.any())

#plot of normal and fraud transaction number
count_classes = pd.value_counts(df['Class'], sort=True)
count_classes.plot (kind="bar", rot=0)
plt.title("Distributed Transactions")
plt.xticks(range(2), ['Normal', 'Fraud'])
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.show()

#How many normal and fraud transactions?
df['Class'].value_counts()