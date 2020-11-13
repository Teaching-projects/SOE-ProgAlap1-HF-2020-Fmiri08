"""
Tovabbfejlesztjuk az elozo dolgot. 

Most atirjuk a kiirato fuggvenyt ugy, hogy kap egy dictionary-t is, amiben benne van a jatekos karakterunk a kovetkezo modon:

character = {
    "name" : "Dark Wanderer",
    "position" : {
        "x" : 4 ,
        "y" : 2 
    }
}


Az eredmenye a kiiratasnak a korabbi peldaterkepen igy nezne ki:

████████████████████████████
██░░░░░░░░░░░░██████████████
██░░░░░░🧙‍░░░░██████░░░░░░██
██░░░░██████████████░░██░░██
██░░░░██░░░░░░░░░░██░░██░░██
██░░░░░░░░░░░░██░░██░░██░░██
██████████░░░░██░░██░░██░░██
██░░░░░░░░░░░░██░░░░░░██░░░░
████████████████████████████

Ket dolog valtozott meg:
 - Az eddigi █ es ░ karaktereket mindig duplan rajzoljuk ki, hogy korulbelul negyzet alaku legyen egy mezo.
 - A karakterunk helyere 🧙‍-t irunk ki.



"""

def initialize_map (width, height):
    # ide masold be a helyes megoldasodat a multkorirol
    terkep=[width*["█"]]
    for i in range(height-2):
        egyseg=["█"]
        for j in range(width-2):
            egyseg.append("░")
        egyseg.append("█")          
        terkep.append(egyseg)
    terkep.append(["█"]*width)    
    return terkep

def pretty_map_print(map, character):
    # Ide masold be a multkorit, a fenti modositasokkal. 
    # Ha a karakter pozicioja a palyan kivul lenne, egyszeruen ne jelenjen meg
    x = character["position"]["x"]
    y = character["position"]["y"]
    sor = len(map[1])
    oszlop = len(map)
    if (x <= sor - 1 and x >= 0) and (y <= oszlop - 1 and y >= 0): 
        print(len(map[y]))
        map[y][x] = "🧙"
        print(len(map[y]))
    for i in range(len(map)):
        for j in range(len(map[i])): print(map[i][j], end="")
        print("")




###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


def initialize_character():
    x=int(input())
    y=int(input())
    return {"name": "Placeholder name", "position" : {"x":x,"y":y} }

width=int(input())
height=int(input())
map=initialize_map(width,height)

character=initialize_character()

pretty_map_print(map,character)
