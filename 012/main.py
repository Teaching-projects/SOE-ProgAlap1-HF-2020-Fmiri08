"""
Tovabbfejlesztjuk az elozo dolgot. 

Most megirunk egy "szepen kiirato" fuggvenyt, ami megkap egy map-et, es az alabbi formaban kiirja a kimenetre:

██████████████
█░░░░░░███████
█░░░░░░███░░░█
█░░███████░█░█
█░░█░░░░░█░█░█
█░░░░░░█░█░█░█
█████░░█░█░█░█
█░░░░░░█░░░█░░
██████████████


ha ez volt a bemenet:

terkep = [
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","░","░","░","█"],
    ["█","░","░","█","█","█","█","█","█","█","░","█","░","█"],
    ["█","░","░","█","░","░","░","░","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","█","░","█","░","█"],
    ["█","█","█","█","█","░","░","█","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","░","░","█","░","░"],
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"]
]

tehat pl egy initialize_map(10,6) altal adott terkepet ha kiiratunk, az igy nezzen ki:
██████████
█░░░░░░░░█
█░░░░░░░░█
█░░░░░░░░█
█░░░░░░░░█
██████████

"""

def initialize_map (width, height):
    # ide masold be a helyes megoldasodat mult hetrol
    terkep=[width*["█"]]
    for i in range(height-2):
        egyseg=["█"]
        for j in range(width-2):
            egyseg.append("░")
        egyseg.append("█")          
        terkep.append(egyseg)
    terkep.append(["█"]*width)    
    return terkep


def pretty_map_print(map):
    # Ide ird meg az uj fuggvenyt, ami a fentiek szerint generalja a kimenetet
    for i in range(len(map)):
        for j in range(len(map[i])): print(map[i][j], end="")
        print()
        

###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


width=int(input())
height=int(input())
pretty_map_print(initialize_map(width,height))
