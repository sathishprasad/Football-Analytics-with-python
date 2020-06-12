# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 00:48:23 2020

@author: Sathish
"""
from Pitch import createPitch
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy  as np

                
match_id=7576   #match_id according to statsbomb
file_name=str(match_id)+'.json'  #converting the id to a string with .json extenstion

with open('E:/Statsbomb/data/events/7576.json') as m:
    data=json.load(m)

train_data=pd.io.json.json_normalize(data,sep='_').assign(match_id = file_name[:-5])

fig,ax=createPitch(120,80,'white','green')

pitchWidthY=80
pitchLengthX=120
home_team_required='Portugal'
away_team_required='Spain'
req_player='Cristiano Ronaldo dos Santos Aveiro'


shots = train_data.loc[train_data['type_name'] == 'Shot'].set_index('id') #creating a separate df for shots

for i,shot in shots.iterrows():  #iterating each row of shots
    x=shot['location'][0]
    y=shot['location'][1]
    
    goal=shot['shot_outcome_name']=='Goal'
    Saved=shot['shot_outcome_name']=='Saved'
    Blocked=shot['shot_outcome_name']=='Blocked'
    OffTarget=shot['shot_outcome_name']=='Off T'
    team_name=shot['team_name']
    player_name=shot['player_name']
    
    #circleSize=2
    circleSize=np.sqrt(shot['shot_statsbomb_xg']*15)

    if (team_name==home_team_required):
        if goal:
            if(player_name==req_player):
              shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
              #plt.text((x+1),pitchWidthY-y+1,shot['player_name']) 
              ax.add_patch(shotCircle)
        elif Saved:
          if(player_name==req_player):
              shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="black")     
              #shotCircle.set_alpha(.2)
              ax.add_patch(shotCircle)
        elif Blocked:
          if(player_name==req_player):
              shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="blue")     
              #shotCircle.set_alpha(.2)
              ax.add_patch(shotCircle)
        elif OffTarget:
          if(player_name==req_player):
              shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="purple")     
              #shotCircle.set_alpha(.2)
              ax.add_patch(shotCircle)
        else:
          if(player_name==req_player):
              shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="yellow")     
              #shotCircle.set_alpha(.2)
              ax.add_patch(shotCircle)
              

fig.set_size_inches(18,12)



