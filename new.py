from sys import argv

print(argv)

color = argv[1]
if color == "red":
    print("STOP")
elif color == "green":
    print("MOVE")
elif color == "orange":
    print("SLOW DOWN your vehicles")