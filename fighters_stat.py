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

        self.fighter_stat = data
        return data

    def get_fighter_stat(self):
        pass

    def get_fighters_by_wins(self):
        url = f"https://api.sportsdata.io/v3/mma/scores/json/Fighters"
        headers = {'Ocp-Apim-Subscription-Key': '6a440b2acb3d45bcae299abb9813839c'}
        json_url = requests.get(url, headers=headers)
        data = json.loads(json_url.text)
        # print(data)

        try:
            data = data
        except:
            data = None

        def get_fighter_wins(player):   
            knockOuts = player['Wins']

            if type(knockOuts) != int:
                knockOuts = 1

            return knockOuts

        list1 = sorted(data, key=get_fighter_wins, reverse=True)
        print(list1)
        
        self.fighter_stat = list1
        return list1

    def get_event_2021(self):
        url = f"https://api.sportsdata.io/v3/mma/scores/json/Schedule/UFC/2021"
        headers = {'Ocp-Apim-Subscription-Key': '6a440b2acb3d45bcae299abb9813839c'}
        json_url = requests.get(url, headers=headers)
        data = json.loads(json_url.text)
        # print(data)

        try:
            data = data
        except:
            data = None

        self.fighter_stat = data
        return data

    def get_event_2020(self):
        url = f"https://api.sportsdata.io/v3/mma/scores/json/Schedule/UFC/2020"
        headers = {'Ocp-Apim-Subscription-Key': '6a440b2acb3d45bcae299abb9813839c'}
        json_url = requests.get(url, headers=headers)
        data = json.loads(json_url.text)
        # print(data)

        try:
            data = data
        except:
            data = None

        self.fighter_stat = data
        return data

    def get_events_2020(self):
        url = f"https://api.sportsdata.io/v3/mma/scores/json/Schedule/UFC/2020"
        headers = {'Ocp-Apim-Subscription-Key': '6a440b2acb3d45bcae299abb9813839c'}
        json_url = requests.get(url, headers=headers)
        data = json.loads(json_url.text)
        # print(data)

        events = []
        for event in data:
            # print(event["EventId"])
            events.append(event["EventId"])
            # event_id = event["EventId"]
        # print(events)

        events_2020 = []
        for event_id in events:
            event_url = f"https://api.sportsdata.io/v3/mma/scores/json/Event/{event_id}"
            event_headers = {'Ocp-Apim-Subscription-Key': '6a440b2acb3d45bcae299abb9813839c'}
            json_event = requests.get(event_url, headers=event_headers)
            event_data = json.loads(json_event.text)
            # print(event_data)
            events_2020.append(event_data)
            # print(len(events_2020))
                  
        # print(len(events_2020))
        
        try:
            events_2020 = events_2020
        except:
            events_2020 = None

        self.fighter_stat = events_2020
        return events_2020

    # Dump File Method
    def dump(self):
        if self.fighter_stat is None:
            return

        fighter_title = "Events_2020" # TODO: get fighter name from data
        fighter_title = fighter_title.replace(" ","_").lower()
        file_name = fighter_title + ".json"
        with open(file_name, 'w') as f:
            json.dump(self.fighter_stat, f, indent=4)

        print("file dumped")
