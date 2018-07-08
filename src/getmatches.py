import os
import requests
import time
import json
import time
x = time.time()
def process_list(result, after_timestamp, more_than_match_id):
    match_ids = []
    for match in result:
        if match['start_time'] > after_timestamp and match['match_id']>more_than_match_id:
            match_ids.append(match["match_id"])
    global match_list
    match_list = match_list + match_ids
    if match_ids:
        return 1, min(match_ids)
    else:
        return 0, 0

def get_matches(less_than_match_id=99999999999, more_than_match_id=0, after_timestamp=0):
    if more_than_match_id > less_than_match_id:
        print("Invalid Parameters")
        return
    
    flag = 1
    while flag:
        r = requests.get("https://api.opendota.com/api/proMatches",params = {"less_than_match_id": less_than_match_id} )
        result = r.json()
        flag, less_than_match_id = process_list(result, after_timestamp, more_than_match_id)

if __name__=="__main__":

    if "config.json" in os.listdir():
        with open("config.json","r") as f:
            config = json.loads(f)
    else:
        config = {"last_match":''}

    match_list = []
    get_matches(99999999999,0,1504224000)
    with open("result.json","w") as f:
        json.dump({"match_list":match_list},f)
    print(time.time()-x)