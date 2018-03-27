import json
import os
import sys

# CONCATENATES THE JSON IN FOLDER JSONS

# # ==== SET UP FOR JSON
finalJson = "finalJson.json"

resetJSON = {}
resetJSON["data "] = [[],[],[],[],[]]

#====WRITE JSON======
with open(finalJson, "w") as f:
    json.dump(resetJSON, f)


for filename in os.listdir("JSONs"):

    if filename.endswith(".json"): 

        print(filename + ".... adding to finalJson")

        #====OPEN JSON READING FROM======
        with open("JSONs/" + filename) as f:
            abnormalReturnsPerGroup = json.load(f)

        #====OPEN JSON READING TO======
        with open(finalJson) as f:
            abnormalReturnsPerGroupADDED = json.load(f)

        for i in range(0,5):
        	abnormalReturnsPerGroupADDED['data '][i] = abnormalReturnsPerGroupADDED['data '][i] + abnormalReturnsPerGroup['data '][i]

        #====WRITE JSON======
        with open(finalJson, "w") as f:
            json.dump(abnormalReturnsPerGroupADDED, f)

