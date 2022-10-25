import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)


# Read csv files into pandas dataframe. The most important datasets to get started seem like
# games.csv, players.csv and plays.csv.
game_data = pd.read_csv('nfl-big-data-bowl-2023/games.csv')

players_data = pd.read_csv('nfl-big-data-bowl-2023/players.csv')

plays_data = pd.read_csv('nfl-big-data-bowl-2023/plays.csv')

# To start, we probably want to get all unique team codes from game_data.  This way
# we can parse players_data and plays_data by team
# print(game_data.columns)
# Columns of game_data: 'gameId', 'season', 'week', 'gameDate', 'gameTimeEastern', 'homeTeamAbbr', 'visitorTeamAbbr'
team_abbr = game_data['homeTeamAbbr'].unique()
print('Teams: ', team_abbr, '\n', 'Team Count: {}'.format(len(team_abbr)))

# Now that we have our list of team name abbreviations, we can pull data from the other datasets.
# To start, we'll get a list of players involved in plays for each team
pick_team = 'CIN'

# Created dataframes containing all defensive and offensive plays for a given team
team_def_plays = plays_data[plays_data['defensiveTeam'] == 'CIN']
team_off_plays = plays_data[plays_data['possessionTeam'] == 'CIN']

# Sort best plays
print(plays_data['playResult'].head)

plays_sorted = plays_data.sort_values(by=['playResult'], ascending=False)
print(team_off_plays.sort_values(by=['playResult'], ascending=False).head)
# yuhhhh