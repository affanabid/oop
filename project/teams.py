class Points:
    def __init__(self , team_name , matches_played , won , lost , draw):

        if any(val < 0 for val in [matches_played, won, lost, draw]):
            raise ValueError("Number of matches, wins, losses, and draws must be non-negative.")
        
        self.team_name = team_name
        self.matches_played = matches_played
        self.won = won
        self.lost = lost
        self.draw = draw
        self.points = self.won * 2


    def __str__(self):
        header = f"{'Team Name':<15}{'Matches Played':<20}{'Won':<10}{'Lost':<10}{'Draw':<10}{'Points':<10}"
        data = f"{self.team_name:<15}{self.matches_played:<20}{self.won:<10}{self.lost:<10}{self.draw:<10}{self.points:<10}"

        return f'{header} \n {data}'
    


class Team:
    def __init__(self , id , team_name , captain_name , coach_name , team_points):
        self.id = id
        self.team_name = team_name
        self.captain_name = captain_name
        self.coach_name = coach_name
        self.team_points = Points(*team_points)


    def __str__(self):
        return f'Team ID: {self.id}\nTeam Name: {self.team_name}\nCaptain: {self.captain_name}\nCoach: {self.coach_name}'

    def point_details(self):
        return self.team_points.__str__()

team_points =  'RCB' ,4,3,1,0
obj = Team(6 , 'RCB' , 'AD Deviliers' , 'Ravi Shastri' , team_points )
print(obj)
print(obj.point_details())
        


class Result:
    def __init__(self ,team1 , team2 , team1_final_score , team2_final_score):
        self.team1 = team1
        self.team2 = team2
        self.team1_final_score = team1_final_score
        self.team2_final_score = team2_final_score
    
    def __str__(self):
        if self.team1_final_score > self.team2_final_score:
            final_score = self.team1_final_score - self.team2_final_score
            return f'{self.team1} won by {final_score} runs'
        else:
            final_score = self.team2_final_score - self.team1_final_score
            return f'{self.team2} won by {final_score} runs'
        

import random
class Toss():
    def perform_toss(self):
        # random.choice = always 2 arguments only 
        self.toss_result = random.choice(["Heads" , "Tails"])
        if self.toss_result == 'Heads':
            return f'{result.team1} won the toss'
        else:
            return f'{result.team2} won the toss'

class Match:
    def __init__(self , date , match_no , overs , match_type , result ):
        self.date = date
        self.match_no = match_no
        self.overs = overs
        self.match_type = match_type
        self.toss = Toss()
        self.result = result
        
    def __str__(self):
        return f'{self.match_type}\nDate: {self.date }\nMatch Number: {self.match_no}\nTeams: {self.result.team1} v/s {self.result.team2}\nOvers: {self.overs}'
    
    def match_result(self):
        return f'{self.toss.perform_toss()}\n{self.result.__str__()}'


result = Result('RCB', 'KKR' , 150 , 152)
obj = Match('10/02/2024',4 , 6 ,'Semi Finals' , result)
print(obj)
print(obj.match_result())
    

        