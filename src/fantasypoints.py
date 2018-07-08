import os
import json


matches = os.listdir("matches")

players = {}
count = 0
for mid in matches:
    count+=1
    print(count, mid)
    with open("matches/"+mid,"r") as f:
        data = json.load(f)

    if "dire_team" in data:
        dire = data["dire_team"]["team_id"]
    else:
        dire = -1
    if "radiant_team" in data:
        radiant = data["radiant_team"]["team_id"]
    else:
        radiant = -1
        
    for index in range(len(data["players"])):
        i = data["players"][index]
        id = i["account_id"]
        if id not in players:
            players[id] = { "fantasy_points":{} }
            players[id]["fantasy_points"]["kill_points"] = 0
            players[id]["fantasy_points"]["death_points"] = 0
            players[id]["fantasy_points"]["LHD_points"] = 0
            players[id]["fantasy_points"]["tower_points"] = 0
            players[id]["fantasy_points"]["roshan_points"] = 0
            players[id]["fantasy_points"]["teamfight_points"] = 0
            players[id]["fantasy_points"]["wards_points"] = 0
            players[id]["fantasy_points"]["camp_points"] = 0
            players[id]["fantasy_points"]["rune_points"] = 0
            players[id]["fantasy_points"]["fb_points"] = 0
            players[id]["fantasy_points"]["stun_points"] = 0
            players[id]["total_matches"] = 0
            players[id]["teams"] = set()
            players[id]["names"] = set()

        players[id]["fantasy_points"]["kill_points"] += i["kills"]*0.3
        players[id]["fantasy_points"]["death_points"] += (3 - (i["deaths"]*0.3))
        players[id]["fantasy_points"]["LHD_points"] += 0.003* (i["last_hits"] + i["denies"])
        players[id]["fantasy_points"]["tower_points"] += i["towers_killed"]
        players[id]["fantasy_points"]["roshan_points"] += i["roshans_killed"]
        players[id]["fantasy_points"]["teamfight_points"] += i["teamfight_participation"]*3
        players[id]["fantasy_points"]["wards_points"] += i["obs_placed"]*0.5
        players[id]["fantasy_points"]["camp_points"] += i["camps_stacked"]*0.5
        players[id]["fantasy_points"]["rune_points"] += i["rune_pickups"]*0.25
        players[id]["fantasy_points"]["fb_points"] += i["firstblood_claimed"]
        players[id]["fantasy_points"]["stun_points"] += i["stuns"]
        players[id]["names"].add(i["name"])

        if index<=4:
            players[id]["teams"].add(radiant)
        else:
            players[id]["teams"].add(dire)

with open("players.json","w") as f:
    json.dump(players,f)

