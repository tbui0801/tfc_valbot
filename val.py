from valo_api import endpoints
import json
import csv

region = "na"

def readcsv(csvfilepath):
    matrix = []
    with open(csvfilepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(row)
            
    return matrix

def main():
    output_csv = []
    names = readcsv('names.csv')
   
    row = get_ranks_valo_api(names, verbose = True) 
    print(row)
    output_csv.append(row)
    
def get_ranks_valo_api(name_csv, verbose = False):
    for eachrow in name_csv: 
        ingamename = eachrow[0]
        tag = eachrow[1]

        if verbose == True:
            print("Working on getting data for: " + ingamename + "#" + tag)

        data = endpoints.get_mmr_details_by_name_v2(region, ingamename, tag)

        row = []
        row.append(ingamename)
        row.append(tag)
        row.append(data.current_data.currenttierpatched)

        print(row)
   
    return row

#WIP
def get_rank_history(ingamename, tag):
    data = endpoints.get_mmr_details_by_name_v2(region, ingamename, tag)    

    rank = data.current_data.currenttierpatched
    seasons = data.by_season

    for act in seasons:
        SeasonDataV2 = seasons[act]
        listofwins = SeasonDataV2.act_rank_wins
        # print(act)
        if listofwins is not None: 
            for winobject in listofwins:
                rank = winobject.patched_tier
                tier = winobject.tier
                # print(rank, tier)
        
def write_txt(filename, content):
    with open(filename + '.txt', 'w') as f:
        f.write(content)

main()