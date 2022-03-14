import numpy as np
import pandas as pd
import plotly.express as ex
import requests
import json

# read the data
df = pd.read_csv("ex/dialect_dataset.csv")

#change the type of it
df["id"] = df.id.astype("str")

# containers
l = []
d=0

#data gathering
for i in range(1,459):
    try:
        data = json.dumps(list(df.iloc[0+d:1000+d,0]))
        post = requests.post("https://recruitment.aimtechnologies.co/ai-tasks",data=data)
        l.append(post.json())        
        d+=1000
        
    except:
        data = json.dumps(list(df.iloc[len(df)-458:,0]))
        post = requests.post("https://recruitment.aimtechnologies.co/ai-tasks",data=data)
        l.append(post.json())        
        d+=1000

print(len(l))


