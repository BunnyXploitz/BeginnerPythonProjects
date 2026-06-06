#Pre-Requisites: 
#•Player_1 - Frags, Knockdowns, Damage 
#•Player_2 - Frags, Knockdowns, Damage 
#•Player_3 - Frags, Knockdowns, Damage 
#•Player_4 - Frags, Knockdowns, Damage 


import pandas as pd

# Player data
Player_1 = {'Name': 'Flare',    'Frags': 17, 'Knock_Downs': 8,  'Damage': 1200}
Player_2 = {'Name': 'Rasmalai', 'Frags': 6,  'Knock_Downs': 4,  'Damage': 850}
Player_3 = {'Name': 'Pahadi',   'Frags': 25, 'Knock_Downs': 12, 'Damage': 2100}
Player_4 = {'Name': 'Xyclone',  'Frags': 7,  'Knock_Downs': 5,  'Damage': 950}

# --- DataFrame ---
df = pd.DataFrame([Player_1, Player_2, Player_3, Player_4])
df.index = df.index + 1

print("*" * 40)
print("       ALL PLAYERS - STATS TABLE")
print("*" * 40)
print(df.to_string(index=True))

# --- Team Totals ---
print("\n" + "*" * 40)
print("           TEAM TOTALS")
print("*" * 40)
totals = df[['Frags', 'Knock_Downs', 'Damage']].sum()
print(totals.to_string())

# --- Top Performers ---
print("\n" + "*" * 40)
print("          TOP PERFORMERS")
print("*" * 40)
print(f"Most Frags      : {df.loc[df['Frags'].idxmax(), 'Name']} ({df['Frags'].max()})")
print(f"Most Knock Downs: {df.loc[df['Knock_Downs'].idxmax(), 'Name']} ({df['Knock_Downs'].max()})")
print(f"Most Damage     : {df.loc[df['Damage'].idxmax(), 'Name']} ({df['Damage'].max()})")

# --- Player Rankings by Frags ---
print("\n" + "*" * 40)
print("     PLAYER RANKING (by Frags)")
print("*" * 40)
ranked = df[['Name', 'Frags', 'Knock_Downs', 'Damage']].sort_values('Frags', ascending=False).reset_index(drop=True)
ranked.index = ranked.index + 1
ranked.index.name = 'Rank'
print(ranked.to_string())
print("*" * 40)
