import pandas as pd
import matplotlib.pyplot as plt

# Read and clean data
df = pd.read_csv(f'C:\\Users\\lab.AUKOL\\Desktop\\company_dtaatset\\company_dataset.csv.xls')
df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')
df['review_count'] = df['review_count'].str.extract('(\d+\.?\d*)')[0].astype(float)
df['years'] = df['years'].str.extract('(\d+)')[0].astype(int)
df['main_hq'] = df['hq'].str.split('+').str[0].str.strip()

# TASK 1: Print Top 10 Company Headquarters
print("="*60)
print("TASK 1: TOP 10 COMPANY HEADQUARTERS")
print("="*60)
for i, row in df.head(10).iterrows():
    print(f"{i+1:2d}. {row['name']:25s} - {row['main_hq']}")

# Create all charts in one figure
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Company Analysis Dashboard', fontsize=18, fontweight='bold')

# TASK 2: Bar Chart - Ratings
top_10 = df.head(10)
axes[0, 0].bar(range(len(top_10)), top_10['ratings'], color='steelblue', edgecolor='black')
axes[0, 0].set_title('Top 10 Companies by Rating', fontweight='bold')
axes[0, 0].set_ylabel('Ratings', fontweight='bold')
axes[0, 0].set_xticks(range(len(top_10)))
axes[0, 0].set_xticklabels(top_10['name'], rotation=45, ha='right', fontsize=9)
axes[0, 0].grid(axis='y', alpha=0.3)

# TASK 3: Horizontal Bar - Reviews (Funnel style)
top_10_reviews = df.nlargest(10, 'review_count').sort_values('review_count', ascending=True)
colors = plt.cm.Blues(range(len(top_10_reviews)))[::-1]
axes[0, 1].barh(top_10_reviews['name'], top_10_reviews['review_count'], color=colors, edgecolor='black')
axes[0, 1].set_title('Top 10 Companies by Reviews', fontweight='bold')
axes[0, 1].set_xlabel('Review Count (k)', fontweight='bold')
for i, v in enumerate(top_10_reviews['review_count']):
    axes[0, 1].text(v + 1, i, f'{v:.1f}k', va='center', fontsize=8)
axes[0, 1].grid(axis='x', alpha=0.3)

# TASK 4: Line Chart - Rating Trend
axes[1, 0].plot(range(1, 11), top_10['ratings'], marker='o', linewidth=2.5, 
                markersize=8, color='darkgreen', markerfacecolor='lightgreen', markeredgewidth=2)
axes[1, 0].set_title('Rating Trend - Top 10 Companies', fontweight='bold')
axes[1, 0].set_xlabel('Company Rank', fontweight='bold')
axes[1, 0].set_ylabel('Rating', fontweight='bold')
axes[1, 0].set_xticks(range(1, 11))
axes[1, 0].set_xticklabels(top_10['name'], rotation=45, ha='right', fontsize=9)
axes[1, 0].grid(True, alpha=0.3)

# TASK 5: Pie Chart - Top 5 Oldest Companies
top_5_years = df.nlargest(5, 'years')
colors_pie = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
axes[1, 1].pie(top_5_years['years'], labels=top_5_years['name'], autopct='%1.1f%%',
               startangle=90, colors=colors_pie, textprops={'fontsize': 9})
axes[1, 1].set_title('Top 5 Oldest Companies by Age', fontweight='bold')

plt.tight_layout()
plt.savefig('company_analysis_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✓ All charts saved as 'company_analysis_dashboard.png'")
