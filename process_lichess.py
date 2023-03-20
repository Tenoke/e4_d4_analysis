import pickle

path = 'path-to-lichess-file-run-twice-for-both-years'

players_e4 = {"blitz":{}, 'rapid':{}}
players_d4 = {"blitz":{}, 'rapid':{}}
players_elo = {"blitz":{}, 'rapid':{}}
current_game = None # for seeking new game
player = None
elo = None
with open(path, 'r') as f:
        while True:
            line = f.readline()
            if not current_game:
                if 'Rated' in line and 'tournament' not in line:
                    if 'Blitz' in line:
                        current_game = 'blitz'
                    if 'Rapid' in line:
                        current_game = 'rapid'
            else:
                if "[White " in line:
                    player = line.split('"')[1]
                elif "[WhiteElo" in line:
                    elo = line.split('"')[1]
                elif '1. e4' in line:
                    players_e4[current_game][player] =  players_e4[current_game].get(player, 0) + 1
                    players_elo[current_game][player] = elo
                    current_game = None # for seeking new game
                    player = None
                    elo = None
                elif '1. d4' in line:
                    players_d4[current_game][player] =  players_d4[current_game].get(player, 0) + 1
                    players_elo[current_game][player] = elo
                    current_game = None # for seeking new game
                    player = None
                    elo = None
            if not line:
                break
        
with open('lichess_data-23-01', 'wb') as f:
    pickle.dump([players_e4, players_d4, players_elo], f)
    

