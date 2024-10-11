import nfl_data_py as nfl
import pandas as pd 

def get_pbp_data(years: list):
    pbp_df = pd.DataFrame(nfl.import_pbp_data(years))

    

    return pbp_df

def get_pbp_data_team(years: list, teams: list):
    all_teams_pbp_data = get_pbp_data(years)

    teams_pbp_df = all_teams_pbp_data[
        all_teams_pbp_data['home_team'].isin(teams) | all_teams_pbp_data['away_team'].isin(teams)
    ]

    return teams_pbp_df