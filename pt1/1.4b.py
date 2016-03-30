nimi = input("Sisestage nimi: ")
lubatudkiirus = input("Sisestage lubatud kiirus (km/h): ")
tegelikkiirus = input("Sisestage tegelik kiirus (km/h): ")

yletatudkiirus = int(tegelikkiirus) - int(lubatudkiirus)
trahv = min(190, int(yletatudkiirus)*3)

print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot.")