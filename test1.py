from modules.processor import load_data, calculate_recovery_score

df = load_data()
df = calculate_recovery_score(df)

df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20

print(df[['Date', 'Sleep_Hours', 'Heart_Rate_bpm', 'Recovery_Score']].head(10))