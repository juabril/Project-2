import constants

def start_stats():
    clean_players = []
    for player in constants.PLAYERS:
        clean_players.append(player)
    
    new_teams = []
    for team in constants.TEAMS:
        new_teams.append(team)
    
    def clean_data(players):    
        for element in players:
            if element['experience'] == 'YES':
                element['experience'] = bool('TRUE')
            elif element['experience'] == 'NO':
                element['experience'] = bool('')
            if 'and' in element['guardians']:
                guardian1, guardian2 = element['guardians'].split(' and ')
                element['guardian1'] = guardian1
                element['guardian2'] = guardian2
            else:
                element['guardian1'] = element['guardians']
                element['guardian2'] = False
            del(element['guardians'])    
            element['height'] = int(element['height'][0:2])
        return players
    
    def balance_players(player_data, team_data):
        num_players = len(player_data)
        num_teams = len(team_data)
        size_teams = num_players / num_teams
        team1_name, team2_name, team3_name = team_data
        
        #Here we count the total number of experienced players in the data
        experienced_players = 0
        for element in player_data:
            if element['experience'] == True:
                experienced_players += 1
        exp_per_team = experienced_players / num_teams

        #This function builds a team
        def team_builder(ply_data, experts_team):
            team = []
            team_experienced_players = 0       
            for element in ply_data[0:]:
                if element['experience'] == True and team_experienced_players < experts_team:
                    team.append(element)
                    team_experienced_players += 1
                    ply_data.remove(element)
            for element in ply_data[0:]:
                if element['experience'] == False and len(team) < size_teams:
                    team.append(element)
                    ply_data.remove(element)
            team_total_players = len(team)
            return(team, ply_data, team_experienced_players, team_total_players)
        
        team1, player_data, team1_experienced_players, team1_total_players = team_builder(player_data, exp_per_team)
        team2, player_data, team2_experienced_players, team2_total_players = team_builder(player_data, exp_per_team)
        team3, player_data, team3_experienced_players, team3_total_players = team_builder(player_data, exp_per_team)
        
        return (team1, team2, team3, team1_name, team2_name, team3_name, 
                team1_total_players, team2_total_players, team3_total_players, 
                team1_experienced_players, team2_experienced_players, 
                team3_experienced_players
               )
        
    #This function prints the stats of a given team    
    def show_team(team, team_name, team_total_players, team_experienced_players):
        print("\nThank you, these are the stats for the {}:\n".format(team_name))
        print("Total players : {}".format(team_total_players))
        print("Player names :")
        team_names = []
        for element in team:
            team_names.append(element['name'])
        separator = ", "
        print(separator.join(team_names))    
        print("Number of experienced players : {}".format(team_experienced_players))
        team_inexperienced_players = len(team)-team_experienced_players
        print("Number of inexperienced players : {}".format(team_inexperienced_players))
        team_height = []
        team_avg_height = 0
        for element in team:
            team_height.append(element['height'])
        team_avg_height = round((sum(team_height) / len(team)),2)  
        print("Average height (inches): {}".format(team_avg_height))                        
        team_guardians = []
        for element in team:
            if element['guardian2'] == False:
                team_guardians.append(element['guardian1'])
            else:
                team_guardians.append(element['guardian1'])
                team_guardians.append(element['guardian2'])
        print("Team guardians :")
        separator = ", "
        print(separator.join(team_guardians))
        print("\n")
    
        
    #The user interface is here
    clean_data(clean_players)
    (team_a, team_b, team_c, team_a_name, team_b_name, team_c_name,
    team_a_total_players, team_b_total_players, team_c_total_players, 
    team_a_experienced_players, team_b_experienced_players,
    team_c_experienced_players) = balance_players(clean_players, new_teams)
    proceed_answer = "y"
    while proceed_answer.lower() == "y":
        print("\n")
        print("*"*26)
        print("\nBASKETBALL TEAM STATS TOOL\n")
        print("*"*26)      
        print("\n")
        print("********MAIN MENU********")
        print("\nHere are your choices :\n")
        print("1. Display team stats")
        print("2. Quit")
        try:
            choice = int(input("\nPlease enter an option : "))
        except ValueError:
            print("\nThat's not a valid input, please try again \n")
        else:
            if choice == 1:
                print("\nBelow are the teams available: \n")
                for index, item in enumerate(new_teams, 1):
                    print(f'{index}. {item}')
                try:
                    team_choice = int(input("\nEnter the team number that you would like to see stats for : "))
                    if team_choice == 1:
                        show_team(team_a, team_a_name, team_a_total_players, team_a_experienced_players)
                        proceed_answer = input("Would you like to continue looking at basketball stats ? (y/n) ")
                    elif team_choice == 2:
                        show_team(team_b, team_b_name, team_b_total_players, team_b_experienced_players)
                        proceed_answer = input("Would you like to continue looking at basketball stats ? (y/n) ")
                    elif team_choice == 3:
                        show_team(team_c, team_c_name, team_c_total_players, team_c_experienced_players)
                        proceed_answer = input("Would you like to continue looking at basketball stats ? (y/n) ")
                    else:
                        print("\nThat's not a valid team option, plese try again \n")
                        proceed_answer = 'y'
                except ValueError:
                    print("\nThat's not a valid input, please try again \n")
            elif choice == 2:
                proceed_answer = 'n'
            else:
                print("\nThat's not a valid menu option, please try again \n")
    print("\nThank you for visiting, see you next time !\n")
        
        
if __name__ == '__main__':
    start_stats()
