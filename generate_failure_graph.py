import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data = {
    'Model': ['ChatGPT', 'GPT-4'],
    'Graph Connectivity': [410, 442],
    'Primality Testing': [339, 374],
    'Senator Search': [153, 435],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate percentage values
df['Graph Connectivity %'] = df['Graph Connectivity'] / 500 * 100
df['Primality Testing %'] = df['Primality Testing'] / 500 * 100
df['Senator Search %'] = df['Senator Search'] / 500 * 100

# Calculate average percentages
df['Average %'] = df[['Graph Connectivity %', 'Primality Testing %', 'Senator Search %']].mean(axis=1)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

barWidth = 0.2
r1 = np.arange(len(df))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

ax.bar(r1, df['Graph Connectivity %'], color='coral', width=barWidth, edgecolor='grey', label='Graph Connectivity %')
ax.bar(r2, df['Primality Testing %'], color='salmon', width=barWidth, edgecolor='grey', label='Primality Testing %')
ax.bar(r3, df['Senator Search %'], color='lightcoral', width=barWidth, edgecolor='grey', label='Senator Search %')
ax.bar(r4, df['Average %'], color='purple', width=barWidth, edgecolor='grey', label='Average %')

# Adding xticks
plt.xlabel('Model', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(df))], df['Model'])
plt.ylabel('Percentage')

plt.legend()
plt.title('Performance Comparison')

df, plt.show()