import requests
import json
from operator import itemgetter

class FightersStatistics:

    # The constructor Method
    def __init__(self): # TODO:fighter_id
        # self.api_key = api_key
        # self.fighter_id = fighter_id
        self.fighter_stat = None 
        self.fighter_data = None

    # Get any fighter statistics
    def get_fighters_list_stat(self): 
        url = f"https://api.sportsdata.io/v3/mma/scores/json/Fighters"
        headers = {'Ocp-Apim-Subscription-Key': '6a440b2acb3d45bcae299abb9813839c'}
        json_url = requests.get(url, headers=headers)
        data = json.loads(json_url.text)
        # print(data)

        try:
            data = data
        except:
            data = None

        def get_fighter_knocks(player):   
            knockOuts = player['Wins']

            if type(knockOuts) != int:
                knockOuts = 1

            return knockOuts

        list1 = sorted(data, key=get_fighter_knocks, reverse=True)
        print(list1)
        
        self.fighter_stat = list1
        return list1

    # Dump File Method
    def dump(self):
        if self.fighter_stat is None:
            return

        fighter_title = "Fighter Name" # TODO: get fighter name from data
        fighter_title = fighter_title.replace(" ","_").lower()
        file_name = fighter_title + ".json"
        with open(file_name, 'w') as f:
            json.dump(self.fighter_stat, f, indent=4)

        print("file dumped")
