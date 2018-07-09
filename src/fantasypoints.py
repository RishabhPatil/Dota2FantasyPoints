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

        if None in [i["towers_killed"],i["roshans_killed"],i["teamfight_participation"],i["obs_placed"],i["camps_stacked"],i["rune_pickups"],i["firstblood_claimed"],i["stuns"]]:
            continue

        id = i["account_id"]
        if id not in players:
            players[id] = { "fantasy_points":{} }
            players[id]["fantasy_points"]["kill_points"] = float(0)
            players[id]["fantasy_points"]["death_points"] = float(0)
            players[id]["fantasy_points"]["LHD_points"] = float(0)
            players[id]["fantasy_points"]["tower_points"] = float(0)
            players[id]["fantasy_points"]["roshan_points"] = float(0)
            players[id]["fantasy_points"]["teamfight_points"] = float(0)
            players[id]["fantasy_points"]["wards_points"] = float(0)
            players[id]["fantasy_points"]["camp_points"] = float(0)
            players[id]["fantasy_points"]["rune_points"] = float(0)
            players[id]["fantasy_points"]["fb_points"] = float(0)
            players[id]["fantasy_points"]["stun_points"] = float(0)
            players[id]["total_matches"] = 0
            players[id]["teams"] = []
            players[id]["names"] = []

        players[id]["fantasy_points"]["kill_points"] += i["kills"]*0.3
        players[id]["fantasy_points"]["death_points"] += (3 - (i["deaths"]*0.3))
        players[id]["fantasy_points"]["LHD_points"] += 0.003* (i["last_hits"] + i["denies"])
        if i["towers_killed"] is not None:
            players[id]["fantasy_points"]["tower_points"] += i["towers_killed"]
        if i["roshans_killed"] is not None:
            players[id]["fantasy_points"]["roshan_points"] += i["roshans_killed"]
        if i["teamfight_participation"] is not None:
            players[id]["fantasy_points"]["teamfight_points"] += i["teamfight_participation"]*3
        if i["obs_placed"] is not None:
            players[id]["fantasy_points"]["wards_points"] += i["obs_placed"]*0.5
        if i["camps_stacked"] is not None:
            players[id]["fantasy_points"]["camp_points"] += i["camps_stacked"]*0.5
        if i["rune_pickups"] is not None:
            players[id]["fantasy_points"]["rune_points"] += i["rune_pickups"]*0.25
        if i["firstblood_claimed"] is not None:
            players[id]["fantasy_points"]["fb_points"] += i["firstblood_claimed"]
        if i["stuns"] is not None:
            players[id]["fantasy_points"]["stun_points"] += i["stuns"]
        if i["name"] not in players[id]["names"]:
            players[id]["names"].append(i["name"])
        players[id]["total_matches"] += 1
        if index<=4:
            if radiant not in players[id]["teams"]: 
                players[id]["teams"].append(radiant)
        else:
            if dire not in players[id]["teams"]:
                players[id]["teams"].append(dire)

with open("players.json","w") as f:
    json.dump(players,f)

