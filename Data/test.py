import pandas as pd

#data = pd.read_csv('taxi-trips-wrvz-psew-subset-large.csv')
#data = pd.read_csv('taxi-trips-wrvz-psew-subset-medium.csv')
data = pd.read_csv('taxi-trips-wrvz-psew-subset-small.csv')

print(data.columns)

#taxis = data['dropoff_community_area'].unique().tolist()
taxis = data['trip_start_timestamp'].unique()
taxis.sort()
print(taxis)
