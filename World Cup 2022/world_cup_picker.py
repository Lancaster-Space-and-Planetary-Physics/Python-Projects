# === World Cup Picker.py ======================================================
# A script to assign random 2022 world cup teams to a list of names. Teams are
# weighted by current world ranking, and each name is assigned a spread of
# ranked teams. Rankings taken from:
# https://www.sportingnews.com/uk/soccer/news/fifa-rankings-world-cup-teams
# -updated-calculated/mxphm9f5h9j81ti9rkhvnqhc

# TO DO:
# - webscrape FIFA World Cup Groups and Rankings

# UPDATED 22 Nov 2022: Elliott added ability to input any number of players.
# Uneven number of team allocations must come randomly from lower rank teams.
# e.g. if someone has 3 teams, versus everyone else having 2, it must be a
# lower-ranked extra.

# === Joe Kinrade / Elliott Day - 18 Nov 2022 ==================================
import numpy as np
import time

# --- Pool of 32 FIFA World cup teams ------------------------------------------
n_teams = 32
# 2022 Groups:
teams = np.array([
         'quatar','ecuador','senegal','netherlands',    # group A
		 'england','iran','usa','wales',                # group B
		 'argentina','saudi arabia','mexico','poland',  # group C
		 'france','australia','denmark','tunisia',	    # group D
		 'spain','costa rica','germany','japan',	    # group E
		 'belgium','canada','morocco','croatia',	    # group F
		 'brazil','serbia','switzerland','cameroon',    # group G
		 'portugal','ghana','uruguay','south korea'])	# group H
# 2022 FIFA rankings:
rankings = [50,44,18,8,                                 # group A
		    5,20,16,19,									# group B
		    3,51,13,9,								    # group C
		    4,38,10,30,								    # group D
		    7,31,11,24,									# group E
		    2,41,22,12,								    # group F
		    1,21,15,43,								    # group G
		    9,61,14,28]								    # group H

#  --- Players in the hat ------------------------------------------------------
players = ['ade','cameron','diego','elliott','george','hannah','joe','maria']
n_players = len(players)

# Enable seed to reproduce a fixed run.
# np.random.seed(0)

#  --- Sort teams into pools by world ranking ----------------------------------
n_pools = int(n_teams / n_players)			# 32 teams / n players  = x ranked pools
remain = n_teams % n_players                # number of teams left after filling pools
teams_ranked = teams[np.argsort(rankings)]	# list of teams sorted by ranking

#create array of pools (excluding spare teams)
pools = np.empty([n_pools,n_players], dtype="U12")
for i in range(n_pools):                    # row 0 = top teams, row_n = worst teams
    pools[i] = teams_ranked[i*n_players:(i+1)*n_players]
ranks = np.reshape(np.arange(n_pools*n_players), [n_pools,n_players])

# --- Fill a names x teams array (n_pools, n_players) by selecting random teams from each tier
draft_teams = np.empty([n_pools,n_players], dtype='U12')
draft_ranks = np.empty([n_pools,n_players], dtype=int)

for i in range(0,n_pools):                  # loop over each tier 1-n_pools
    randoms = np.random.rand(n_players)	    # n_player random numbers between 0-1
    rand_ind = np.argsort(randoms)          # index that would sort these random ints
    draft_teams[i,:] = pools[i,rand_ind]    # assign random teams from current tier
    draft_ranks[i,:] = ranks[i,rand_ind]    # and assign ranks for those teams

# --- Create sweepstake --------------------------------------------------------
sweep_teams = dict()
sweep_ranks = dict()                                   # tally world rankings
for i, player in enumerate(players):
    sweep_teams[player] = list(draft_teams[:,i])       # assign teams to player
    sweep_ranks[player] = np.sum(draft_ranks[:,i])     # cumulative rankings assigned to player

# --- assign remaining teams to players with highest cumulative rankings -------
player_rankings = np.array([sweep_ranks[player] for player in sweep_ranks.keys()]) # ranks assigned to players
player_names = np.array([player for player in sweep_ranks.keys()])                 # names assigned to those ranks
rank_order = np.argsort(player_rankings)                                           # get order of ranking
player_names = player_names[rank_order]                                            # order players by cumulative ranking
for i in range(1, remain+1):
    sweep_teams[player_names[-i]].append(teams_ranked[-i])                         # assign extra teams to players with worst cumulative ranking

# --- Print result to screen ---------------------------------------------------
print('Connecting to HEC...')
time.sleep(1)
print('Connection established.')
print('Allocating processors...')
time.sleep(1)
print('Running sweep sequence...')

for player in sweep_teams.keys():
    print(player)
    print("-----")
    time.sleep(2)
    player_teams = sweep_teams[player]
    for team in player_teams:
        time.sleep(2)
        print(team)
    print("\n")

print('Closing connection...')
time.sleep(1)
print('Session ended. Thank you for using HEC. Have a nice day.')
