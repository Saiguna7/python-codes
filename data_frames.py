import pandas as pd 
from tabulate import tabulate
data={'Forest fires':['Ground fires','Crown fires','Surface fires','Fire storm'],'Nuclear disasters':['Chernobil','Fukushima','Chernobil','Fukushima'],'Chemical dosaster':['Bhopa gas leak','MIC','UCIL',"Sevin Manufacturing"]}
df=pd.DataFrame(data)
table=tabulate(data,headers='keys',tablefmt='grid')
print(table)