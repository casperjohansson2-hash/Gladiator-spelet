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
fiende = ["Tiger", "Tiger", "Tiger", "Gladiator", "Gladiator", "Gladiator", "Gladiator", "Gladiator", "Gladiator", "Gladiator", "Gladiator", "Gladiator"]
erfarenhet = 0
vapen = ("dina händer")
gladiatorns_vapen = ["ett Kortsvärd", "en Kroksabel", "ett Spjut", "en Pilbåge"]
runda = 1      
spelare_hälsopoäng = 10
fiende_hälsopoäng = 10
vapen_skada = 3
spelare_vapen = vapen_skada
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

vapen_träffchans = None

träffar = False

omtyckt = 0


        


    


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
    vapen_skada = 3
    tiger_skada = 2
    drake_skada = 3
elif svårighet == (2):
    spelare_hälsopoäng = 10
    fiende_hälsopoäng = 10
    vapen_skada = 2
    tiger_skada = 3
    drake_skada = 4
elif svårighet == (3):
    spelare_hälsopoäng = 10
    fiende_hälsopoäng = 15
    vapen_skada = 1
    tiger_skada = 4
    drake_skada = 5
    omtyckt += 1


Händer = (vapen_skada)
Kortsvärd = 1 + (vapen_skada)
Yxor = 2 + (vapen_skada)
Kroksabel = 3 + (vapen_skada)
Spjut = 4 + (vapen_skada)
Pilbåge = 3 + (vapen_skada)


def affären(romdaler):
    global vapen
    global spelare_vapen, vapen_attack
    global Kortsvärd, Yxor, Kroksabel, Spjut
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
                    spelare_vapen = 0
                    spelare_vapen = Kortsvärd
                    vapen_attack = "Kortsvärd"
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
                    spelare_vapen = 0
                    spelare_vapen = Yxor
                    vapen_attack = "Yxor"
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
                    spelare_vapen = 0
                    spelare_vapen = Kroksabel
                    vapen_attack = "Kroksabel"
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
                    spelare_vapen = 0
                    spelare_vapen = Spjut
                    vapen_attack = "Spjut"
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
#################################
vapen_attack = "Spjut"          #
spelare_vapen = Spjut           #
#################################



if vapen_attack == "Kortsvärd":
    vapen_träffchans = "(Träffchans(6/10))"
elif vapen_attack == "Yxor":
    vapen_träffchans = "(Träffchans(5/10))"
elif vapen_attack == "Kroksabel":
    vapen_träffchans = "(Träffchans(4/10))"
elif vapen_attack == "Spjut":
    vapen_träffchans = "(Träffchans(2/10))"



def träff():
    global vapen_träffchans, vapen_attack, träffar, fiende_hälsopoäng
    odds = 0
    if vapen_attack == "Kortsvärd":
        odds = random.randint(1, 10)
        if odds == 1 or odds == 3 or odds == 5 or odds == 7 or odds == 9 or odds == 10:
            träffar = True
            if gore == True:
                print("Du träffar din fiende med kortsvärdet, och det skär djupt in i fiendens mage, där blod sprutar och du ser din fiendes\n magsäck, och magsyran rinner ut i din fiendes kropp och fräter.")
                fiende_hälsopoäng -= spelare_vapen
            elif gore == False:
                print("Du träffar din fiende och fienden skriker till av smärta.")
                fiende_hälsopoäng -= spelare_vapen
        else:
            träffar = False
            print("Du missar din fiende.")
    elif vapen_attack == "Yxor":
        odds = random.randint(1, 2)
        if odds == 1:
            träffar = True
            if gore == True:
                print("Du träffar din fiende med yxorna, och de sjunker djupt in i fiendens bröst, där blod sprutar och du ser en av din fiendes\n punkterade lungor, som kämpar att få in luft.")
                fiende_hälsopoäng -= spelare_vapen
            elif gore == False:
                print("Du träffar din fiende och fienden skriker till av smärta.")
                fiende_hälsopoäng -= spelare_vapen
        else:
            träffar = False
            print("Du missar din fiende.")
    elif vapen_attack == "Kroksabel":
        odds = random.randint(1, 10)
        if odds == 1 or odds == 3 or odds == 7 or odds == 9:
            träffar = True
            if gore == True:
                print("Du träffar din fiende med kroksabeln, och det skär över halsen på din fiende.\nDet bildas snabbt en blodpöl och din fiende tappar medvetandet, men vaknar sedan snabbt upp för att slåss.")
                fiende_hälsopoäng -= spelare_vapen
            elif gore == False:
                print("Du träffar din fiende och fienden skriker till av smärta.")
                fiende_hälsopoäng -= spelare_vapen
        else:
            träffar = False
            print("Du missar din fiende.")
    elif vapen_attack == "Spjut":
        odds = random.randint(1, 5)
        if odds == 1 or odds == 3:
            träffar = True
            if gore == True:
                print("Du träffar din fiende med spjutet, och du spetsar din fiende som en flagga. Blodet regnar ner på dig och din fiendes inälvor flyter ut på marken.\nFörvånadsvärt nog så hoppas fienden av ditt spjut och gör sig redo att anfalla.")
                fiende_hälsopoäng -= spelare_vapen
            elif gore == False:
                print("Du träffar din fiende och fienden skriker till av smärta.")
                fiende_hälsopoäng -= spelare_vapen
        else:
            träffar = False
            print("Du missar din fiende.")



