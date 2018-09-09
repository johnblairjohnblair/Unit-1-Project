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
            print("experienced")
        elif players[player]['experience'] == 'NO':
            inexperienced_players[player] = players[player]
            print("inexp")
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
        if len(sharks) == len(dragons) and len(sharks) == len(raptors):
            sharks[player] = players[player]
        if len(sharks) <= len(dragons) and len(sharks) <= len(dragons):
            sharks[player] = players[player]
        elif len(dragons) <= len(sharks) and len(dragons) <= len(raptors):
            dragons[player] = players[player]
        elif len(raptors) <= len(dragons) and len(raptors) <= len(sharks):
            raptors[player] = players[player]
        else:
            print("something happened ", player, " not assigned to a team!")


#Assign inexperiences list based on least fill
    for player in inexperienced_players:
        if len(sharks) == len(dragons) and len(sharks) == len(raptors):
            sharks[player] = players[player]
        if len(sharks) <= len(dragons) and len(sharks) <= len(dragons):
            sharks[player] = players[player]
        elif len(dragons) <= len(sharks) and len(dragons) <= len(raptors):
            dragons[player] = players[player]
        elif len(raptors) <= len(dragons) and len(raptors) <= len(sharks):
            raptors[player] = players[player]
        else:
            print("something happened ", player, " not assigned to a team!")

# SELF CHECK FOR TEAMS
    print("Sharks:")
    for player in sharks:
        print(player)
    print("Dragons:")
    for player in dragons:
        print(player)
    print("Raptors:")
    for player in raptors:
        print(player)

# Write teams and players to doc


# Generate welcome letters
