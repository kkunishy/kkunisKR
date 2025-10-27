
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame()


df['sum'] = df['test'] + df['assign1']+df['assign2']
df['avg'] = df['sum'] / 3
print(df)
print()
display(df[df['sum']>=88])





display(df)
print()
soft_df=df.sort_values(by='avg',ascending=False)
display(soft_df)

df['grade']=np.where(df['avg']>=90,'A',
            np.where(df['avg']>=80,'B',
            np.where(df['avg']>=70,'C',
            'd')))
print()
display(df)

df['assign1']=[20,17,22,18,24]
df['assign2']=[19,14,18,15,25]
df['sum']=df['test']+df['assign1']+df['assign2']
display(df)

plt.figure



