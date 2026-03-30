
import pandas as pd

#read in csv file
df = pd.read_csv("D:\ClimateBase\monthly-average-surface-temperatures-by-year\monthly-average-surface-temperatures-by-year.csv")

#print(df.head()) print head to check

'''
Melt my data:
melt(
id_vars= Columns used to identify variables
var_name= rename column after melting
value_name= allows you to rename the value column after melting.
)

'''
melted_df = pd.melt(
        df,
        id_vars = ['Country','Month'],
        var_name = 'Year',
        value_name = 'Avg_Temps'
)

#print(melted_df.head(50))

# Changed type of year
melted_df['Year'] =melted_df['Year'].astype(int)

'''
Pivoting table

pivot(index=Column name to use to make new frame’s index,
 columns=Column name to use to make new frame’s columns., 
 values=list of the previous, optional. Column(s) to use for populating new frame’s values.
 )

'''
df_final = melted_df.pivot_table(index=['Country', 'Year'],
                               columns='Month',
                               values='Avg_Temps').reset_index()

print(df_final.head(25))

df_final.to_csv("D:\\ClimateBase\\monthly-average-surface-temperatures-by-year\\clean.csv", index=False)