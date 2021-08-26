def getNumPlayersInTheRaid(roster_list, num_players_needed):
    # you can do things in here.
    x = len(roster_list)
    missing_players = num_players_needed - x
    return x, missing_players


def getRaidInfo(roster_list, num_players_needed):
    num_players = len(roster_list)
    missing_players = num_players_needed - num_players

    return {
        "playerCount": num_players,
        "absentJerks": missing_players,
    }


karazhan_roster = [
    "rne",
    "steptank",
    "flashy",
    "drye",
    "shanko",
]

gruul_roster = [
    "asriel",
    "kurbie",
    "rne",
    "steptank",
]

magtheridon_roster = [
    "nobody",

]

kara_info = getNumPlayersInTheRaid(karazhan_roster, 10)
grull_info = getNumPlayersInTheRaid(gruul_roster, 25)

print("The number of players attending kara is:")
print(kara_info[0])
print("The number of players absent is")
print(kara_info[1])

print("The number of players attending gruul is:")
print(grull_info[0])
print("The number of players absent is")
print(grull_info[1])

print("PART 2: ================")

print(getRaidInfo(karazhan_roster, 10))
print(getRaidInfo(gruul_roster, 25))

kara_info2 = getRaidInfo(karazhan_roster, 10)
print(kara_info2["absentJerks"])

