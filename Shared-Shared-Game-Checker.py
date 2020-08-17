import json
import time
import requests


def Get_Game_Names(steam_id):
    while len(steam_id) != 17:
        steam_id = input('Invalid Steam ID (It must be 17 numbers.)\nTry Again.\n')
    with open('api_key.txt') as f:
        api_key = f.read()
    base_url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json&include_appinfo=1'
    data = requests.get(base_url).json()
    game_list = []
    for item in data['response']['games']:
        game_name = item['name']
        game_list.append(game_name)
    print(f'Found {len(game_list)} games in profile.\n')
    time.sleep(1)
    return game_list


def Check_For_Shared_Games(lists_to_check):
    list_num = len(lists_to_check)
    final_list = []
    if list_num == 2:
        final_list = set(lists_to_check[0]) & set(lists_to_check[1])
    if list_num == 3:
        final_list = set(lists_to_check[0]) & set(lists_to_check[1]) & set(lists_to_check[2])
    if list_num == 4:
        final_list = set(lists_to_check[0]) & set(lists_to_check[1]) & set(lists_to_check[2]) & set(lists_to_check[3])
    return final_list


def Create_Game_Lists():
    user_check_count = int(input('How many users do you want to compare games for? (2-4)\n'))
    lists_to_check = []
    for user in range(1, user_check_count):
        if user_check_count > 1:
            list_1 = Get_Game_Names(input('\nInput Steam ID 1\n'))
            list_2 = Get_Game_Names(input('Input Steam ID 2\n'))
            lists_to_check.append(list_1)
            lists_to_check.append(list_2)
        if user_check_count > 2:
            list_3 = Get_Game_Names(input('Input Steam ID 3\n'))
            lists_to_check.append(list_3)
        if user_check_count > 3:
            list_4 = Get_Game_Names(input('Input Steam ID 4\n'))
            lists_to_check.append(list_4)
    print(Check_For_Shared_Games(lists_to_check))


if __name__ == "__main__":
    Create_Game_Lists()
