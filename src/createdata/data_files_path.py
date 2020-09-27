import os
from pathlib import Path

BASE_PATH = Path(os.getcwd()).parents[0] / "data"
EVENT_AND_FIGHT_LINKS_PICKLE_PATH = BASE_PATH / "event_and_fight_links.pickle"
PAST_EVENT_LINKS_PICKLE_PATH = BASE_PATH / "past_event_links.pickle"
NEW_EVENT_AND_FIGHTS = BASE_PATH / "new_fight_data.csv"
TOTAL_EVENT_AND_FIGHTS = BASE_PATH / "total_fight_data.csv"
PREPROCESSED_DATA = BASE_PATH / "preprocessed_data.csv"
FIGHTER_DETAILS = BASE_PATH / "fighter_details.csv"
UFC_DATA = BASE_PATH / "data.csv"
