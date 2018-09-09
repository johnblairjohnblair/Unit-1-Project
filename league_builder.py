import csv

if __name__ == "__main__":

#Declare variables
    players = {}

    sharks = {}
    dragons = {}
    raptors = {}

    experienced_players = {}
    inexperienced_players = {}

# Open csv and read values into dicts
    with open("soccer_players.csv", "r") as players_file:
        file = csv.reader(players_file)
        file.next()
        for row in file:
            players.update({row[0]: {
                'name': row[0],
                'height': row[1],
                'experience': row[2],
                'guardians': row[3]
            }})

    for player in players:
        print(players[player])

# Sort players into dicts based on experience
    for player in players:
        if players[player]['experience'] == 'YES':
            experienced_players[player] = players[player]
            print(player + "experienced")
        elif players[player]['experience'] == 'NO':
            inexperienced_players[player] = players[player]
            print(player + "inexp")
        else:
            print("no exp variable")

# TEST PRINT #
    print("Experienced Players:")
    for player in experienced_players:
        print(player)

    print("Inexperienced Players:")
    for player in inexperienced_players:
        print(player)

# Assign experienced list based on list fill
    for player in experienced_players:
        lowest_team = min(len(sharks), len(dragons), len(raptors))
        if len(sharks) == lowest_team:
            sharks[player] = players[player]
            print(players[player]['name'] + "assigned to sharks")
        elif len(dragons) == lowest_team:
            dragons[player] = players[player]
            print(players[player]['name'] + "assigned to dragons")
        elif len(raptors) == lowest_team:
            raptors[player] = players[player]
            print(players[player]['name'] + "assigned to raptors")
        else:
            print("something happened ", player, " not assigned to a team!")


#Assign inexperiences list based on least fill
    for player in inexperienced_players:
        lowest_team = min(len(sharks), len(dragons), len(raptors))
        if len(sharks) == lowest_team:
            sharks[player] = players[player]
            print(players[player]['name'] + "assigned to sharks")
        elif len(dragons) == lowest_team:
            dragons[player] = players[player]
            print(players[player]['name'] + "assigned to dragons")
        elif len(raptors) == lowest_team:
            raptors[player] = players[player]
            print(players[player]['name'] + "assigned to raptors")
        else:
            print("something happened ", player, " not assigned to a team!")

# SELF CHECK FOR TEAMS
    print("\nSharks:")
    for player in sharks:
        print(player)
    print("\nDragons:")
    for player in dragons:
        print(player)
    print("\nRaptors:")
    for player in raptors:
        print(player)


#Create text to print into text doc
    def player_info(player):
        text = player['name'] + ", " + player['experience'] + ", " + player['guardians']
        return(text)

    def full_message():
        print("\nSharks:")
        for player in sharks:
            player_info(sharks[player])

        print("\nDragons:")
        for player in dragons:
            player_info(dragons[player])

        print("\nRaptors:")
        for player in raptors:
            player_info(raptors[player])

        return("This is what returned from full_message function...")

# Write teams and players to doc
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
