import pandas as pd

def remove_strip(text):
    return text.strip()


data=pd.read_csv("/content/drive/MyDrive/Data.csv")
print(data.head() )#show the head of the dataset
data['Domain']=data['Domain'].apply(remove_strip)
for domain in  data['Domain'].unique():
    print(domain)
    area_data=data.loc[data['Domain']==domain].loc[:,["Abstract","area"]]
    area_data=pd.DataFrame(area_data.to_numpy(),index=area_data.index,columns=["Abstract","Domain"])
    area_data=area_data.reset_index() 
    area_data.to_csv(f"{domain}.csv",index=False)