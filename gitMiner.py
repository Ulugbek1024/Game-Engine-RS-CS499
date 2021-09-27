import requests
import os
from pprint import pprint

#token access for GITHUB
token = os.getenv('GITHUB_TOKEN', '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')
#Unity Games Dictionary
unity = {1: 'YarnSpinnerTool/YarnSpinner', 2: "BayatGames/RedRunner", 3: "nvjob/Infinity-Square-Space", 4: "roydejong/chromium-unity-server",
         5: "bugsnag/bugsnag-unity", 6: "dgkanatsios/AzureServicesForUnity", 7: "codinanon/RenaissanceCoders_UnityScripting",
         8: "northwood-studios/SCPSL-Translations", 9: "Kidel/DynamicResolution-for-Unity3D", 10: "dmitmel/tienk.io",
         11: "dbpienkowska/bloxyz", 12: "pale-cinder/hover-racer-training", 13: "darealshinji/UnityEngine2deb", 14: "AnimaRain / ShootAR",
         15: "codinanon / ZigZagClone"}
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

