import pandas as pd

# Load the data from the image into a Pandas DataFrame
data = pd.read_fwf('unnamed.png', header=None, names=['Roll Number', 'Name'])

# Filter the DataFrame to only include lateral entry students
lateral_entry_students = data[data['Roll Number'].str.startswith('B22EC2')]

# Print the roll numbers and names of the lateral entry students
print(lateral_entry_students[['Roll Number', 'Name']])