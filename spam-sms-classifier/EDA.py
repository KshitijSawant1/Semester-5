import pandas as pd
import matplotlib.pyplot as plt 

def Datacleaning(): 
    df.drop(columns=["Unnamed: 2","Unnamed: 3","Unnamed: 4"],inplace=True)
    df.rename(columns={'v1':'Target','v2':'Text'},inplace=True)
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    df['Target'] = encoder.fit_transform(df['Target'])
    print(df.isnull().sum())
    print(df.duplicated().sum())
    df.drop_duplicates(keep="first")
    print(df.shape)

# EDA
df = pd.read_csv("spam-sms-classifier/spam new.csv", encoding='latin-1')
Datacleaning()

#Data Reading Target
print("\nData Reading Target")
print(df["Target"].value_counts())


# Pie chart
plt.pie(df["Target"].value_counts(), labels=["ham", "spam"], autopct="%0.2f%%", colors=["skyblue", "lightcoral"])
plt.title("Distribution of Ham vs Spam Messages")
plt.axis('equal')  
plt.show()