import random
import time
import os
from colorama import Fore, Style
is_player_alive = True
gore = False
print("")
print(Fore.RED + Style.BRIGHT + "BLOOD AND HONOR\n")
menu_choice = 0
times = 0
gladiator = 0
svårighet = ("lätt")
romdaler = 0
kejsaren_närvarande = ["närvarande!", "inte närvarande.","inte närvarande.", "inte närvarande.", "närvarande!", "inte närvarande.","inte närvarande.", "inte närvarande.", "närvarande!", "inte närvarande.","inte närvarande.", "inte närvarande.",]
fiende = ["Tiger", "Tiger", "Tiger", "Tiger", "Gladiator", "Gladiator", "Gladiator", "Gladiator", "Gladiator", "Gladiator", "Drake", "Gladiator", "Gladiator", "Gladiator"]
erfarenhet = 0
vapen = ("dina händer")
gladiatorns_vapen = ["ett Kortsvärd", "en Kroksabel", "ett Spjut", "en Pilbåge"]
runda = 1      
spelare_hälsopoäng = 10
fiende_hälsopoäng = 10
vapen_skada = 3                                  

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def affären(romdaler):
    global vapen
    marknaden = 1
    while marknaden == (1):
        köp = "Nej"
        val = None
        print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
        print(Fore.RESET + Style.BRIGHT + "Affären")
        print(f"Du har {romdaler} romdaler kvar")
        print("")
        print(Style.RESET_ALL + "Vad vill du köpa idag?")
        print("1. Kortsvärd (20r)\n2. Yxor (30r)\n3. Kroksabel (40)\n4. Spjut (50r)")
        val = input(":")
        if val == "1" or val == "kortsvärd" or val == "Kortsvärd":
            if vapen == "ett kortsvärd":
                print("1. Köp Kortsvärd (Du har redan detta vapnet)")
            elif romdaler > 19:
                print("1. Köp Kortsvärd (" + Fore.GREEN + "20" + Fore.RESET + ")?")
                köp = input("(ja) eller (nej):")
                if köp == "ja":
                    romdaler -= 20
                    vapen = "ett kortsvärd"
                    print("Du äger nu ett kortsvärd!")
                else:
                    print("Okej :(")

            else:
                print("1. Köp Kortsvärd (" + Fore.RED + "20" + Fore.RESET + ")?")
                köp = input("(ja) eller (nej):")
                if köp == "ja":
                    print("Du har inte tillräckligt med pengar...")
                else:
                    print("Okej :(")
        elif val == "2" or val == "yxor" or val == "Yxor":
            if vapen == "dina yxor":
                print("2. Köp Yxor (Du har redan detta vapnet)")
            elif romdaler > 29:
                print("2. Köp Yxor (" + Fore.GREEN + "30" + Fore.RESET + ")?")
                köp = input("(ja) eller (nej):")
                if köp == "ja":
                    romdaler -= 30
                    vapen = "dina yxor"
                    print("Du äger nu yxor!")
                else:
                    print("Okej :(")

            else:
                print("2. Köp Yxor (" + Fore.RED + "30" + Fore.RESET + ")?")
                köp = input("(ja) eller (nej):")
                if köp == "ja":
                    print("Du har inte tillräckligt med pengar...")
                else:
                    print("Okej :(")
        elif val == "3" or val == "kroksabel" or val == "Kroksabel":
            if vapen == "en kroksabel":
                print("3. Köp Kroksabel (Du har redan detta vapnet)")
            elif romdaler > 39:
                print("3. Köp Kroksabel (" + Fore.GREEN + "40" + Fore.RESET + ")?")
                köp = input("(ja) eller (nej):")
                if köp == "ja":
                    romdaler -= 40
                    vapen = "en kroksabel"
                    print("Du äger nu en kroksabel!")
                else:
                    print("Okej :(")
            else:
                print("3. Köp Kroksabel (" + Fore.RED + "40" + Fore.RESET + ")?")
                köp = input("(ja) eller (nej):")
                if köp == "ja":
                    print("Du har inte tillräckligt med pengar...")
                else:
                    print("Okej :(")
        elif val == "4" or val == "spjut" or val == "Spjut":
            if vapen == "ett spjut":
                print("4. Köp Spjut (Du har redan detta vapnet)")
            elif romdaler > 49:
                print("4. Köp Spjut (" + Fore.GREEN + "50" + Fore.RESET + ")?")
                köp = input("(ja) eller (nej):")
                if köp == "ja":
                    romdaler -= 50
                    vapen = "ett spjut"
                    print("Du äger nu ett spjut!")
                else:
                    print("Okej :(")

            else:
                print("4. Köp Spjut (" + Fore.RED + "50" + Fore.RESET + ")?")
                köp = input("(ja) eller (nej):")
                if köp == "ja":
                    print("Du har inte tillräckligt med pengar...")
                else:
                    print("Okej :(")
    
        marknaden = int(input("Om du vill lämna marknaden tryck (2), om du vill fortsätta tryck (1)"))
        print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
    clear_screen()
    return romdaler
    

            



    



    





