import pandas as pd

a=pd.read_csv("datasetk.csv")
rows=len(a.axes[0])
a.insert(4,"Score",0)
u=input("enter parameters first being the most important and last being least important")
v=input("enter  parameters first being the most important and last being least important")
w=input("enter  parameters first being the most important and last being least important")
x=input("enter  parameters first being the most important and last being least important")
y=input("enter  parameter first being the most important and last being least important")

score=0

for i in range(1,rows-1):
    
    m=str(a.loc[i,"Resume"])
    
    position=i
    label="Score"
    
    if u in m:
        score=int(a.loc[i,"Score"])+5
        
        a.at[position,label]=score
       
       
    if v in m:
        score=int(a.loc[i,"Score"])+4
        a.at[position,label]=score
        

    if w in m:
        score=int(a.loc[i,"Score"])+3
        a.at[position,label]=score
        
        
    if x in m:
        score=int(a.loc[i,"Score"])+2
        a.at[position,label]=score

    if y in m:
        score=int(a.loc[i,"Score"])+1
        a.at[position,label]=score
        
        
max_score=a["Score"].max()
print("Selected candidate ids are")
for i in range(1,rows-1):
    if( int(a.loc[i,"Score"])==max_score):
        print("Selected:",a.loc[i,"ID"])        
