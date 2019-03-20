import pandas as pd

data = pd.read_csv("C:\\Users\\Kunal K.S. Sahni\\Desktop\\IET-Makeathon\\apy.csv")

State_Name = list(set(data["State_Name"]))
District_Name = list(set(data["District_Name"]))
Season = list(set(data["Season"]))
Crop = list(set(data["Crop"]))

state_count = 0
district_count = 0
season_count = 0
crop_count = 0

states = {}
crops = {}
districts = {}
seasons = {}

#
for state in State_Name:
    data.replace(state , state_count , inplace = True)
    states[state] = state_count
    state_count+=1

for district in District_Name:
    data.replace(district,district_count,inplace = True)
    districts[district] = district_count
    district_count+=1

for season in Season:
    data.replace(season,season_count,inplace = True)
    seasons[season] = season_count
    season_count+=1

for crop in Crop:
    data.replace(crop,crop_count,inplace = True)
    crops[crop] = crop_count
    crop_count+=1

def returnval():
    return list(states,crops,districts,seasons)
print(states,crops,districts,seasons)
# data.to_csv("new_data.csv")
