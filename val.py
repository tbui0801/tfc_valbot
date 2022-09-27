from turtle import goto
from valo_api import endpoints
import json

name = "Twerkyyy"
tag = "95355"
region = "na"

data = endpoints.get_mmr_details_by_name_v2(region,name,tag)

print(data.name)
print(data.tag)
print(data.current_data.currenttierpatched)
rank = data.current_data
seasons = data.by_season

for act in seasons:
    SeasonDataV2 = seasons[act]
    listofwins = SeasonDataV2.act_rank_wins
    print(act)
    if listofwins is not None: 
        for winobject in listofwins:
            rank = winobject.patched_tier
            tier = winobject.tier
            print(rank, tier)
    

# with open('output.txt', 'w') as f:
#     f.write(matches)


