from fighters_stat import FightersStatistics

# API_KEY = '6a440b2acb3d45bcae299abb9813839c'
# fighter_id = ""

fs = FightersStatistics()
# fs.get_events_2020()
# fs.get_fighters_list_stat()
fs.get_fights_by_fighterId()
fs.dump()