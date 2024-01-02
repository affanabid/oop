class Player:
    def __init__(self, name,age, team, role1='No',role2='No',role3='No'):
        self.name = name
        self.age = age
        self.team = team
        self.role1 = role1
        self.role2 = role2
        self.role3 = role3

    def display_player_info(self):
        x=f"Player Name: {self.name}\nAge: {self.age}\nTeam: {self.team}\nRole: "
        r=[]
        if self.role1.lower()=='yes':
            r.append('batsman')
        if self.role2.lower()=='yes':
            r.append('bowler')
        if self.role3.lower()=='yes':
            r.append('wicket keeper') 
        r4="\\".join(r)   
        x+=r4
        return x

class Points:
    def __init__(self , team_name , matches_played , won , lost):
        if any(val < 0 for val in [matches_played, won, lost]):
            raise ValueError("Number of matches, wins, losses, and draws must be non-negative.")
        self.team_name = team_name
        self.matches_played = matches_played
        self.won = won
        self.lost = lost       
        self.points = self.won * 2
    
    def __str__(self):
        header = f"{'Team Name':<15}{'Matches Played':<20}{'Won':<10}{'Lost':<10}{'Points':<10}"
        data = f"{self.team_name:<15}{self.matches_played:<20}{self.won:<10}{self.lost:<10}{self.points:<10}"
        return f'{header} \n {data}'

class Team:
    def __init__(self , team_name ,id, captain_name ,vc, coach_name , points):
        self.id = id
        self.team_name = team_name
        self.captain_name = captain_name
        self.vice_captain=vc
        self.coach_name = coach_name
        self.team_points = points
    def __str__(self):
        return f'Team ID: {self.id}\nTeam Name: {self.team_name}\nCaptain: {self.captain_name}\nVice Captain: {self.vice_captain}\nCoach: {self.coach_name}'
    def display_teams(self):
        if self.team_name=='NewZealand':
            return 'New Zealand'
        elif self.team_name=='SriLanka':
            return 'Sri Lanka'
        return self.team_name
            
class Match:
    def __init__(self , match_no ,team1,team2,date, overs , winner,loser ):
        self.date = date
        self.match_no = match_no
        self.team1=team1
        self.team2=team2
        self.overs = overs
        self.winner = winner
        self.loser = loser
    def __str__(self):
        return f'Date: {self.date }\nMatch Number: {self.match_no}\nTeams: {self.team1} v/s {self.team2}\nOvers: {self.overs}\nWinner:{self.winner}'


if __name__=="__main__":
    player1 = Player("Virat Kohli", 33, "India", "Yes",'No','No')

    print(player1.display_player_info())
    print()

    