print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
fienden = random.choice(fiende)
kejsaren = random.choice(kejsaren_närvarande)
if fienden == "Gladiator":
    gladiatorns_vapen_för_striden = random.choice(gladiatorns_vapen)


def ai():
    global fienden, gladiatorns_vapen_för_striden, spelare_hälsopoäng, vapen_skada, spelare_vapen
    if fienden == "Gladiator":
        if svårighet == (1):
            if gladiatorns_vapen_för_striden == "ett Kortsvärd":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 5 or ai_träffar == 7 or ai_träffar == 9 or ai_träffar == 10:
                    if gore == True:
                        print("Du blir träffad av din fiende och blodet börjar rinna från din mun. Du samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kortsvärd
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kortsvärd
                else:
                    print("Du parerar din fiendes kortsvärd och returnerar med en egen attack, men du blir parerad.")
            elif gladiatorns_vapen_för_striden == "en Kroksabel":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 7 or ai_träffar == 9:
                    if gore == True:
                        print("Du blir träffad av din fiende och blodet börjar sprutar från ditt sår. Du samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kroksabel
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kroksabel
                else:
                    print("Du aktar dig för din fiendes kroksabel och ställer dig i en attack position.")
            elif gladiatorns_vapen_för_striden == "ett Spjut":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 3 or ai_träffar == 7:
                    if gore == True:
                        print("Du blir träffad av din fiende och du börjar bli spetsad.Du tar dig loss och samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Spjut
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Spjut
                else:
                    print("Du hoppar bort från din fiendes spjut och tar dig in för att skicka en farlig motattack.")
            elif gladiatorns_vapen_för_striden == "en Pilbåge":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 7:
                    if gore == True:
                        print("Du blir träffad av en pil och blod flyter ut från ditt sår. Du samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Pilbåge
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Pilbåge
                else:
                    print("Du duckar för pilen och din fiende tittar på dig förskräckt medan han försöker ta fram en ny pil.\nDu närmar dig för att anfalla.")
        elif svårighet == (2):
            if gladiatorns_vapen_för_striden == "ett Kortsvärd":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 5 or ai_träffar == 7 or ai_träffar == 9 or ai_träffar == 10:
                    if gore == True:
                        print("Du blir träffad av din fiende och blodet börjar rinna från din mun. Du samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kortsvärd
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kortsvärd
                else:
                    print("Du parerar din fiendes kortsvärd och returnerar med en egen attack, men du blir parerad.")
            elif gladiatorns_vapen_för_striden == "en Kroksabel":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 7 or ai_träffar == 9:
                    if gore == True:
                        print("Du blir träffad av din fiende och blodet börjar sprutar från ditt sår. Du samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kroksabel
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kroksabel
                else:
                    print("Du aktar dig för din fiendes kroksabel och ställer dig i en attack position.")
            elif gladiatorns_vapen_för_striden == "ett Spjut":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 3 or ai_träffar == 7:
                    if gore == True:
                        print("Du blir träffad av din fiende och du börjar bli spetsad.Du tar dig loss och samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Spjut
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Spjut
                else:
                    print("Du hoppar bort från din fiendes spjut och tar dig in för att skicka en farlig motattack.")
            elif gladiatorns_vapen_för_striden == "en Pilbåge":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 7:
                    if gore == True:
                        print("Du blir träffad av en pil och blod flyter ut från ditt sår. Du samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Pilbåge
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Pilbåge
                else:
                    print("Du duckar för pilen och din fiende tittar på dig förskräckt medan han försöker ta fram en ny pil.\nDu närmar dig för att anfalla.")
        elif svårighet == (3):
            if gladiatorns_vapen_för_striden == "ett Kortsvärd":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 5 or ai_träffar == 7 or ai_träffar == 9 or ai_träffar == 10:
                    if gore == True:
                        print("Du blir träffad av din fiende och blodet börjar rinna från din mun. Du samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kortsvärd
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kortsvärd
                else:
                    print("Du parerar din fiendes kortsvärd och returnerar med en egen attack, men du blir parerad.")
            elif gladiatorns_vapen_för_striden == "en Kroksabel":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 7 or ai_träffar == 9:
                    if gore == True:
                        print("Du blir träffad av din fiende och blodet börjar sprutar från ditt sår. Du samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kroksabel
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Kroksabel
                else:
                    print("Du aktar dig för din fiendes kroksabel och ställer dig i en attack position.")
            elif gladiatorns_vapen_för_striden == "ett Spjut":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 3 or ai_träffar == 7:
                    if gore == True:
                        print("Du blir träffad av din fiende och du börjar bli spetsad.Du tar dig loss och samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Spjut
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Spjut
                else:
                    print("Du hoppar bort från din fiendes spjut och tar dig in för att skicka en farlig motattack.")
            elif gladiatorns_vapen_för_striden == "en Pilbåge":
                ai_träffar = random.randint(1, 10)
                if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 7:
                    if gore == True:
                        print("Du blir träffad av en pil och blod flyter ut från ditt sår. Du samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Pilbåge
                    else:
                        print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                        spelare_hälsopoäng -= Pilbåge
                else:
                    print("Du duckar för pilen och din fiende tittar på dig förskräckt medan han försöker ta fram en ny pil.\nDu närmar dig för att anfalla.")
    elif fienden == "Tiger":
        ai_träffar = random.randint(1, 4)
        if ai_träffar == 1 or ai_träffar == 4:
            if gore == True:
                print("Du blir träffad av tigerns klor och blod sprutar ut på marken som tigern slickar på, du gör dig redo att attackera.")
                spelare_hälsopoäng -= tiger_skada
            else:
                print("Du blir träffad av tigerns klor, du faller bak men gör dig redo att anfalla.")
        else:
            print("Du undvek tigern och närmar dig besten för att attackera.")
    elif fienden == "Drake":
        ai_träffar = random.randint(1,10)
        if ai_träffar == 1:
            if gore == True:
                print("Draken andas ut eld på dig och du börjar brinna, du skriker av smärta,\nDu känner din hud smälta och ditt vapen går sönder.")
                spelare_hälsopoäng -= drake_skada
                spelare_vapen = Händer
            else:
                print("Draken andas ut eld på dig och du börjar brinna, du skriker av smärta och ditt vapen går sönder.")
                spelare_hälsopoäng -= drake_skada
                spelare_vapen = Händer
        else:
            print("Du undvek drakens eld och går nära för att anfalla.")
        
            
        

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



def röstsystem():
    global omtyckt, is_player_alive
    ute_ur_spelet = 0
    kejsaren_händelser = ["Mutad", "Struntar"]
    if omtyckt < 5:
        chans = "75%"
    elif omtyckt > 5 and omtyckt < 10:
        chans = "50%"
    elif omtyckt > 10 and omtyckt < 20:
        chans = "25%"
    elif omtyckt > 20:
        chans = "10%"
    if kejsaren == "närvarande!":
        print("Kejsaren ställer sig upp för att fighten är nu på sin tjugonde minut.\nPubliken vet vad som händer nu, och börjar utropa deras favorit.")        
        print("Du har" + Fore.GREEN + str(omtyckt) + Fore.RESET + "omtyckthetspoäng hos publiken, vilket innebär en" + Fore.RED + (chans) + Fore.RESET + "att bli utröstad.")
        händer_nåt = random.randint(1, 3)
        if händer_nåt == 2:
            vad_händer = random.choice(kejsaren_händelser)
            if vad_händer == "Mutad":
                ...########################################################
        
        print("Kejsaren sticker ut sin hand för att bestämma om du får vara kvar eller inte...")

        time.sleep(5)
        if chans == "75%":
            ute_ur_spelet = random.randint(1,100)
            if ute_ur_spelet < 76:
                print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.\nDu vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner\n är publiken som jublar åt din fiende.")
                is_player_alive = False
            else:
                print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")
        elif chans == "50%":
            ute_ur_spelet = random.randint(1,100)
            if ute_ur_spelet < 51:
                print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.\nDu vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner\n är publiken som jublar åt din fiende.")
                is_player_alive = False
            else:
                print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")
        elif chans == "25%":
            ute_ur_spelet = random.randint(1,100)
            if ute_ur_spelet < 26:
                print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.\nDu vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner\n är publiken som jublar åt din fiende.")
                is_player_alive = False
            else:
                print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")
        elif chans == "10%":
            ute_ur_spelet = random.randint(1,100)
            if ute_ur_spelet < 11:
                print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.\nDu vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner\n är publiken som jublar åt din fiende.")
                is_player_alive = False
            else:
                print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")
    else:
        print("Publiken har tröttnat och vill rösta.")
        print("Du har" + Fore.GREEN + str(omtyckt) + Fore.RESET + "omtyckthetspoäng hos publiken, vilket innebär en" + Fore.RED + (chans) + Fore.RESET + "att bli utröstad.")
        if chans == "75%":
            ute_ur_spelet = random.randint(1, 100)
            if ute_ur_spelet < 76:
                print("Publiken röstar...")
                time.sleep(3)
                print("Och du får de flesta rösterna, du blir utröstad och bort buad från arenan. Du kommer aldrig kunna visa dig igen, och får leva som slav resten av ditt liv.")
                is_player_alive = False
            else:
                print("Publiken röstar...")
                time.sleep(3)
                print("Och din motståndare får de flesta rösterna! Han blir utröstad och blir bort buad från arenan.")
        elif chans == "50%":
            ute_ur_spelet = random.randint(1, 100)
            if ute_ur_spelet < 51:
                print("Publiken röstar...")
                time.sleep(3)
                print("Och du får de flesta rösterna, du blir utröstad och bort buad från arenan. Du kommer aldrig kunna visa dig igen, och får leva som slav resten av ditt liv.")
                is_player_alive = False
            else:
                print("Publiken röstar...")
                time.sleep(3)
                print("Och din motståndare får de flesta rösterna! Han blir utröstad och blir bort buad från arenan.")
        elif chans == "25%":
            ute_ur_spelet = random.randint(1, 100)
            if ute_ur_spelet < 26:
                print("Publiken röstar...")
                time.sleep(3)
                print("Och du får de flesta rösterna, du blir utröstad och bort buad från arenan. Du kommer aldrig kunna visa dig igen, och får leva som slav resten av ditt liv.")
                is_player_alive = False
            else:
                print("Publiken röstar...")
                time.sleep(3)
                print("Och din motståndare får de flesta rösterna! Han blir utröstad och blir bort buad från arenan.")
        elif chans == "10%":
            ute_ur_spelet = random.randint(1, 100)
            if ute_ur_spelet < 11:
                print("Publiken röstar...")
                time.sleep(3)
                print("Och du får de flesta rösterna, du blir utröstad och bort buad från arenan. Du kommer aldrig kunna visa dig igen, och får leva som slav resten av ditt liv.")
                is_player_alive = False
            else:
                print("Publiken röstar...")
                time.sleep(3)
                print("Och din motståndare får de flesta rösterna! Han blir utröstad och blir bort buad från arenan.")



while spelare_hälsopoäng > 0 and fiende_hälsopoäng > 0:
    träffar = False
    print(f"Runda {runda}")
    print("Du har " + Fore.GREEN + str(spelare_hälsopoäng) + Fore.RESET + " hälsopoäng kvar, och din motståndare har " + Fore.RED +  str(fiende_hälsopoäng) + Fore.RESET + " hälsopoäng kvar.")
    print(f"Du har {omtyckt} omtyckthetspoäng hos publiken.")
    
    print("Vad använder du för attack?\n(1)" + Fore.YELLOW + "Kvickt slag " + Fore.RESET + "(" + Fore.RED + str(vapen_skada) + Fore.RESET + ")" + "(Träffchans(7/10)\n(2)" + Fore.YELLOW + str(vapen_attack) + Fore.RESET + " (" + Fore.RED + str(spelare_vapen) + Fore.RESET + ")" + str(vapen_träffchans))
    attack_val = int(input("(1) eller (2):"))
    if attack_val == 1:
        slag = random.randint(1, 10)
        if slag != 1 or slag != 5 or slag != 10:
            träffar = True
            fiende_hälsopoäng -= vapen_skada
            if gore == True:
                print("Du träffar din fiende i bröstkorgen och du hör hur flera revben krossas inuti din fiendes kropp.\nDin fiende skriker till av smärta.")
            elif gore == False:
                print("Du träffar ditt slag och din fiende flämtar till.")
        else:
            träffar = False
            print("Du missar din fiende.")
    elif attack_val == 2:
        träff()
    
    print("Din fiende förbereder sig för att anfalla dig...")
    ai()

    draken_kommer = random.randint(1,100)
    if draken_kommer < 5:
        ...

    input("")

    runda += 1
    if runda > 20:
        röstsystem()
affären(romdaler)