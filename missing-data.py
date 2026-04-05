import pandas as pd

df = pd.read_csv("D:\ADRIJA_DMV_LAB\dataset.csv")

print(df.isnull().sum())

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))

print("\nOutlier count per column:\n")
print(outliers.sum())

print("\nRows containing outliers:\n")
print(df[outliers.any(axis=1)])
