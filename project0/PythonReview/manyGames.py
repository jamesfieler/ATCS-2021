games = ["Minecraft", "Basketball", "Cards"]

out = "I like "
i = 0
while i < len(games)-1:
    out += games[i] + ", "
    i += 1
out += "and " + games[i] + ". What games do you like? \n*** Enter \"n\" to stop adding games ***\n"

userGame = input(out)
while (userGame != "n"):
    games.append(userGame)
    userGame = input(out)

i = 0
out = ""
while i < len(games)-1:
    out += games[i] + ", "
    i += 1
out += games[i]

print(out)