import random
import time
is_player_alive = True
gore = False
print("")
print("GLADIATORERNA\n")
menu_choice = 0
svårighet = ("lätt")
karaktär = ("Ingen")
while menu_choice is not ("4"):
    print("Spelmeny\nGore             Välj Gladiator                  Svårighetsgrad\n")
    menu_choice = input("Klicka 1 för att sätta på eller av Gore(Blodiga effekter)\n" 
    "Klicka 2 för att välja svårighetsgrad \nKlicka 3 för att välja karaktär \nKlicka 4 för att börja spela\n:")
    if menu_choice == ("1"):
        gore_choice = input(f"Gore är på {gore}.\nVill du ha gore (På) eller (Av)?")
        if gore_choice == ("På"):
            gore = True
            print("Gore är nu (På).")
        else:
            gore = False
            print("Gore är nu (Av).")
    if menu_choice == ("2"):
        print("Svårighetsgraderna är (lätt), (medel), (expert).")
        svårighet = input("Vilken svårighet vill du ha?")
        if svårighet == ("lätt"):
            svårighet = ("lätt")
        
        if svårighet == ("medel"):
            svårighet = ("medel")

        if svårighet == ("expert"):
            svårighet = ("expert")
        
        print(f"Svårighetsgraden är nu på {svårighet}")
    
    if menu_choice == ("3"):
        print("Välj en av följande gladiatorer:")
        print("1. Bobius Bobiusson\nEn vildman i 20 års åldern, tagen som slav från den nordesta toppen av romarriket, är fylld av hat och ilska,\n" \
        "redo att ta ut den på alla som kommer i hans väg...")
        print("Egenskaper:\n+Är skicklig med yxor\n+Går in i berserkagång ibland och gör mer skada\n-Kan i sin berserkagång råka skada sig själv\n\n")
        print("2. Maximus Decimus Meridius\nEn äldre romersk general som blivit förråd och fått sin familj mördad. " \
        "Han är redo att ge igen mot allt och alla som förstört honom.")
        print("Egenskaper:\n+Är skicklig med kortsvärd\n+Ger ibland iväg ett vrål, som sänker fiendens moral, som sänker deras träffchans\n-På grund av sin ålder, är långsammare och gör mindre skada.\n\n")
        print("3. Berlinda Bobsson\nEn soldatkvinna från söder, tagen som slav är farlig med kroksablar, och förbluffar fiender med hennes snabbhet.\nHon är fast besluten att ta sig hem till södern.")
        print("Egenskaper:\n+Är skicklig med kroksablar\n+Är väldigt snabb, har ökad träffchans\n-Gör mindre skada på grund av biologiskt kön\n\n")
        print("4. ")
    
    print(" ")
    input("Tryck valfri tangent för att komma tillbaka till menyn...\n")