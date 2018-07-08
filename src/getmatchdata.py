import requests
import json
import os
import time

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
        if "error" in result and result["error"]=="rate limit exceeded":
            return 1
        elif "error" in result:
            print(result)
            exit()
        with open("matches/"+str(match_id),"w+") as f:
            json.dump(result, f)
        return 1

if __name__=="__main__":
    with open("result.json","r") as f:
        data = json.load(f)

    print(len(data["match_list"]))
    new_set = set(data["match_list"]) - set(matches)
    print(len(new_set))
    count = 0
    for match in new_set:
        error = -1
        count+=1
        print(count,match)
        while error==-1:
            error = get_match_data(match)
            if error==-1:
                time.sleep(10)