#Så länge som spelaren inte klickat på 4 för att börja spela, så är menyn igång
while menu_choice != ("4"):
    print(Fore.RESET + Style.BRIGHT + "===============================================================================================================================")
    print(Style.BRIGHT + Fore.WHITE + "Spelmeny\n" + Style.RESET_ALL + Fore.RED + "Gore        " + Fore.GREEN +"Välj Gladiator   "  + Fore.YELLOW + "Svårighetsgrad\n")
    menu_choice = input(Fore.RESET + "Klicka 1 för att sätta på eller av Gore(Blodiga effekter)\n" 
    "Klicka 2 för att välja svårighetsgrad \nKlicka 3 för att välja karaktär \nKlicka 4 för att börja spela\nOBS! VÄLJ KARAKTÄR INNAN DU BÖRJAR\n:")
    if menu_choice == ("1"):
        gore_choice = input(f"Gore är på {gore}.\nVill du ha gore (På) eller (Av)?")
        if gore_choice == ("På"):
            gore = True
            print("Gore är nu (På).")
        else:
            gore = False
            print("Gore är nu (Av).")
            print(" ")
        input("Tryck valfri tangent för att komma tillbaka till menyn...\n")
    if menu_choice == ("2"):
        print("Svårighetsgraderna är (lätt), (medel), (expert).")
        svårighet = input("Vilken svårighet vill du ha?")
        if svårighet == ("lätt"):
            svårighet = (1)
            print("Svårighetsgraden är nu på lätt")
        elif svårighet == ("medel"):
            svårighet = (2)
            print("Svårighetsgraden är nu på medel")
        elif svårighet == ("expert"):
            svårighet = (3)
            print("Svårighetsgraden är nu på expert")
        else:
            if times == (0):
                print("Don't mess with the system! Du får lätt, vill du ha en annan så får du göra om det.")
                svårighet = (1)
                times += 1
            elif times == (1):
                print("Okej det är seriöst inte roligt nu, du får medel, tryck in en riktig svårighetsgrad om du vill ha en annan.")
                svårighet = (2)
                times += 1
            else:
                print("Fuck you du får expert.")
                svårighet = (3)
                times += 1
                print("Svårighetsgraden är nu på expert")
        print(" ")
        input("Tryck valfri tangent för att komma tillbaka till menyn...\n")
    
    
    if menu_choice == ("3"):
        kön_val = input("Vill du vara man eller kvinna?")
        if kön_val == "man":
            print("Välj en av följande gladiatorer:")
            print("1. Bobius Bobiusson\nEn vildman i 20 års åldern, tagen som slav från den nordesta toppen av romarriket, är fylld av hat och ilska,\n" \
            "redo att ta ut den på alla som kommer i hans väg...")
            print("Egenskaper:\n" + Fore.GREEN + "+ Är skicklig med yxor\n+ Går in i berserkagång ibland och gör mer skada\n" + Fore.RED + "- Kan i sin berserkagång råka skada sig själv\n\n" + Fore.RESET)
            print("2. Maximus Decimus Meridius\nEn äldre romersk general som blivit förråd och fått sin familj mördad. " \
            "Han är redo att ge igen mot allt och alla som förstört honom.")
            print("Egenskaper:\n" + Fore.GREEN + "+ Är skicklig med kortsvärd\n+ Ger ibland iväg ett vrål, som sänker fiendens moral, som sänker deras träffchans\n" + Fore.RED + "- På grund av sin ålder, är långsammare och gör mindre skada.\n\n" + Fore.RESET)
            gladiator = int(input("Välj din gladiator(1 eller 2)"))
            if gladiator == (1):
                gladiator = ("Bobius Bobiusson")
            elif gladiator == (2):
                gladiator = ("Maximus Decimus Meridius")
            else:
                print("Det var inte ett val, du får Bobius Bobsson. Gör om detta ifall du vill ha en annan.")
                gladiator = ("Bobius Bobiusson")

            print(f"Du har just nu valt {gladiator} som din gladiator.")
            if gladiator == ("Bobius Bobiusson"):
                gladiator = (1)
            elif gladiator == ("Maximus Decimus Meridius"):
                gladiator = (2)
        elif kön_val == "kvinna":
            print("3. Berlinda Bobsson\nEn soldatkvinna från söder, tagen som slav är farlig med kroksablar, och förbluffar fiender med hennes snabbhet.\nHon är fast besluten att ta sig hem till södern.")
            print("Egenskaper:\n" + Fore.GREEN + "+ Är skicklig med kroksablar\n+ Är väldigt snabb, har ökad träffchans\n" + Fore.RED + "- Gör mindre skada på grund av gammal skada\n\n" + Fore.RESET)
            print("4. Emilia Neosdotter\nEn tjuv som tillsluts tagits efter flera år av stölder och terrorisering.\nEmilia är väldigt gymnastisk och farlig på grund av hennes kunnighet inom stridskonst.")
            print("Egenskaper:\n" + Fore.GREEN + "+ Är skickligast utan vapen\n+ Är väldigt kvick, och är svårare att träffa\n" + Fore.RED + "- Gör mindre skada på grund av svaghet\n\n" + Fore.RESET)
            gladiator = int(input("Välj din gladiator(3 eller 4)"))
            if gladiator == (3):
                gladiator = ("Berlinda Bobsson")
            elif gladiator == (4):
                gladiator = ("Emilia Neosdotter")
            else:
                print("Det var inte ett val, du får Berlinda Bobsson. Gör om detta ifall du vill ha en annan.")
                gladiator = ("Berlinda Bobsson")

            print(f"Du har just nu valt {gladiator} som din gladiator.")
            if gladiator == ("Berlinda Bobsson"):
                gladiator = (3)
            elif gladiator == ("Emilia Neosdotter"):
                gladiator = (4)

        kön_val = None
        print(" ")
        input("Tryck valfri tangent för att komma tillbaka till menyn...\n")

    clear_screen()
        
