import numpy as np 
import pandas as pd 

file_id = "15PqRueu4DrKvp17dQODeOMm5iGjyP46B"
url = f"https://drive.google.com/uc?id={file_id}" 

matches = pd.read_csv(url)

#print(matches.head())
def teamsApi():
    new_df = list(pd.concat([matches['team1'],matches['team2']],ignore_index=True).unique())
    teams_dict = {
        'teams' : new_df
    }
    return teams_dict

def teamVteam(Team1,Team2):

    valid_teams = list(pd.concat([matches['team1'],matches['team2']],ignore_index=True).unique())

    if (Team1 in valid_teams) & (Team2 in valid_teams):    
        temp_df = matches[((matches['team1'] == Team1) & (matches['team2'] == Team2)) | ((matches['team1'] == Team2) & (matches['team2'] == Team1))] 
        total_matches = len(temp_df)
        team1 = temp_df['winner'].value_counts()[Team1]
        team2 = temp_df['winner'].value_counts()[Team2]
        draws = total_matches - (team1+team2)

        respone = {
            'Total_matches' : total_matches,
            Team1 : team1.item(), 
            Team2 : team2.item(), 
            'Draws' : draws.item()
        }
        return respone
    else:
        return{"Message" : "Invalid team names"}