import requests
import os
from pprint import pprint

#token access for GITHUB
token = os.getenv('GITHUB_TOKEN', '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')
#Unity Games Dictionary
unity = {1: 'YarnSpinnerTool/YarnSpinner', 2: "BayatGames/RedRunner", 3: "nvjob/Infinity-Square-Space", 4: "roydejong/chromium-unity-server",
         5: "bugsnag/bugsnag-unity", 6: "dgkanatsios/AzureServicesForUnity", 7: "codinanon/RenaissanceCoders_UnityScripting",
         8: "northwood-studios/SCPSL-Translations", 9: "Kidel/DynamicResolution-for-Unity3D", 10: "dmitmel/tienk.io",
         11: "dbpienkowska/bloxyz", 12: "pale-cinder/hover-racer-training", 13: "darealshinji/UnityEngine2deb", 14: "AnimaRain/ShootAR",
         15: "codinanon/ZigZagClone"}
gamemakerStudio = {1: "YellowAfterlife/GMEdit", 2: "JujuAdams/Scribble", 3: "VacaRoxa/gamedev4noobs", 4: "gm-core/gdash",
                   5: "evolutionleo/GM-Online-Framework", 6: "bscotch/stitch", 7: "sohomsahaun/SnowState", 8: "borup3/Lighting-System-2D",
                   9: "JujuAdams/input_legacy", 10: "JujuAdams/SNAP", 11: "johnwdubois/rezonator", 12: "niksudan/gms2-destructible-terrain",
                   13: "JujuAdams/dotobj", 14: "JujuAdams/DoLater", 15: "DragoniteSpam/Emu"}
#for loop to access Unity Dictionary
print("\n UNITY GAMES: ")
for i in range(1, len(unity) + 1):
    #exception handler for repositories that don't have parameters we are looking for
    repo = unity[i]
    try:
        query_url = f"https://api.github.com/repos/{repo}"
        headers = {'Authorization': f'token {token}'}
        r = requests.get(query_url, params='')
        data = (r.json())
        print("\nGame: " + repo)
        print("Description: " + str(data['description']))
        print("Language Used: " + str(data['language']))
        print("Number of Open Issues: " + str(data['open_issues']))
        print("Watchers Count: " + str(data['watchers_count']))
    except KeyError:
        print("No info found")

print("\n GameMaker Studio 2: ")
for j in range(1, len(gamemakerStudio) + 1):
    #exception handler for repositories that don't have parameters we are looking for
    repo = gamemakerStudio[j]
    try:
        query_url = f"https://api.github.com/repos/{repo}"
        headers = {'Authorization': f'token {token}'}
        r = requests.get(query_url, params='')
        data = (r.json())
        print("\nGame: " + repo)
        print("Description: " + str(data['description']))
        print("Language Used: " + str(data['language']))
        print("Number of Open Issues: " + str(data['open_issues']))
        print("Watchers Count: " + str(data['watchers_count']))
    except KeyError:
        print("No info found")
