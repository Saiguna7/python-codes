import pandas as pd
from tabulate import tabulate

# Create a sample DataFrame with roll numbers and names
data = {'Roll Number': ['B21EE121L','B21EE122L', 'B21EE123L', 'B21EE124L', 'B21EE125L','B21EE126L','B21EE127L','B21EE128L','B21EE129L','B21EE130L','B21EE131L','B21EE132L'],
        'Name': ['JUPELLY ROHITH', 'SAI TEJ', 'MD ZEESHAN', 'SHEKAR', 'BANKA SPANDANA PRIYA','VARSHIT','VARUN RAJ','SAI BALAJI','GANJI DEEPIKA','SAI ANIRUDH','SAI SANTHOSH','MAMIDALA SAI VARSHITHA'],
        'Entry Type': ['Lateral', 'Lateral', 'Lateral', 'Lateral', 'Lateral','Lateral', 'Lateral', 'Lateral', 'Lateral', 'Lateral','Lateral', 'Lateral',]}

df = pd.DataFrame(data)

# Filter the DataFrame to get lateral entry students
lateral_entry_students = df[df['Entry Type'] == 'Lateral']

# Print the lateral entry student information in a table
table = tabulate(lateral_entry_students, headers='keys', tablefmt='grid')
print(table)
