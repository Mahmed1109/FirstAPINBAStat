from nba_api.stats.endpoints import PlayerGameLog
#playergamelog gives you game stats for player, points, assists, rebounds for each game.
from nba_api.stats.static import players
#imports all players current and past
import pandas as pd
#used to create data table
from tabulate import tabulate
#takes the dataframe table and makes it into a readable format

def search_player(pname):
    # Function to search for player if not found it will return msg Player not found 
    player = players.find_players_by_full_name(pname)
    if not player:
        return "Player cant be found"
    return player[0]

def get_stats(player_id):
    # Function to grab the games for the season specified for this instance is the 24/25 season
    gamelog = PlayerGameLog(player_id=player_id, season='2024-25')
    df = gamelog.get_data_frames()[0]
    

def main():
    pname=input("Enter the players full name please:")

    player=search_player(pname)
    #checks for player is a viable string in the season search
    #isinstance is python function, first parameter is player input and second is checking if its a string
    if isinstance(player,str):
        print(player)
        return
    
    try:
        stats=get_stats(player['id'])
        print(f"\n Stats for {player['full_name']})(Season 24-25):")
        print(tabulate(stats,headers='keys', tablefmt='grid', showindex=False))
        #tablemft=grid is just the style, and showindex just turns the row numbers off

    except Exception as e:
        print(f"Error getting data: {e}")

if __name__=="__main__":
    main()



