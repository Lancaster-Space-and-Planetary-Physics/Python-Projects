# === World Cup Picker.py ======================================================
# A script to assign random 2022 world cup teams to a list of names. Teams are
# weighted by current world ranking, and each name is assigned a spread of
# ranked teams. Rankings taken from:
# https://www.sportingnews.com/uk/soccer/news/fifa-rankings-world-cup-teams
# -updated-calculated/mxphm9f5h9j81ti9rkhvnqhc

# TO DO:
# - webscrape FIFA World Cup Groups and Rankings
# - adapt this for any number of players (up to 32). Uneven number of team
#   allocations must come randomly from lower pool teams. i.e. if someone has 3
#   teams, versus everyone else having 2, it must be a lower-ranked extra team.

# === Joe Kinrade - 18 Nov 2022 ================================================
import numpy as np

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

#  --- Players in the hat (must be 8 at the moment) ----------------------------
players = ['joe','diego','elliott','george','cameron','hannah','maria','yan']
n_players = int(len(players))

#  --- Sort teams into pools by world ranking ----------------------------------
n_pools = int(n_teams / n_players)			# 32 teams / 8 players  = 4 ranked pools
teams_ranked = teams[np.argsort(rankings)]	# list of teams sorted by ranking

gold =   teams_ranked[0:8]                  # Gold pool
silver = teams_ranked[8:16]                 # Silver pool
bronze = teams_ranked[16:24]                # Bronze pool
poop =   teams_ranked[24:32]                # Poop pool

pools = np.vstack([gold,silver,bronze,poop])

# --- Fill a names x teams array (8x4) by selecting random teams from each tier
draft = np.empty([n_pools,n_players], dtype='S20')

for i in range(0,4):                         # loop over each tier 1-4
    randoms = np.random.rand(8)			     # 8 random numbers between 0-1
    rand_ind = list(np.argsort(randoms))     # index that would sort these random ints
    draft[i,:] = pools[i,rand_ind]		     # assign random teams from current tier

# --- Print result to screen ---------------------------------------------------
picks = np.vstack([players,draft]).T
[print(*line) for line in picks]
