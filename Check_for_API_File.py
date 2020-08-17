import os

def Check_for_API():
    if os.path.isfile('api_key.txt') is False:
        api_key =''
        with open(os.path.join(os.getcwd(), 'api_key.txt'), 'w') as f:
            api_key = input('Enter your Steam API Key.\n')
            f.write(api_key)
