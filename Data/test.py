import pandas as pd

data = pd.read_csv('taxi-trips-wrvz-psew-subset-large.csv')

print(data.columns)

taxis = data['dropoff_community_area'].unique().tolist()
taxis.sort()
print(taxis)
