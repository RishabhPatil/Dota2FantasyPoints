import requests
import json
import os

matches = os.listdir("matches")
for i in range(len(matches)):
    matches[i] = int(matches[i])
print(len(matches))

def get_match_data(match_id):
    if match_id in matches:
        print(match_id+" exists.")
        return
    else:
        r = requests.get("https://api.opendota.com/api/matches/"+str(match_id))
        result = r.json()
        with open("matches/"+str(match_id),"w+") as f:
            json.dump(result, f)

if __name__=="__main__":
    with open("result.json","r") as f:
        data = json.load(f)

    print(len(data["match_list"]))
    new_set = set(data["match_list"]) - set(matches)
    print(len(new_set))
    for match in new_set:
        print(match)
        get_match_data(match)
    