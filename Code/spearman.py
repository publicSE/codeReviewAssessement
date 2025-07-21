import pandas as pd
from scipy.stats import spearmanr


file_path = 'path2dataset.csv'
data = pd.read_csv(file_path)

column1 = data.iloc[:, 0]
column2 = data.iloc[:, 1]

corr, p_value = spearmanr(column1, column2)

print(f'Spearman Rank Correlation Coefficient: {corr}')
print(f'P-value: {p_value}')
