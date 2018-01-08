import sys

import csv
import matplotlib.pyplot as plt
import numpy


def main():
    csv = file_to_list("../../DATA/SCii/starcraft.csv")
    list_palyer_per_league = player_per_league(csv)
    display_ranks(list_palyer_per_league)

def file_to_list(location):
        list = []
        with open(location) as fh:
            csv_reader = csv.reader(fh,delimiter = ',')
            for row in csv_reader:
                
                list.append(row)
        return list
    
def display_ranks(player_per_league):
    leagues = ["bronze","silver","gold","plat","diamond","master","gm","pro"]
    plt.bar(  numpy.arange(len(leagues))
                          , player_per_league
                         )
    plt.xticks(numpy.arange(len(leagues)), leagues)
    plt.ylabel('amount')
    plt.title('player per league')
    
    plt.show() 

def player_per_league(csv):
    leagues = [0,0,0,0,0,0,0,0]
    
    for row in csv[1:]:
        num = row[1]
        leagues[int(row[1])-1] += 1
        
        
    return leagues
    
if __name__ == "__main__":
    main()