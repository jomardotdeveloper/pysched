import json
from tabulate import tabulate

vessels = json.load(open('vessels.json'))

MANILA_BERTH = [
    {
        "name": "Manila Berth 1",
        "capacity": 3,
        "length" : 420,
        "num" : 0
    },
    {
        "name": "Manila Berth 2",
        "capacity": 2,
        "length" : 270,
        "num" : 0
    },
    {
        "name": "Manila Berth 3",
        "capacity": 2,
        "length" : 270,
        "num" : 0
    },
    {
        "name": "Manila Berth 4",
        "capacity": 2,
        "length" : 95,
        "num" : 0
    },
    {
        "name": "Manila Berth 5",
        "capacity": 3,
        "length" : 420,
        "num" : 0
    },
]

results = []



def get_service_time(vessel):
    if vessel.get("tonnage") < 5000:
        return 3
    elif vessel.get("tonnage") > 5000 and vessel.get("tonnage") <= 8000:
        return 5
    elif vessel.get("tonnage") > 8000 and vessel.get("tonnage") <= 16000:
        return 6
    elif vessel.get("tonnage") > 16000 and vessel.get("tonnage") <= 20000:
        return 7

    return 0

def reset_berth():
    for berth in MANILA_BERTH:
        berth["num"] = 0

def get_berth(vessel):
    for berth in MANILA_BERTH:
        if vessel.get("length") <= berth.get("length") and berth.get("num") < berth.get("capacity"):
            return berth

    return None

def berth_is_taken(berth):
    pass

time = 0
last_execute_time = 0

for vessel in vessels:
    #ASSUMING THAT VESSELS ARRIVE IN ORDER
    arrival_time = 0 if vessel.get("name") == 1 else vessel.get("name")
    service_time = get_service_time(vessel)
    available_bert = get_berth(vessel)

    if available_bert:
        result = {
            "vessel_no" : vessel.get("name"),
            "actual_start" : time,
            "waiting_time" :  time - arrival_time,
            "service_time" : service_time,
            "berth" : available_bert.get("name"),
        }
        available_bert["num"] += 1
    else:
        result = {
            "vessel_no" : vessel.get("name"),
            "actual_start" : time,
            "waiting_time" :  time - arrival_time,
            "service_time" : service_time,
            "berth" : "Anchorage",
        }


        

    time += service_time
    
    results.append(result)

reset_berth()

        
        
for result in results:
    print(tabulate([result.values()], headers=result.keys(), tablefmt="grid"))









