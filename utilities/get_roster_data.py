import nfl_data_py as nfl
import pandas as pd



def get_roster_info(years: list, dest_dir: str):
    """
    Method to return a DataFrame for Roster data for the given years provided.

    The DataFrame is then split per team and the corresponding DataFrames are currently saved as CSV files into the specified dest_dir and named as according to the team and year.

    Args:
        years (list): list of nums for years of data wanting to be returned
        dest_dir (str): destination directory of where to save the CSV files produced to
    """
    roster_info = nfl.import_seasonal_rosters(years)

    roster_info_df = pd.DataFrame(roster_info)
    
    for (team, season), team_df in roster_info_df.groupby(['team', 'season']):
        team_df.to_csv(f'{dest_dir}/{team}_{season}.csv')

    print(f'Roster Per Team Uploaded to Google Sheets For Years: {years}')
