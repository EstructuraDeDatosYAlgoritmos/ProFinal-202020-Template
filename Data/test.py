import pandas as pd

data = pd.read_csv('taxi-trips-wrvz-psew-subset-large.csv')

taxis = data['company'].unique().tolist()

print(len(taxis))
