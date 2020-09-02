import json
import time
import requests
from Check_for_API_File import Check_for_API

steam_id = '76561197982626192'


def Get_Player_Info(steam_id):
    url = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}'
    data = requests.get(url).json()
    # print(data)
    name = data['response']['players'][0]['personaname']
    personastate = data['response']['players'][0]['personastate']
    states = {0: 'Offline', 1: "Online", 2: "Busy", 3: "Away", 4: "Snooze", 5: "Looking To Trade", 6: "Looking To Play"}
    if personastate in states:
        status = states[personastate]
    else:
        status = 'Unknown'
    print(f'{name} is {status}.')
    last_logoff = data['response']['players'][0]['lastlogoff']
    return name, last_logoff, status


def Get_Friends_List(api_key):
    url = f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={api_key}&steamid={steam_id}&relationship=friend'
    data = requests.get(url).json()
    friends_list = []
    for item in data['friendslist']['friends']:
        steamid = item['steamid']
        name, last_logoff, status = Get_Player_Info(steamid)
        friend = {
            "name": name,
            "personastate": personastate,
            "last logoff": last_logoff,
            "steam id": steamid
            }
        friends_list.append(name)
    return friends_list


if __name__ == "__main__":
    api_key = Check_for_API()
    print(Get_Friends_List(api_key))
