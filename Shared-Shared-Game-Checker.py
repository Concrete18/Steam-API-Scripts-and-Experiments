import json
import time
import requests
import os
from Check_for_API_File import Check_for_API


def Get_Game_Names(steam_id, api_key):
    '''Gets names of games owned by the entered Steam ID.'''
    while len(steam_id) != 17:
        steam_id = input('Invalid Steam ID (It must be 17 numbers.)\nTry Again.\n')
    base_url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&include_played_free_games=0&format=json&include_appinfo=1'
    data = requests.get(base_url).json()
    game_list = []
    for item in data['response']['games']:
        game_name = item['name']
        game_list.append(game_name)
    print(f'Found {len(game_list)} games in profile.\n')
    time.sleep(1)
    return game_list


def Check_For_Shared_Games(lists_to_check):
    '''Finds the shared games among the lists entered.'''
    list_num = len(lists_to_check)
    final_list = []
    if list_num == 2:
        final_list = set(lists_to_check[0]) & set(lists_to_check[1])
    if list_num == 3:
        final_list = set(lists_to_check[0]) & set(lists_to_check[1]) & set(lists_to_check[2])
    if list_num == 4:
        final_list = set(lists_to_check[0]) & set(lists_to_check[1]) & set(lists_to_check[2]) & set(lists_to_check[3])
    return final_list


def Create_Game_Lists(api_key):
    '''Creates a list containing a list each of the profiles games entered using the Get_Game_Names Function.'''
    user_check_count = int(input('How many users do you want to compare games for? (2-4)\n'))
    lists_to_check = []
    if user_check_count > 1:
        list_1 = Get_Game_Names(input('\nInput Steam ID 1\n'), api_key)
        list_2 = Get_Game_Names(input('Input Steam ID 2\n'), api_key)
        lists_to_check.append(list_1)
        lists_to_check.append(list_2)
    if user_check_count > 2:
        list_3 = Get_Game_Names(input('Input Steam ID 3\n'), api_key)
        lists_to_check.append(list_3)
    if user_check_count > 3:
        list_4 = Get_Game_Names(input('Input Steam ID 4\n'), api_key)
        lists_to_check.append(list_4)
    final_list = Check_For_Shared_Games(lists_to_check)
    shared_games = ', '.join(final_list)
    print(f'Total of {len(final_list)} games shared.')
    print(shared_games)
    input()

if __name__ == "__main__":
    api_key = Check_for_API()
    Create_Game_Lists(api_key)
