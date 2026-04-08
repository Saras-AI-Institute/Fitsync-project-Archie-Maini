import pandas as pd

def load_data():
    """
    Load the health data CSV, handle missing values, and convert the 'Date' column to datetime objects.
    Returns the cleaned DataFrame.
    """
    # Read the CSV file
    file_path = 'data/health_data.csv'
    data = pd.read_csv(file_path)
    
    # Handle missing values intelligently
    # Fill missing 'Steps' with the median value of the column
    data['Steps'].fillna(data['Steps'].median(), inplace=True)
    
    # Fill missing 'Sleep_Hours' with a default value of 7.0
    data['Sleep_Hours'].fillna(7.0, inplace=True)
    
    # Fill missing 'Heart_Rate_bpm' with a default value of 68
    data['Heart_Rate_bpm'].fillna(68, inplace=True)
    
    # Fill missing values in other columns with their respective median values
    for column in ['Calories_Burned', 'Active_Minutes']:
        data[column].fillna(data[column].median(), inplace=True)
    
    # Convert the 'Date' column to datetime objects
    data['Date'] = pd.to_datetime(data['Date'])
    
    return data

def calculate_recovery_score(df):
    """
    Calculate and add a 'Recovery_Score' column to the DataFrame based on sleep hours, heart rate, and steps.

    Parameters:
        df (pd.DataFrame): DataFrame containing health metrics.

    Returns:
        pd.DataFrame: DataFrame with a new 'Recovery_Score' column.
    """
    # Initialize the Recovery_Score column with a base score of 50
    df['Recovery_Score'] = 50

    # Adjust score based on Sleep Hours
    # Good sleep (7+ hours) improves recovery score significantly
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20
    # Poor sleep (less than 6 hours) heavily reduces recovery score
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_Score'] -= 15

    # Adjust score based on Heart Rate bpm
    # Lower heart rates are better for recovery
    df.loc[df['Heart_Rate_bpm'] <= 70, 'Recovery_Score'] += 10
    # Higher heart rates might indicate stress or poor recovery
    df.loc[df['Heart_Rate_bpm'] > 85, 'Recovery_Score'] -= 10

    # Adjust score based on Steps
    # Moderate activity (between 8000 and 14000 steps) is good
    df.loc[(df['Steps'] >= 8000) & (df['Steps'] <= 14000), 'Recovery_Score'] += 5
    # Very low or very high activity can reduce recovery slightly
    df.loc[df['Steps'] < 4000, 'Recovery_Score'] -= 5
    df.loc[df['Steps'] > 14000, 'Recovery_Score'] -= 5

    # Ensure the Recovery_Score stays within the range [0, 100]
    df['Recovery_Score'] = df['Recovery_Score'].clip(lower=0, upper=100)

    return df

