import tkinter as tk

def show_message(window, message):
    message_window = tk.Toplevel(window)
    message_window.title("Note")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    half_width = screen_width // 2
    half_height = screen_height // 2

    x_position = (screen_width - half_width) // 2
    y_position = (screen_height - half_height) // 2

    message_window.geometry(f"{half_width}x{half_height}+{x_position}+{y_position}")

    message_label = tk.Label(message_window, text='Note:', padx=20, pady=10)
    message_label.pack()

    squad_label = tk.Label(message_window, text=message, padx=20, pady=10)
    squad_label.pack()

def display_squad(window, team_name):
    players = squad(team_name)
    print(players)  # Get the list of players for the team
    if players:
        squad_window = tk.Toplevel(window)
        squad_window.title("Squad")

        # Display players in a label
        players_label = tk.Label(squad_window, text='\n'.join(players), padx=20, pady=10)
        players_label.pack()
    else:
        show_message(window, 'Team not found!')

def standings(window):
    table = []
    with open('points.txt', 'r') as file:
        line = file.readline()
        table.append(line)
        file.readline()
        contents = file.readlines()
        for content in contents:
            content = content
            table.append(content)
    standings_window = tk.Toplevel(window)
    standings_window.title("Standings")

    players_label = tk.Label(standings_window, text='\n'.join(table), padx=20, pady=10, justify='left')
    players_label.pack()
    
def display_teams(window):
    teams = []
    with open('teams.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            team = content.split()[0]
            teams.append(team + '\n')
    if teams:
        squad_window = tk.Toplevel(window)
        squad_window.title("Teams")

        players_label = tk.Label(squad_window, text='\n'.join(teams), padx=20, pady=10, justify='left')
        players_label.pack()

def points(window, team_name):
    search = False
    with open('points.txt', 'r') as file:
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            team = content.split()[1]
            if team == team_name:
                points = content.split()[6]
                display_points(window, points)
                search = True
    if search == False:
        show_message(window, 'Team not found!')

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
        file.readline()
        file.readline()
        contents = file.readlines()
        for content in contents:
            fixtures.append(content)
    fixtures_window = tk.Toplevel(window)
    fixtures_window.title("Fixtures")

    fixtures_label = tk.Label(fixtures_window, text='\n'.join(fixtures), padx=20, pady=10, justify='left')
    fixtures_label.pack()

def match_details(window, team1, team2):
    data = []
    # team1=team1.split()
    # team1="".join(team1)
    # team2=team2.split()
    # team2="".join(team2)
    with open('matches.txt','r') as file:
        head = file.readline()
        data.append(head)
        file.readline()
        for line in file:
            x=line.split()
            if (team1==x[1] and team2==x[2]) or (team2==x[1] and team1==x[2]):
                data.append(line.strip())
                display_match(window, data)
                return ''
    show_message(window, 'Match details not found!')

def display_match(window, match):
    match_window = tk.Toplevel(window)
    match_window.title("Match")

    match_label = tk.Label(match_window, text='\n'.join(match), padx=20, pady=10, justify='left')
    match_label.pack()

def remove_match(match_no):
    file=open('matches.txt','r')
    z=file.readlines()
    Line=(z[match_no+1]).split()
    z=z[:match_no+1]+z[match_no+2:]
    if Line[-1]=='TBD' or Line[-2]=='TBD':
        filelength=len(z)
        if match_no+2>filelength:
            raise Exception('No match of this number exists')
        x=match_no
        for i in range(x+1,filelength):
            line=z[i]
            w=str(i-1)+line[2:]
            z[i]=w
        file.close()
        file=open('matches.txt','w')
        file.writelines(z)
        file.close()
        print('Match record removed successfully')
    else:
        raise Exception('This match cannot be deleted')
    
# remove_match(11)
# def remove_match(window, match_no):
#     match_no = int(match_no)
#     file=open('matches.txt','r')
#     z=file.readlines()
#     z=z[:match_no+1]+z[match_no+2:]
#     filelength=len(z)
#     if match_no+2>filelength:
#         raise Exception('No match of this number exists')
#     x=match_no
#     for i in range(x+1,filelength):
#         line=z[i]
#         w=str(i-1)+line[2:]
#         z[i]=w
#     file.close()
#     file=open('matches.txt','w')
#     file.writelines(z)
#     file.close()
#     show_message(window, 'Match record removed successfully')

def player_details(window, player_name):
    player = []
    with open('players.txt','r') as file:
        player.append(file.readline())
        file.readline()
        lineNo=2
        for line in file:
            x=line.split()
            name = x[0] + ' ' + x[1]
            if player_name==name:
                player.append(line.strip())
                display_player(window, player)
                return ''
            lineNo +=1
    return show_message(window, 'Player not found!')

def display_player(window, player):
    player_window = tk.Toplevel(window)
    player_window.title("Player")

    player_label = tk.Label(player_window, text='\n'.join(player), padx=20, pady=10, justify='left')
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
