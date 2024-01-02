import tkinter as tk
from layer1 import*

def show_message(window, message):
    message_window = tk.Toplevel(window)
    message_window.title("Note")
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    half_width = screen_width // 4
    half_height = screen_height // 4

    x_position = (screen_width - half_width) // 2
    y_position = (screen_height - half_height) // 2

    message_window.geometry(f"{half_width}x{half_height}+{x_position}+{y_position}")

    message_label = tk.Label(message_window, text='Note:', padx=20, pady=10)
    message_label.pack()

    squad_label = tk.Label(message_window, text=message, padx=20, pady=10)
    squad_label.pack()

def display_squad(window, team_name):
    players = squad(team_name)
    print(players)
    if players:
        squad_window = tk.Toplevel(window)
        squad_window.title("Squad")
        players_label = tk.Label(squad_window, text='\n'.join(players), padx=20, pady=10)
        players_label.pack()
    else:
        show_message(window, 'Team not found!')

def standings(window):
    table = []

    played = 0
    won = 0
    lost = 0
    draw = 0
    team_name = 'Pakistan'
    with open('matches.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            line = content.strip()
            line = line.split()
            # print(line[5])
            if (line[5] != 'TBD' or line[6] != 'TBD') and line[1] == team_name or line[2] == team_name:
                search = True
                played += 1
                if line[5] == team_name:
                    won += 1
                elif line[6] == team_name:
                    lost += 1
                elif line[5] == 'draw' or line[6] == 'draw':
                    draw += 1
    points = (won * 2) + draw
    state = f'{team_name}\t{played}\t{won}\t{lost}\t{draw}\t{points}\n'
    table.append(state)

    played = 0
    won = 0
    lost = 0
    draw = 0
    team_name = 'India'
    with open('matches.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            line = content.strip()
            line = line.split()
            # print(line[5])
            if (line[5] != 'TBD' or line[6] != 'TBD') and line[1] == team_name or line[2] == team_name:
                search = True
                played += 1
                if line[5] == team_name:
                    won += 1
                elif line[6] == team_name:
                    lost += 1
                elif line[5] == 'draw' or line[6] == 'draw':
                    draw += 1
    points = (won * 2) + draw
    state = f'{team_name}\t\t{played}\t{won}\t{lost}\t{draw}\t{points}\n'
    table.append(state)

    played = 0
    won = 0
    lost = 0
    draw = 0
    team_name = 'Australia'
    with open('matches.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            line = content.strip()
            line = line.split()
            # print(line[5])
            if (line[5] != 'TBD' or line[6] != 'TBD') and line[1] == team_name or line[2] == team_name:
                search = True
                played += 1
                if line[5] == team_name:
                    won += 1
                elif line[6] == team_name:
                    lost += 1
                elif line[5] == 'draw' or line[6] == 'draw':
                    draw += 1
    points = (won * 2) + draw
    state = f'{team_name}\t{played}\t{won}\t{lost}\t{draw}\t{points}\n'
    table.append(state)

    played = 0
    won = 0
    lost = 0
    draw = 0
    team_name = 'SriLanka'
    with open('matches.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            line = content.strip()
            line = line.split()
            if (line[5] != 'TBD' or line[6] != 'TBD') and line[1] == team_name or line[2] == team_name:
                search = True
                played += 1
                if line[5] == team_name:
                    won += 1
                elif line[6] == team_name:
                    lost += 1
                elif line[5] == 'draw' or line[6] == 'draw':
                    draw += 1
    points = (won * 2) + draw
    state = f'{team_name}\t{played}\t{won}\t{lost}\t{draw}\t{points}\n'
    table.append(state)

    played = 0
    won = 0
    lost = 0
    draw = 0
    team_name = 'NewZealand'
    with open('matches.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            line = content.strip()
            line = line.split()
            if (line[5] != 'TBD' or line[6] != 'TBD') and line[1] == team_name or line[2] == team_name:
                search = True
                played += 1
                if line[5] == team_name:
                    won += 1
                elif line[6] == team_name:
                    lost += 1
                elif line[5] == 'draw' or line[6] == 'draw':
                    draw += 1
    points = (won * 2) + draw
    state = f'{team_name}\t{played}\t{won}\t{lost}\t{draw}\t{points}\n'
    table.append(state)
    new_table = []
    for row in table:
        row = row.split()
        new_table.append(row)
    sorted_table = sorted(new_table, key=lambda x: int(x[5]), reverse=True)
    for i in range(len(sorted_table)):
        for j in range(4):
            if sorted_table[i][j] == 'India':
                sorted_table[i][j] = 'India\t'

    heading = 'Team\t\tPlayed\tWon\tLost\tDraw\tPoints'
    lines = '-------------------------------------------------------'
    table = list(map('\t'.join, sorted_table))
    new_table = table[:]
    new_table.insert(0, heading)
    new_table.insert(1, lines)

    standings_window = tk.Toplevel(window)
    standings_window.title("Standings")
    label_font = ("Courier", 8)  
    players_label = tk.Label(standings_window, text='\n'.join(new_table), font=label_font, padx=20, pady=10, justify='left')
    players_label.pack(expand=True, fill=tk.BOTH)

def display_teams(window):
    teams = []
    with open('teams.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            team = content.split()
            x=Team(*team)
            teams.append(x.display_teams())
    if teams:
        squad_window = tk.Toplevel(window)
        squad_window.title("Teams")
        players_label = tk.Label(squad_window, text='\n'.join(teams), padx=20, pady=10, justify='left')
        players_label.pack()

def display_team(window,team1):
    team =''
    with open('teams.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            t = content.split()
            if team1==t[0]:
                x=Team(*t)
                team=x
    if team:
        squad_window = tk.Toplevel(window)
        squad_window.title("Team Info")
        players_label = tk.Label(squad_window, text=team, padx=20, pady=10, justify='left')
        players_label.pack()
        
def points(window, team_name):
    played = 0
    won = 0
    lost = 0
    draw = 0
    search = False
    with open('matches.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            line = content.strip()
            line = line.split()
            print(line[5])
            if (line[5] != 'TBD' or line[6] != 'TBD') and line[1] == team_name or line[2] == team_name:
                search = True
                played += 1
                if line[5] == team_name:
                    won += 1
                elif line[6] == team_name:
                    lost += 1
                elif line[5] == 'draw' or line[6] == 'draw':
                    draw += 1

    if search == True:
        points = won * 2
        display_points(window, points)
    elif search == False:
        show_message(window, 'Team not found!')
    # print(played)
    # print(won)
    # print(lost)
                    
def display_points(window, points):
    points_window = tk.Toplevel(window)
    points_window.title("Points")

    points_label = tk.Label(points_window, text=f'Points: {points}', padx=20, pady=10, justify='left')
    points_label.pack()

def conc_names(names):
    concatenated_names = []
    for i in range(0, len(names), 2):
        first_name = names[i]
        second_name = names[i + 1] if i + 1 < len(names) else None
        if second_name:
            concatenated_names.append(f"{first_name} {second_name}")
    return(concatenated_names)

def squad(team_name):
    players = []
    with open('players.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            # print(content)
            team = content.split()[2]
            if team == team_name:
                name = content.split()[0] + ' ' + content.split()[1]
                players.append(name)
    return players 

def fixtures(window):
    fixtures = []
    with open('matches.txt', 'r') as file:
        fixtures.append(file.readline())
        file.readline()
        contents = file.readlines()
        for content in contents:
            fixtures.append(content)
    fixtures_window = tk.Toplevel(window)
    fixtures_window.title("Fixtures")
    label_font = ("Courier", 8) 
    fixtures_label = tk.Label(fixtures_window, text='\n'.join(fixtures), font=label_font, padx=10, pady=10, justify='left')
    fixtures_label.pack(expand=True, fill=tk.BOTH)

def display_match(window, match):
    match_window=tk.Toplevel(window)
    match_window.title("Match")
    label_font = ("Courier", 8) 
    match_label=tk.Label(match_window, text='\n'.join(match),font=label_font, padx=20,pady=20,justify ="left")
    match_label.pack()

def player_details(window, player_name):
    with open('players.txt','r') as file:
        file.readline()
        file.readline()
        lineNo=2
        for line in file:
            x=line.split()
            name = x[0] + ' ' + x[1]
            if player_name==name:
                p=line.split()
                x=Player(p[0]+" "+p[1],p[-1],p[2],p[3],p[4],p[5])
                u=x.display_player_info()
                display_player(window, u)
                return ''
            lineNo +=1
    return show_message(window, 'Player not found!')

def display_player(window, player):
    player_window = tk.Toplevel(window)
    player_window.title("Player")
    label_font = ("Courier", 8) 
    player_label = tk.Label(player_window, text=player, font=label_font, padx=20, pady=10, justify='left')
    player_label.pack()

def add_player(name,team,age, bat, bowl,wk):
    with open('players.txt','a') as file:
        x=name.ljust(26)+team.ljust(16)+bat.ljust(9)+bowl.ljust(9)+wk.ljust(13)+str(age).ljust(5)
        file.write('\n' + x)      

def remove_player(window, player_name):
    with open('players.txt','r') as file:
        file.readline()
        file.readline()
        lineNo=2
        for line in file:
            x=line.split()
            if player_name==x[0]+" "+x[1]:
                break
            lineNo +=1
    with open('players.txt','r') as file:
        x=file.readlines()
        x=x[:lineNo]+x[lineNo+1:]
    with open('players.txt','w') as file:
        file.writelines(x)
    show_message(window, 'Player record removed successfully')

def remove_match(window, match_no):
    file=open('matches.txt','r')
    match_no=int(match_no)
    z=file.readlines()
    filelength=len(z)
    if match_no+1>filelength:
        show_message(window, 'No match of this number exists')
        return ""
    Line=(z[match_no+1]).split()
    z=z[:match_no+1]+z[match_no+2:]
    filelength=len(z)
    if Line[-1]=='TBD' or Line[-2]=='TBD':
        x=match_no
        if x+2<filelength:
            for i in range(x+1,filelength):
                line=z[i]
                w=str(i-1)+line[2:]
                z[i]=w
        file.close()
        file=open('matches.txt','w')
        file.writelines(z)
        file.close()
        show_message(window, 'Match record removed successfully')
        return ""
    else:
        show_message( window, 'This match cannot be deleted')
        return ""
    
def match_details(window, team1, team2='Null'):
    result = []
    if team2 != 'Null':
        team1=team1.split()
        team1="".join(team1)
        team2=team2.split()
        team2="".join(team2)
        with open('matches.txt','r') as file:
            result.append(file.readline().strip())
            result.append(file.readline().strip() + '\n')
            # result.append(file.readline().strip())
            # result.append(file.readline().strip())
            for line in file:
                x=line.split()
                if (team1==x[1] and team2==x[2]) or (team2==x[1] and team1==x[2]):
                    result.append(line)
    elif type(team1)==str:
        with open('matches.txt','r') as file:
            result.append(file.readline().strip())
            result.append(file.readline().strip() + '\n')
            # result.append(file.readline().strip())
            # result.append(file.readline().strip())
            for line in file:
                x=line.split()
                if team1==x[1]  or team1==x[2]:
                    result.append(line)
    elif type(team1)==int:
        with open('matches.txt','r') as file:
            result.append(file.readline().strip())
            result.append(file.readline().strip() + '\n')
            file.readline().strip()
            # result.append(file.readline().strip())
            # result.append(file.readline().strip())
            for line in file:
                x=line.split()
                if team1==int(x[0]):
                   result.append(line)
    display_match(window, result)
