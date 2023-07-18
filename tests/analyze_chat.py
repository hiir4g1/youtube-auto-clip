import pandas as pd

def analyze_kusa_comments(id):
    file_path = './output/'+id+'/'+id+'.csv'
    # Load the data with correct column names
    df = pd.read_csv(file_path, names=['Timestamp', 'Username', 'Comment', 'Unknown'])

    # Convert the "Timestamp" column to datetime type
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Filter the DataFrame for comments containing "草"
    kusa_comments = df[df['Comment'].str.contains('草', case=False)]  # Case-insensitive match

    # Resample the DataFrame to count the number of comments per minute
    kusa_comments_resampled = kusa_comments.resample('1T', on='Timestamp').count()

    # Find the top 5 minutes with the highest number of comments
    top_5_minutes = kusa_comments_resampled['Comment'].nlargest(5)
    
    # Convert to list of string timestamps
    top_5_minutes_list = [timestamp.strftime('%Y-%m-%d %H:%M:%S') for timestamp in top_5_minutes.index.to_list()]

    return top_5_minutes_list