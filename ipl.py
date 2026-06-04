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

print(teamsApi())