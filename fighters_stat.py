import requests
import json

class FightersStatistics:

    def __init__(self): # TODO:fighter_id
        # self.api_key = api_key
        # self.fighter_id = fighter_id
        self.fighter_stat = None 

    def get_fighters_list_stat(self): 
        url = f"https://api.sportsdata.io/v3/mma/scores/json/Fighters"
        headers = {'Ocp-Apim-Subscription-Key': '6a440b2acb3d45bcae299abb9813839c'}
        json_url = requests.get(url, headers=headers)
        data = json.loads(json_url.text)
        # print(data)
        try:
            data = data[0]["CareerStats"]
        except:
            data = None
        return data
