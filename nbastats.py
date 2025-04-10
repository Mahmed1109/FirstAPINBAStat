from nba_api.stats.endpoints import playergamelog
#playergamelog gives you game stats for player, points, assists, rebounds for each game.
from nba_api.stats.static import players
#imports all players current and past
import pandas as pd
#used to display stats in tables from the info i get from API

def search_player(name):
    # Function to search for player if not found it will return msg Player not found 
    player = players.find_players_by_full_name(name)
    if not player:
        return "Player cant be found"
    return player[0]

def get_stats(player_id):
    # Function to grab the games for the season specified for this instance is the 24/25 season
    gamelog = playergamelog(player_id=player_id, season='2024-25')
    df = gamelog.get_data_frames()[0]

