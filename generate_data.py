import pandas as pd
import numpy as np
from datetime import timedelta, datetime
import random

# Start date
date_start = datetime(2025, 1, 1)

# Initialize data lists
dates = [date_start + timedelta(days=i) for i in range(365)]
steps = np.random.normal(8500, 2500, 365).clip(3000, 18000)
sleep_hours = np.random.normal(7.2, 1, 365).clip(4.5, 9.5)
heart_rate_bpm = np.random.normal(68, 10, 365).clip(48, 110)
calories_burned = np.random.normal(3000, 600, 365).clip(1800, 4200)
active_minutes = np.random.normal(60, 30, 365).clip(20, 180)

# Introduce missing values
for column in [steps, sleep_hours, heart_rate_bpm, calories_burned, active_minutes]:
    indices = random.sample(range(365), int(0.05 * 365))
    for index in indices:
        column[index] = np.nan

# Create DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Steps': steps.round(),
    'Sleep_Hours': sleep_hours.round(1),
    'Heart_Rate_bpm': heart_rate_bpm.round(),
    'Calories_Burned': calories_burned.round(),
    'Active_Minutes': active_minutes.round()
})

# Save to CSV
data.to_csv('data/health_data.csv', index=False)