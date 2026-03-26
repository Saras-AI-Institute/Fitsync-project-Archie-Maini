import numpy as np
import pandas as pd
from datetime import timedelta, datetime

# Set seed for reproducibility
np.random.seed(42)

# Define the start date
start_date = datetime(2025, 1, 1)

# Number of days
days = 365

# Generate dates
dates = [start_date + timedelta(days=i) for i in range(days)]

# Generate data with specified distributions
steps = np.random.normal(loc=8500, scale=3000, size=days).clip(3000, 18000)
sleep_hours = np.random.normal(loc=7.2, scale=1.0, size=days).clip(4.5, 9.5)
heart_rate_bpm = np.random.normal(loc=68, scale=10, size=days).clip(48, 110)
calories_burned = np.random.uniform(1800, 4200, size=days)
active_minutes = np.random.uniform(20, 180, size=days)

# Introduce 5% NaN values randomly in each column
def introduce_nan(data, fraction=0.05):
    nan_indices = np.random.choice(data.size, size=int(data.size * fraction), replace=False)
    data.ravel()[nan_indices] = np.nan
    return data

steps = introduce_nan(steps)
sleep_hours = introduce_nan(sleep_hours)
heart_rate_bpm = introduce_nan(heart_rate_bpm)
calories_burned = introduce_nan(calories_burned)
active_minutes = introduce_nan(active_minutes)

# Create a DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_Rate_bpm': heart_rate_bpm,
    'Calories_Burned': calories_burned,
    'Active_Minutes': active_minutes
})

# Save to CSV
data.to_csv('data/health_data.csv', index=False)
