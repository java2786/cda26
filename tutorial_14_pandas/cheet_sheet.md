## Quick Reference Cheat Sheet    
    
```python    
# Reading Data    
pd.read_csv('file.csv')              # Read CSV    
pd.read_excel('file.xlsx')           # Read Excel    
    
# Viewing Data    
df.head()                            # First 5 rows    
df.tail()                            # Last 5 rows    
df.info()                            # Data types and info    
df.describe()                        # Statistical summary    
df.shape                             # (rows, columns)    
    
# Selecting Data    
df['column']                         # Single column    
df[['col1', 'col2']]                # Multiple columns    
df.iloc[0]                           # First row    
df.iloc[0:5]                         # First 5 rows    
df[df['col'] > 100]                 # Filtering    
    
# Adding/Modifying    
df['new_col'] = values              # Add column    
df.loc[0, 'col'] = value            # Update value    
    
# Deleting    
df.drop('col', axis=1)              # Delete column    
df.drop(0, axis=0)                  # Delete row    
    
# Sorting    
df.sort_values('col')               # Sort ascending    
df.sort_values('col', ascending=False)  # Sort descending    
    
# GroupBy    
df.groupby('col')['col2'].sum()     # Group and sum    
df.groupby('col').agg({'col2': ['sum', 'mean']})  # Multiple agg    
    
# Missing Data    
df.isnull()                         # Check missing    
df.isnull().sum()                   # Count missing    
df.fillna(0)                        # Fill with 0    
df.dropna()                         # Drop missing rows    
    
# Export    
df.to_csv('file.csv', index=False)  # Save to CSV    
df.to_excel('file.xlsx', index=False)  # Save to Excel    
```    
    
