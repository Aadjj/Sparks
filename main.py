import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

file_path = "C:\\Users\\Mohammed Khubaib\\OneDrive\\Desktop\\globalterrorismdb_0718dist.csv"
data = pd.read_csv(file_path, encoding='latin1')
plt.style.use('seaborn-whitegrid')

plt.figure(figsize=(12, 6))
sns.countplot(x='region_txt', data=data, order=data['region_txt'].value_counts().index, palette='viridis')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.title('Hot Zones of Terrorism', fontsize=14, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Number of Incidents', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
yearly_incidents = data['iyear'].value_counts().sort_index()
sns.lineplot(x=yearly_incidents.index, y=yearly_incidents.values, color='blue')
plt.title('Number of Terrorist Incidents Over the Years', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Incidents', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='attacktype1_txt', data=data, order=data['attacktype1_txt'].value_counts().index, palette='muted')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.title('Types of Attacks', fontsize=14, fontweight='bold')
plt.xlabel('Attack Type', fontsize=12)
plt.ylabel('Number of Incidents', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(y='targtype1_txt', data=data, order=data['targtype1_txt'].value_counts().index, palette='muted')
plt.title('Target Types', fontsize=14, fontweight='bold')
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('Target Type', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(y='weaptype1_txt', data=data, order=data['weaptype1_txt'].value_counts().index, palette='muted')
plt.title('Weapons Used', fontsize=14, fontweight='bold')
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('Weapon Type', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(y='gname', data=data, order=data['gname'].value_counts().iloc[:15].index, palette='muted')
plt.title('Top 15 Terrorist Groups', fontsize=14, fontweight='bold')
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('Terrorist Group', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(y='country_txt', data=data, order=data['country_txt'].value_counts().iloc[:15].index, palette='muted')
plt.title('Top 15 Countries with Most Terrorist Incidents', fontsize=14, fontweight='bold')
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
yearly_casualties = data.groupby('iyear')['nkill'].sum().sort_index()
sns.lineplot(x=yearly_casualties.index, y=yearly_casualties.values, color='red')
plt.title('Number of Casualties from Terrorist Incidents Over the Years', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Casualties', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
monthly_attacks = data['imonth'].value_counts().sort_index()
sns.barplot(x=monthly_attacks.index, y=monthly_attacks.values, color='purple')
plt.title('Terrorist Attacks by Month', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Attacks', fontsize=12)
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
attack_success_counts = data['success'].value_counts()
colors = ['#F15F5F', '#7AC36A']  # Red and green colors for attack success and failure respectively
plt.pie(attack_success_counts, labels=attack_success_counts.index, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Terrorist Attacks by Attack Success', fontsize=14, fontweight='bold')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
target_nationalities = data['natlty1_txt'].value_counts().iloc[:10]
sns.barplot(x=target_nationalities.values, y=target_nationalities.index, palette='muted')
plt.title('Top 10 Target Nationalities', fontsize=14, fontweight='bold')
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('Nationality', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
attacks_by_region_year = data.groupby(['region_txt', 'iyear']).size().reset_index(name='count')
sns.lineplot(x='iyear', y='count', hue='region_txt', data=attacks_by_region_year, palette='muted')
plt.title('Terrorist Attacks by Region and Year', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Attacks', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

major_economic_countries = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'France']
plt.figure(figsize=(12, 8))
incidents_by_country_year = data[data['country_txt'].isin(major_economic_countries)].groupby(['country_txt', 'iyear']).size().reset_index(name='count')
sns.lineplot(x='iyear', y='count', hue='country_txt', data=incidents_by_country_year, palette='Set2', linewidth=2.5)
plt.title('Number of Terrorist Incidents on major Economical HotSpots and in which Year', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Incidents', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Country', title_fontsize=12, fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

region_counts = data['region_txt'].value_counts()
colors = ['#F15F5F', '#7AC36A', '#5A9BD4', '#FAA75B', '#9E67AB', '#CE7058', '#D77FB4',
          '#737373', '#D9E2F3', '#A389D4', '#FFB878', '#7E4452', '#FAC858', '#FB7D4C', '#5E1833']
fig = px.pie(data_frame=region_counts, names=region_counts.index, title='Hot Zones of Terrorism',
             color_discrete_sequence=colors)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_font=dict(size=16, family='Arial', color='white'),
                  legend=dict(title='Regions', font=dict(size=12, family='Arial', color='white')),
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0.7)',
                  font=dict(color='white'))
fig.show()
