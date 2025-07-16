import pandas as pd
df = pd.read_csv("spam-sms-classifier/spam new.csv", encoding='latin-1')
#drop last three columns
print("\nDrop last three columns")
df.drop(columns=["Unnamed: 2","Unnamed: 3","Unnamed: 4"],inplace=True)
print(df.sample())

# rename columns 
print("\n Rename columns ")
df.rename(columns={'v1':'Target','v2':'Text'},inplace=True)
print(df.sample())

# Re Fitting first column "Target"
print("\nRe Fitting first column Target")
print(df["Target"].unique())
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df['Target'] = encoder.fit_transform(df['Target'])
print(df.head())

# Check for missing values 
print("\nCheck for missing values ")
print(df.isnull().sum())

# Check for duplicate Values 
print("\nCheck for duplicate Values")
print(df.duplicated().sum())

#Remove Duplicate Values 
print("\nRemove Duplicate Values ")
df.drop_duplicates(keep="first")

# After Changes 
print("\nAfter Changes ")
print(df.shape)
