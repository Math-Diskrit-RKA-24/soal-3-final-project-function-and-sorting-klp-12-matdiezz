PlayerList = []
def initPlayers():
    global PlayerList 
    PlayerList= []

def createNewPlayer(name, damage=0, defensePower=0):
    return{
        "name":name,
        "score":0,
        "damage":damage,
        "health":100,
        "defensePower":defensePower,
        "defense":False
    }
        

def addPlayer(player):
    global PlayerList
    PlayerList.append(player)

def removePlayer(name):
    global PlayerList
    for i in PlayerList:
        if i['name']==name:
            PlayerList.remove(i)
            return
    print("There is no player with that name!")

        
def setPlayer(player, key, value):
    if key in player:
        player[key]=value

def attackPlayer(attacker:dict, target:dict):
    if target["defense"]:
        dReceive= max(0, attacker["damage"] - target["defensePower"]) #serangan penyerang-pertahanan korban
    else:
        dReceive= attacker["damage"]

    setPlayer(target, "health", target["health"] - dReceive)
    setPlayer(attacker, "score", attacker["score"] + dReceive)
    setPlayer(target, "defense", False)
    
def displayMatchResult():
    sorted_players= sorted(PlayerList, key=lambda p: (p["score"], p["health"]), reverse=True)
    print("\nMatch Results:")
    print(f"{'Rank':<5}|{'Name':<14}|{'Score':<10}|{'Health'}")
    for rank, player in enumerate(sorted_players, start=1):
        print(f"{rank:<5}|{player['name']:<14}|{player['score']:<10}|{player['health']}")
