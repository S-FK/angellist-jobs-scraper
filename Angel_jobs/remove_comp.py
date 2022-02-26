import pandas as pd
df = pd.read_csv('internships.csv')
df['Company Name'] = df['Company Name'].str.split(n=1).str[1]
df.to_csv("updated.csv")
