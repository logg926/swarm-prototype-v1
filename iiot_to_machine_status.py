# %%
import pandas as pd
import datetime as dt
# %%
df = pd.read_csv('ProductionReport.csv')
df['END_TIME'] = pd.to_datetime(df['END_TIME'])
# %%
# Check progress - 
# INPUT: replace pattern variable with pattern name
pattern = "{P220082-line}"

pattern_df = df[df['AGG_PATTERN_NAME'].str.contains(pattern)]
total_sum =pattern_df[['COMPLETE']].sum()
# OUTPUT:
print(total_sum)

# %%

# INPUT: list of machine () replace list_of_machine with list of machine 
field_name = 'MC_ID'
list_of_machine = df[field_name].unique()

# if past 24 hr have completed job means the machine is busy
df_past24hr = df[df['END_TIME']>=(dt.datetime.now()-dt.timedelta(hours=24))]
list_of_occupied_machine = df_past24hr[field_name].unique()
list_if_machine_is_occupied = [(x in list_of_occupied_machine) for x in list_of_machine]
df_occupied_or_not = pd.DataFrame({'list_of_machine': list(list_of_machine), 'list_if_machine_is_occupied': list_if_machine_is_occupied, }, columns=['list_of_machine', 'list_if_machine_is_occupied'])
# OUTPUT:
df_occupied_or_not

# %%
