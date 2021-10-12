games = ["Minecraft", "Basketball", "Cards"]

out = "I like "
i = 0
while i < len(games)-1:
    out += games[i] + ", "
    i += 1
out += "and " + games[i] + ". What games do you like? "

userGame = input(out)
games.append(userGame)

i = 0
out = ""
while i < len(games)-1:
    out += games[i] + ", "
    i += 1
out += games[i]

print(out)