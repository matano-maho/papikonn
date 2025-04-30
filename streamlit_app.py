import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# データ作成（例：2群）
np.random.seed(0)
groupA = np.random.normal(loc=5, scale=1, size=30)
groupB = np.random.normal(loc=6, scale=1, size=30)

# Mann-Whitney U検定の実施
u_statistic, p_value = stats.mannwhitneyu(groupA, groupB, alternative='two-sided')

# データ整形
df = pd.DataFrame({
    'Value': np.concatenate([groupA, groupB]),
    'Group': ['Group A'] * len(groupA) + ['Group B'] * len(groupB)
})

# ボックスプロットで可視化
plt.figure(figsize=(8, 6))
sns.boxplot(x='Group', y='Value', data=df, palette='pastel')
plt.title(f'Mann-Whitney U Test (U={u_statistic:.2f}, p={p_value:.3f})')
plt.grid(True)
plt.tight_layout()
plt.show()