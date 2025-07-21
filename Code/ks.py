import pandas as pd
from scipy.stats import spearmanr
import pandas as pd
from scipy.stats import ks_2samp
import numpy as np

file_path = 'path2dataset.csv'
data = pd.read_csv(file_path)


data1 = data.iloc[:, 0]
data2 = data.iloc[:, 1]


ks_stat, p_value = ks_2samp(data2, data1)

mean1, mean2 = np.mean(data1), np.mean(data2)
std1, std2 = np.std(data1, ddof=1), np.std(data2, ddof=1)

n1, n2 = len(data1), len(data2)

pooled_std = np.sqrt(((n1 - 1) * std1**2 + (n2 - 1) * std2**2) / (n1 + n2 - 2))

cohen_d = (mean1 - mean2) / pooled_std

print(f"Cohen's d: {cohen_d}")