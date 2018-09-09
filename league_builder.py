import csv

players = {}

experienced_players = {}
inexperienced_players = {}

sharks = {}
dragons = {}
raptors = {}

# Open csv and read values into dicts
def open_file():
    with open("soccer_players.csv", "r") as players_file:
        players_file = csv.reader(players_file)
        players_file.next()
        for row in players_file:
            players.update({row[0]: {
                'name': row[0],
                'height': row[1],
                'experience': row[2],
                'guardians': row[3]
            }})

# Sort players into dicts based on experience
def sort():
    for player in players:
        if players[player]['experience'] == 'YES':
            experienced_players[player] = players[player]
        elif players[player]['experience'] == 'NO':
            inexperienced_players[player] = players[player]
        else:
            print("no exp variable")

# Assign experienced list based on list fill
def assign(players_list):
    for player in players_list:
        lowest_team = min(len(sharks), len(dragons), len(raptors))
        if len(sharks) == lowest_team:
            sharks[player] = players[player]
        elif len(dragons) == lowest_team:
            dragons[player] = players[player]
        elif len(raptors) == lowest_team:
            raptors[player] = players[player]
        else:
            print("something happened ", player, " not assigned to a team!")

# Create player specific line of text including information, experience and guardians
def player_info(player):
    text = player['name'] + ", " + player['experience'] + ", " + player['guardians']
    return(text)

# Write teams and players to doc
def write_final():
    final = open("teams.txt", "w")
    final.write("\nSharks:")
    for player in sharks:
        final.write("\n" + player_info(sharks[player]))
    final.write("\n\nDragons:")
    for player in dragons:
        final.write("\n" + player_info(dragons[player]))
    final.write("\n\nRaptors:")
    for player in raptors:
        final.write("\n" + player_info(raptors[player]))
    final.close()

# Generate welcome letters
def welcome_letters():
    all_players = {"Sharks": sharks, "Dragons": dragons, "Raptors": raptors}
    for team in all_players:
        for student in all_players[team]:
            letter_filename = student.replace(" ", "_")+".txt"
            welcome_letter = open(letter_filename, "w")
            welcome_letter.write("Dear " + all_players[team][student]['guardians'] + ", \n\nCONGRATULATIONS!!\n\n"
                                 + all_players[team][student]['name'] + " has been selected to join the "
                                 + team + "! \n\nOur first practice will be Wednesday, September 12th at 7pm CT "
                                          "at the school soccer field. \n\nBring snacks!")

#Main, call all functions
if __name__ == '__main__':
    open_file()
    sort()
    assign(inexperienced_players)
    assign(experienced_players)
    write_final()
    welcome_letters()