#################################################################################################################################
if svårighet == (1):
    spelare_hälsopoäng = 15
    fiende_hälsopoäng = 10
    vapen_skada = 4
elif svårighet == (2):
    spelare_hälsopoäng = 10
    fiende_hälsopoäng = 10
    vapen_skada = 3
elif svårighet == (3):
    spelare_hälsopoäng = 10
    fiende_hälsopoäng = 15
    vapen_skada = 2
    

print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
print("Du går in i mäktiga Coloseum för första gången, och publiken iaktar dig misstänksamt, de känner inte igen dig.\nKejsaren är inte närvarande, och framför dig så ser du din första fiende, en gladiator.")
print(f"Dina trasor till kläder fläktar i vinden, och {vapen} är vid din sida. Du och din motståndare är redo att slåss.")
print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
#sätt in fight här
    

print("")

    
print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
fienden = random.choice(fiende)
kejsaren = random.choice(kejsaren_närvarande)
if fienden == "Gladiator":
    gladiatorns_vapen_för_striden = random.choice(gladiatorns_vapen)

if fienden == "Gladiator":
    print(f"Du går in i mäktiga Colosseum, publiken jublar och hejar fram dig. Framför dig så står en Gladiator med {gladiatorns_vapen_för_striden}!\nKejsaren är {kejsaren} Du och din motståndare är redo att slåss.") 
else:
    print(f"Du går in i mäktiga Colosseum, publiken jublar och hejar fram dig. Framför dig så står en {fienden}!\nKejsaren är {kejsaren} Du och din motståndare är redo att slåss.")

print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)



while spelare_hälsopoäng > 0 and fiende_hälsopoäng > 0:
    print(f"Runda {runda}")
    print("Du har " + Fore.GREEN + str(spelare_hälsopoäng) + Fore.RESET + " hälsopoäng kvar, och din motsåndare har " + Fore.RED +  str(fiende_hälsopoäng) + Fore.RESET + " hälsopoäng kvar.")
    
    
    print("Vad använder du för attack?\n1." + Fore.YELLOW + "Hårt slag " + Fore.RED + str(vapen_skada) + "")


affären(romdaler)