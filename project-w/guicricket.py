import tkinter as tk
import file

def add_frame(window):
    def save_player(window):
        player_name = name_entry.get()
        player_team = team_entry.get()
        player_age = age_entry.get()
        player_batting = batting_entry.get()
        player_bowling = bowling_entry.get()
        is_wicketkeeper = wk_entry.get()

        if player_name and player_team and player_age and player_batting and player_bowling and is_wicketkeeper:
            file.add_player(player_name, player_team, player_age, player_batting, player_bowling, is_wicketkeeper)
            add_player_window.destroy()
        else:
            add_player_window.destroy()
            file.show_message(window, 'Incomplete data. Try again!')
        # file.add_player(name=player_name, team=player_team, age=player_age, bat=player_batting, bowl=player_bowling, wk=is_wicketkeeper)

        # add_player_window.destroy()

    add_player_window = tk.Toplevel()
    add_player_window.title("Add Player")

    name_label = tk.Label(add_player_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(add_player_window)
    name_entry.pack()

    team_label = tk.Label(add_player_window, text="Team:")
    team_label.pack()
    team_entry = tk.Entry(add_player_window)
    team_entry.pack()

    age_label = tk.Label(add_player_window, text="Age:")
    age_label.pack()
    age_entry = tk.Entry(add_player_window)
    age_entry.pack()

    batting_label = tk.Label(add_player_window, text="Batting:(yes/no)")
    batting_label.pack()
    batting_entry = tk.Entry(add_player_window)
    batting_entry.pack()

    bowling_label = tk.Label(add_player_window, text="Bowling:(yes/no)")
    bowling_label.pack()
    bowling_entry = tk.Entry(add_player_window)
    bowling_entry.pack()

    wk_label = tk.Label(add_player_window, text="Wicket Keeper:(yes/no)")
    wk_label.pack()
    wk_entry = tk.Entry(add_player_window)
    wk_entry.pack()

    save_button = tk.Button(add_player_window, text="Save", command=lambda: save_player(window))
    save_button.pack()

def extra_frame():
    frame = tk.LabelFrame(window, text="Tournament Overview", bg="light gray", padx=20, pady=10)
    frame.grid(row=1, column=0, padx=20, pady=15, sticky="nsew")

    standings_button = tk.Button(frame, text="Standings", command=lambda: file.standings(window))
    standings_button.grid(row=0, column=0, pady=5, padx=(10, 10))

    fixtures_button = tk.Button(frame, text="Fixtures", command=lambda: file.fixtures(window))
    fixtures_button.grid(row=0, column=1, pady=5, padx=(10, 10))

def team_frame(window):
    team_frame = tk.LabelFrame(window, text="Team Management", bg="light gray", padx=50, pady=10)
    team_frame.grid(row=2, column=0, padx=20, pady=15, sticky="nsew")

    team_name_label = tk.Label(team_frame, text="Team Name")
    team_name_label.grid(row=0, column=0, pady=5)
    team_name_entry = tk.Entry(team_frame)
    team_name_entry.grid(row=0, column=1, pady=5)

    squad_button = tk.Button(team_frame, text="Squad", command=lambda: file.display_squad(window, team_name_entry.get()))
    squad_button.grid(row=0, column=2, pady=5, padx=(20, 10))

    points_button = tk.Button(team_frame, text="Points", command=lambda: file.points(window, team_name_entry.get()))
    points_button.grid(row=0, column=3, pady=5, padx=(10, 10))

    # add_team_button = tk.Button(team_frame, text="Add Team", command=lambda: show_message("Add Team"))
    # add_team_button.grid(row=0, column=4, pady=5, padx=(10, 10))

    list_teams_button = tk.Button(team_frame, text="List All Teams", command=lambda: file.display_teams(window))
    list_teams_button.grid(row=1, column=0, pady=5, padx=(10, 10))

def match_frame():
    match_frame = tk.LabelFrame(window, text="Match Management", bg="light gray", padx=20, pady=10)
    match_frame.grid(row=3, column=0, padx=20, pady=15, sticky="nsew")

    team1_label = tk.Label(match_frame, text="Team 1")
    team1_label.grid(row=0, column=0, pady=5)
    team1_entry = tk.Entry(match_frame)
    team1_entry.grid(row=0, column=1, pady=5)

    team2_label = tk.Label(match_frame, text="Team 2")
    team2_label.grid(row=1, column=0, pady=5)
    team2_entry = tk.Entry(match_frame)
    team2_entry.grid(row=1, column=1, pady=5)

    get_details_button = tk.Button(match_frame, text="Get Details", command=lambda: file.match_details(window, team1_entry.get(), team2_entry.get()))
    get_details_button.grid(row=1, column=2, pady=5, padx=(10, 10))

    remove_match_label = tk.Label(match_frame, text="Enter match number")
    remove_match_label.grid(row=3, column=0, pady=5)
    remove_match_entry = tk.Entry(match_frame)
    remove_match_entry.grid(row=3, column=1, pady=5)

    remove_match_button = tk.Button(match_frame, text="Remove Match", command=lambda: file.remove_match(window, remove_match_entry.get()))
    remove_match_button.grid(row=3, column=2, pady=5, padx=(10, 10))

def player_frame():
    player_frame = tk.LabelFrame(window, text="Player Management", bg="light gray", padx=20, pady=10)
    player_frame.grid(row=4, column=0, padx=20, pady=15, sticky="nsew")

    player_name_label = tk.Label(player_frame, text="Player Name")
    player_name_label.grid(row=0, column=0, pady=5)
    player_name_entry = tk.Entry(player_frame)
    player_name_entry.grid(row=0, column=1, pady=5)

    details_button = tk.Button(player_frame, text="Details", command=lambda: file.player_details(window, player_name_entry.get()))
    details_button.grid(row=0, column=2, pady=5, padx=(20, 10))

    add_player_button = tk.Button(player_frame, text="Add Player", command=lambda: add_frame(window))
    add_player_button.grid(row=1, column=0, pady=5, padx=(10, 10))

    remove_player_button = tk.Button(player_frame, text="Remove Player", command=lambda: file.remove_player(window, player_name_entry.get()))
    remove_player_button.grid(row=0, column=3, pady=5, padx=(10, 10))



# Main window
window = tk.Tk()
window.title("Cricket Tournament Management System")

# Define a custom font style
title_font = ("Arial", 8, "bold")  # Font: Arial, size 14, bold

# Apply the custom font to the window title
window.title("Cricket Tournament Management System")
window.option_add("*Font", title_font)

window.state('zoomed')  # Full-screen mode with title bar and close button

# Heading
heading_label = tk.Label(window, text="CRICKET MANAGEMENT SYSTEM", font=("Times New Roman", 25, "bold"), pady=30)
heading_label.grid(row=0, column=0, sticky="nsew")

# Extra frame for Standings and Schedule buttons
extra_frame()

# Frames
team_frame(window)
match_frame()
player_frame()

# Adjust column weights for horizontal elongation
window.grid_columnconfigure(0, weight=1)

window.mainloop()
