from pickle import FALSE
import random
import time
import os
from colorama import Fore, Style
from playsound3 import playsound
is_player_alive = True
gore = False
load = 0
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



for i in range(100):
    print(f"Loading ({load}%)")
    load += 1
    time.sleep(0.025)
    clear_screen()


sound = playsound("C:/Gladiatorerna/Meny.mp4", block=False)

print("")
print(Fore.RED + Style.BRIGHT + "BLOOD AND HONOR\n")
menu_choice = 0
times = 0
gladiator = 0
svårighet = 2
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
spelare_vapen = None
namn = None
musik = True

vapen_träffchans = None
träffar = False

omtyckt = 0
fiende_omtyckthet = 0

vunna_fighter = 0



    


#Så länge som spelaren inte klickat på 5 för att börja spela, så är menyn igång
while menu_choice != ("5"):
    print(Fore.RESET + Style.BRIGHT + "===============================================================================================================================")
    print(Style.BRIGHT + Fore.WHITE + "Spelmeny\n" + Style.RESET_ALL)
    menu_choice = input(Fore.RESET + "1 för att sätta på eller av Gore(Blodiga effekter)\n" 
    "2 för att välja svårighetsgrad \n3 för att välja karaktär \n4 för att sätta på/av musik\n5 för att spela\n:")
    if menu_choice == ("1"):
        sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
        time.sleep(0.7)
        gore_choice = input(f"Gore är på {gore}.\nVill du ha gore (På) eller (Av)?")
        if gore_choice == ("På") or gore_choice == ("på") or gore_choice == ("ja"):
            sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
            time.sleep(0.7)
            gore = True
            print("Gore är nu (På).")
        else:
            sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
            time.sleep(0.7)
            gore = False
            print("Gore är nu (Av).")
            print(" ")
        input("Tryck valfri tangent för att komma tillbaka till menyn...\n")

    if menu_choice == ("2"):
        sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
        time.sleep(0.7)
        print("Svårighetsgraderna är (lätt), (medel), (expert).")
        svårighet = input("Vilken svårighet vill du ha?").lower()
        if svårighet == ("lätt"):
            sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
            time.sleep(0.7)
            svårighet = (1)
            print("Svårighetsgraden är nu på lätt")
        elif svårighet == ("medel"):
            sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
            time.sleep(0.7)
            svårighet = (2)
            print("Svårighetsgraden är nu på medel")
        elif svårighet == ("expert"):
            sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
            time.sleep(0.7)
            svårighet = (3)
            print("Svårighetsgraden är nu på expert")
        else:
            sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
            time.sleep(0.7)
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
        sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
        time.sleep(0.7)
        kön_val = input("Vill du vara man eller kvinna?")
        sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
        time.sleep(0.7)
        if kön_val == "man":
            print("Välj en av följande gladiatorer:")
            print("1. Bobius Bobiusson\nEn vildman i 20 års åldern, tagen som slav från den nordesta toppen av romarriket, är fylld av hat och ilska,\n" \
            "redo att ta ut den på alla som kommer i hans väg...")
            print("Egenskaper:\n" + Fore.GREEN + "+ Är skicklig med yxor\n+ Går in i berserkagång ibland och gör mer skada\n" + Fore.RED + "- Kan i sin berserkagång råka skada sig själv\n\n" + Fore.RESET)

            print("2. Maximus Decimus Meridius\nEn äldre romersk general som blivit förråd och fått sin familj mördad. " \
            "Han är redo att ge igen mot allt och alla som förstört honom.")
            print("Egenskaper:\n" + Fore.GREEN + "+ Är skicklig med kortsvärd\n+ Ger ibland iväg ett vrål, som sänker fiendens moral, som sänker deras träffchans\n" + Fore.RED + "- På grund av sin ålder, är långsammare och gör mindre skada.\n\n" + Fore.RESET)

            print("3. Egen\n Inga fördelar eller nackdelar")
            gladiator = input("Välj din gladiator(1, 2 eller 3)")
            sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
            time.sleep(0.7)

            if gladiator == "1":
                gladiator = ("Bobius Bobiusson")
            elif gladiator == "2":
                gladiator = ("Maximus Decimus Meridius")
            elif gladiator == "3":
                gladiator = input("Vad är ditt gladiator namn?")
            else:
                print("Det var inte ett val, du får Bobius Bobsson. Gör om detta ifall du vill ha en annan.")
                gladiator = ("Bobius Bobiusson")

            print(f"Du har just nu valt {gladiator} som din gladiator.")
            if gladiator == ("Bobius Bobiusson"):
                gladiator = (1)
            elif gladiator == ("Maximus Decimus Meridius"):
                gladiator = (2)
            else:
                gladiator = (3)
        elif kön_val == "kvinna":
            print("1. Berlinda Bobsson\nEn soldatkvinna från söder, tagen som slav är farlig med kroksablar, och förbluffar fiender med hennes snabbhet.\nHon är fast besluten att ta sig hem till södern.")
            print("Egenskaper:\n" + Fore.GREEN + "+ Är skicklig med kroksablar\n+ Är väldigt snabb, har ökad träffchans\n" + Fore.RED + "- Gör mindre skada på grund av gammal skada\n\n" + Fore.RESET)

            print("2. Emilia Neosdotter\nEn tjuv som tillslut tagits efter flera år av stölder och terrorisering.\nEmilia är väldigt gymnastisk och farlig på grund av hennes kunnighet inom stridskonst.")
            print("Egenskaper:\n" + Fore.GREEN + "+ Är skickligast utan vapen\n+ Är väldigt kvick, och är svårare att träffa\n" + Fore.RED + "- Gör mindre skada på grund av svaghet\n\n" + Fore.RESET)
            
            print("3. Egen\n Inga fördelar eller nackdelar")
            gladiator = input("Välj din gladiator(1, 2 eller 3)")
            sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
            time.sleep(0.7)

            if gladiator == "1":
                gladiator = ("Berlinda Bobsson")
            elif gladiator == "2":
                gladiator = ("Emilia Neosdotter")
            elif gladiator == "3":
                gladiator = input("Vad är ditt gladiator namn?")
            else:
                print("Det var inte ett val, du får Berlinda Bobsson. Gör om detta ifall du vill ha en annan.")
                gladiator = ("Berlinda Bobsson")

            print(f"Du har just nu valt {gladiator} som din gladiator.")

            if gladiator == ("Berlinda Bobsson"):
                gladiator = (3)
            elif gladiator == ("Emilia Neosdotter"):
                gladiator = (4)
            else:
                gladiator = (5)

        kön_val = None
        print(" ")
        input("Tryck valfri tangent för att komma tillbaka till menyn...\n")

    if menu_choice == "4":
        sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
        time.sleep(0.7)
        print("Vill du ha på musik? (På) eller (Av)")
        musik = input(":")
        sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
        time.sleep(0.7)
        if musik == "På" or musik == "på" or musik == "PÅ" or musik == "Ja" or musik == "ja" or musik == "JA":
            print("Musik är nu på.")
            musik = True
            
        else:
            print("Musik är nu av.")
            musik = False
        print(" ")
        input("Tryck valfri tangent för att komma tillbaka till menyn...\n")
        
    
    if menu_choice == "5":
        sound.stop()
        sound_5 = playsound("C:/Gladiatorerna/Val.mp4", block=False)
        time.sleep(0.7)
        load = 0
        for i in range(100):
            print(f"Loading ({load}%)")
            load += 1
            time.sleep(0.025)
            clear_screen()
        

    clear_screen()
        
#################################################################################################################################




#Här ställs hälsan för spelare, fiende och grund skada hos vapen in beroende på vilken svårighet man valde, 
#man får dessutom ett extra omtyckthets poäng om man valde expert, och man får ett extra poäng om man är namnlös, alltså inte valde någon gladiator.
#Här ställs det dessutom in hur många fighter man behöver vinna för att få sin frihet.
if svårighet == (1):
    spelare_hälsopoäng = 20
    fiende_hälsopoäng = 10
    vapen_skada = 3
    tiger_skada = 2
    drake_skada = 3
    omtyckt = 0

elif svårighet == (2):
    spelare_hälsopoäng = 15
    fiende_hälsopoäng = 10
    vapen_skada = 2
    tiger_skada = 3
    drake_skada = 4
    omtyckt = 0

elif svårighet == (3):
    spelare_hälsopoäng = 10
    fiende_hälsopoäng = 10
    vapen_skada = 1
    tiger_skada = 4
    drake_skada = 5
    omtyckt = 1

#De olika vapnen som finns i spelet, här konfigueras deras skada utifrån svårigheten och karaktär plus deras grund skada.
if gladiator == (4):
    Händer = (vapen_skada) + 2
else:
    Händer = (vapen_skada)

if gladiator == (2):
    Kortsvärd = 1 + (vapen_skada) + 2
else:
    Kortsvärd = 1 + (vapen_skada)

if gladiator == (1):
    Yxor = 2 + (vapen_skada) + 2
else:
    Yxor = 2 + (vapen_skada)

if gladiator == (3):
    Kroksabel = 3 + (vapen_skada) + 2
else:
    Kroksabel = 3 + (vapen_skada)

Spjut = 4 + (vapen_skada)
Pilbåge = 3 + (vapen_skada)

#Här är definitionen av funktionen "Affären", efter varje fight så får man "romdaler", som är valutan i detta spelet. Och efter varje fight så kommer man hit, för att köpa något.
def affären():
    clear_screen()
    global vapen, romdaler, sound_3, sound_2, sound_4, is_player_alive, musik
    global spelare_vapen, vapen_attack
    global Kortsvärd, Yxor, Kroksabel, Spjut
    marknaden = "2"
    sound_3 = playsound("C:/Gladiatorerna/Affären.mp4", block=False)
    if musik == True:
        sound_4 = playsound("C:/Gladiatorerna/Affärmusik.mp4", block=False)
    while marknaden != "1":
        clear_screen()
        köp = "Nej"
        val = None
        print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
        print(Fore.RESET + Style.BRIGHT + "Affären")
        print(f"Du har {romdaler} romdaler kvar")
        print("")
        print(Style.RESET_ALL + "Vad vill du köpa idag?")
        print("1. Kortsvärd (20r)\n2. Yxor (30r)\n3. Kroksabel (40r)\n4. Spjut (50r)\n5. (Lämna marknaden)")
        val = input(":")
        if val == "1" or val == "kortsvärd" or val == "Kortsvärd":
            if vapen == "ett kortsvärd":
                print("1. Köp Kortsvärd (Du har redan detta vapnet)")
            elif romdaler > 19:
                print("1. Köp Kortsvärd (" + Fore.GREEN + "20" + Fore.RESET + ")?")
                köp = input("(ja) eller (nej):")
                if köp == "ja":
                    sound_2 = playsound("C:/Gladiatorerna/Köpnågot.mp4", block=False)
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
                    sound_2 = playsound("C:/Gladiatorerna/Köpnågot.mp4", block=False)
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
                    sound_2 = playsound("C:/Gladiatorerna/Köpnågot.mp4", block=False)
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
                    sound_2 = playsound("C:/Gladiatorerna/Köpnågot.mp4", block=False)
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
        
        elif val == "porr" or val == "Porr" or val == "droger" or val == "drogas" or val == "människor" or val == "din mamma" or val == "mami" or val == "papi" or val == "dih" or val == "strap-on":
            is_player_alive = False
            print("Butiksvärden blir förolämpad av ditt svar och slår ihjäl dig. Vilken lättkränkt man.")
            time.sleep(5)
            break

    
        marknaden = (input("Om du vill lämna marknaden tryck (1), om du vill fortsätta tryck (2)"))
        print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
    clear_screen()
    sound_4.stop()

#################################
vapen_attack = "Händer"         #     Vilket vapen man börjar med.
spelare_vapen = Händer          #
#################################


#Träffchansen som skrivs ut inom while-loopen när det är fight
if vapen_attack == "Kortsvärd":
    vapen_träffchans = "(Träffchans(6/10))"
elif vapen_attack == "Yxor":
    vapen_träffchans = "(Träffchans(5/10))"
elif vapen_attack == "Kroksabel":
    vapen_träffchans = "(Träffchans(4/10))"
elif vapen_attack == "Spjut":
    vapen_träffchans = "(Träffchans(2/10))"


#Funktionen som kollar vilket vapen du har, räknar ut en random int, och kollar om du träffar
def träff():
    global vapen_träffchans, vapen_attack, träffar, fiende_hälsopoäng, vunna_fighter, state_ai
    odds = 0

    if vapen_attack == "Kortsvärd":
        odds = random.randint(1, 10)

        if odds == 1 or odds == 3 or odds == 5 or odds == 7 or odds == 9 or odds == 10:
            träffar = True

            if gore == True:
                print("Du träffar din fiende med kortsvärdet, och det skär djupt in i fiendens mage, där blod sprutar och du ser din fiendes\n magsäck, och magsyran rinner ut i din fiendes kropp och fräter.")
                fiende_hälsopoäng -= spelare_vapen
                print("Din fiende backar defensivt och ställer sig stadigt.")
                state_ai = "defensiv"

            elif gore == False:
                print("Du träffar din fiende och fienden skriker till av smärta.")
                fiende_hälsopoäng -= spelare_vapen
                print("Din fiende backar defensivt och ställer sig stadigt.")
                state_ai = "defensiv"

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
                print("Din fiende backar defensivt och ställer sig stadigt.")
                state_ai = "defensiv"

            elif gore == False:
                print("Du träffar din fiende och fienden skriker till av smärta.")
                fiende_hälsopoäng -= spelare_vapen
                print("Din fiende backar defensivt och ställer sig stadigt.")
                state_ai = "defensiv"

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
                print("Din fiende backar defensivt och ställer sig stadigt.")
                state_ai = "defensiv"

            elif gore == False:
                print("Du träffar din fiende och fienden skriker till av smärta.")
                fiende_hälsopoäng -= spelare_vapen
                print("Din fiende backar defensivt och ställer sig stadigt.")
                state_ai = "defensiv"

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
                print("Din fiende backar defensivt och ställer sig stadigt.")
                state_ai = "defensiv"

            elif gore == False:
                print("Du träffar din fiende och fienden skriker till av smärta.")
                fiende_hälsopoäng -= spelare_vapen
                print("Din fiende backar defensivt och ställer sig stadigt.")
                state_ai = "defensiv"

        else:
            träffar = False
            print("Du missar din fiende.")








#Här bestäms det inför varje fight vilken motståndare man möter, om det är en gladiatior isåfall vilket vapen, och om kejsaren är där eller inte.
print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
fienden = random.choice(fiende)
kejsaren = random.choice(kejsaren_närvarande)
if fienden == "Gladiator":
    gladiatorns_vapen_för_striden = random.choice(gladiatorns_vapen)

återattack = 0
#Här beräknas det om ai:n får in en träff på spelaren, beroende på vilken fiende det är och vilket vapen den använder
def ai():
    global fienden, gladiatorns_vapen_för_striden, spelare_hälsopoäng, vapen_skada, spelare_vapen, fiende_omtyckthet, gladiator_attack, state_ai, återattack
    if fienden == "Gladiator":
        if svårighet == (1):
            gladiator_attack = random.randint(1,3)
            if gladiator_attack == 3:
                fiende_briljera = random.randint(1, 10)
                if fiende_briljera != 1 or fiende_briljera != 5 or fiende_briljera != 8:
                    fiende_omtyckthet += 2
                    print("Din fiende hånar dig samtidigt som hen svingar runt sitt vapen och dansar.")
                    print("Du känner en vrede växa inom dig.")
                else:
                    fiende_omtyckthet -= 2
                    print("Din fiende börjar sivnga runt sitt vapen och hånar dig, men tappar sitt vapen!")
                    print("Du skäms för din motståndare och likaså publiken.")
            else:
                if gladiatorns_vapen_för_striden == "ett Kortsvärd":
                    ai_träffar = random.randint(1, 10)
                    if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 5 or ai_träffar == 7 or ai_träffar == 9 or ai_träffar == 10:
                        if gore == True: #Här kollar systemet om och om igen vilken beskrivning den ska ge beroende på statusen av Gore inställningen
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
            gladiator_attack = random.randint(1,3)
            if gladiator_attack == 3:
                fiende_briljera = random.randint(1, 10)
                if fiende_briljera != 1 or fiende_briljera != 5 or fiende_briljera != 8 or fiende_briljera != 10:
                    fiende_omtyckthet += 2
                    print("Din fiende hånar dig samtidigt som hen svingar runt sitt vapen och dansar.")
                    print("Du känner en vrede växa inom dig.")
                else:
                    fiende_omtyckthet -= 2
                    print("Din fiende börjar sivnga runt sitt vapen och hånar dig, men tappar sitt vapen!")
                    print("Du skäms för din motståndare och likaså publiken.")
            else:
                if gladiatorns_vapen_för_striden == "ett Kortsvärd":
                    ai_träffar = random.randint(1, 10)
                    if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 5 or ai_träffar == 7 or ai_träffar == 9 or ai_träffar == 10:
                        if gore == True:
                            print("Du blir träffad av din fiende och blodet börjar rinna från din mun. Du samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Kortsvärd
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                        else:
                            print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Kortsvärd
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                    else:
                        print("Du parerar din fiendes kortsvärd och returnerar med en egen attack, men du blir parerad.")
                        state_ai = "normal"
                        återattack = 0
                elif gladiatorns_vapen_för_striden == "en Kroksabel":
                    ai_träffar = random.randint(1, 10)
                    if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 7 or ai_träffar == 9:
                        if gore == True:
                            print("Du blir träffad av din fiende och blodet börjar sprutar från ditt sår. Du samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Kroksabel
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                        else:
                            print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Kroksabel
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                    else:
                        print("Du aktar dig för din fiendes kroksabel och ställer dig i en attack position.")
                        state_ai = "normal"
                        återattack = 0
                elif gladiatorns_vapen_för_striden == "ett Spjut":
                    ai_träffar = random.randint(1, 10)
                    if ai_träffar == 3 or ai_träffar == 7:
                        if gore == True:
                            print("Du blir träffad av din fiende och du börjar bli spetsad.Du tar dig loss och samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Spjut
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                        else:
                            print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Spjut
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                    else:
                        print("Du hoppar bort från din fiendes spjut och tar dig in för att skicka en farlig motattack.")
                        state_ai = "normal"
                        återattack = 0
                elif gladiatorns_vapen_för_striden == "en Pilbåge":
                    ai_träffar = random.randint(1, 10)
                    if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 7:
                        if gore == True:
                            print("Du blir träffad av en pil och blod flyter ut från ditt sår. Du samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Pilbåge
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                        else:
                            print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Pilbåge
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                    else:
                        print("Du duckar för pilen och din fiende tittar på dig förskräckt medan han försöker ta fram en ny pil.\nDu närmar dig för att anfalla.")
                        state_ai = "normal"
                        återattack = 0
        elif svårighet == (3):
            gladiator_attack = random.randint(1,3)
            if gladiator_attack == 3:
                fiende_briljera = random.randint(1, 10)
                if fiende_briljera != 1 or fiende_briljera != 5 or fiende_briljera != 8 or fiende_briljera != 10:
                    fiende_omtyckthet += 2
                    print("Din fiende hånar dig samtidigt som hen svingar runt sitt vapen och dansar.")
                    print("Du känner en vrede växa inom dig.")
                else:
                    fiende_omtyckthet -= 2
                    print("Din fiende börjar sivnga runt sitt vapen och hånar dig, men tappar sitt vapen!")
                    print("Du skäms för din motståndare och likaså publiken.")
            else:
                if gladiatorns_vapen_för_striden == "ett Kortsvärd":
                    ai_träffar = random.randint(1, 10)
                    if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 5 or ai_träffar == 7 or ai_träffar == 9 or ai_träffar == 10:
                        if gore == True:
                            print("Du blir träffad av din fiende och blodet börjar rinna från din mun. Du samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Kortsvärd
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                        else:
                            print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Kortsvärd
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                    else:
                        print("Du parerar din fiendes kortsvärd och returnerar med en egen attack, men du blir parerad.")
                        state_ai = "normal"
                        återattack = 0
                elif gladiatorns_vapen_för_striden == "en Kroksabel":
                    ai_träffar = random.randint(1, 10)
                    if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 7 or ai_träffar == 9:
                        if gore == True:
                            print("Du blir träffad av din fiende och blodet börjar sprutar från ditt sår. Du samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Kroksabel
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                        else:
                            print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Kroksabel
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                    else:
                        print("Du aktar dig för din fiendes kroksabel och ställer dig i en attack position.")
                        state_ai = "normal"
                        återattack = 0
                elif gladiatorns_vapen_för_striden == "ett Spjut":
                    ai_träffar = random.randint(1, 10)
                    if ai_träffar == 3 or ai_träffar == 7:
                        if gore == True:
                            print("Du blir träffad av din fiende och du börjar bli spetsad.Du tar dig loss och samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Spjut
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                        else:
                            print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Spjut
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                    else:
                        print("Du hoppar bort från din fiendes spjut och tar dig in för att skicka en farlig motattack.")
                        state_ai = "normal"
                        återattack = 0
                elif gladiatorns_vapen_för_striden == "en Pilbåge":
                    ai_träffar = random.randint(1, 10)
                    if ai_träffar == 1 or ai_träffar == 3 or ai_träffar == 7:
                        if gore == True:
                            print("Du blir träffad av en pil och blod flyter ut från ditt sår. Du samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Pilbåge
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                        else:
                            print("Du blir träffad av din fiende, men samlar dig för att slå tillbaka.")
                            spelare_hälsopoäng -= Pilbåge
                            state_ai = "aggressiv"
                            if återattack == 2:
                                återattack = 0
                                state_ai = "normal"
                            else:
                                print("Din fiende blir kaxig och attackerar igen.")
                                återattack += 1
                                time.sleep(5)
                                ai()
                    else:
                        print("Du duckar för pilen och din fiende tittar på dig förskräckt medan han försöker ta fram en ny pil.\nDu närmar dig för att anfalla.")
                        state_ai = "normal"
                        återattack = 0
                    #Här kollar systemet om fienden är en tiger, och isåfall om den ska träffa spelaren
    elif fienden == "Tiger":
        ai_träffar = random.randint(1, 4)
        if ai_träffar == 1 or ai_träffar == 4:
            if gore == True:
                print("Du blir träffad av tigerns klor och blod sprutar ut på marken som tigern slickar på, du gör dig redo att attackera.")
                spelare_hälsopoäng -= tiger_skada
                state_ai = "aggressiv"
                if återattack == 2:
                    återattack = 0
                    state_ai = "normal"
                else:
                    print("Din fiende blir kaxig och attackerar igen.")
                    återattack += 1
                    time.sleep(5)
                    ai()
            else:
                print("Du blir träffad av tigerns klor, du faller bak men gör dig redo att anfalla.")
                spelare_hälsopoäng -= tiger_skada
                state_ai = "aggressiv"
                if återattack == 2:
                    återattack = 0
                    state_ai = "normal"
                else:
                    print("Din fiende blir kaxig och attackerar igen.")
                    återattack += 1
                    time.sleep(5)
                    ai()

        else:
            print("Du undvek tigern och närmar dig besten för att attackera.")
            state_ai = "normal"
            återattack = 0
          #Under fighten så finns det en liten chans att en drake kommer och invaderar
    elif fienden == "Drake":
        ai_träffar = random.randint(1,10)
        if ai_träffar == 1:
            if gore == True:
                print("Draken andas ut eld på dig och du börjar brinna, du skriker av smärta,\nDin hud smälter och ditt vapen går sönder.")
                spelare_hälsopoäng -= drake_skada
                state_ai = "aggressiv"
                spelare_vapen = Händer
                if återattack == 2:
                    återattack = 0
                    state_ai = "normal"
                else:
                    print("Din fiende blir kaxig och attackerar igen.")
                    återattack += 1
                    time.sleep(5)
                    ai()
            else:
                print("Draken andas ut eld på dig och du börjar brinna, du skriker av smärta och ditt vapen går sönder.")
                spelare_hälsopoäng -= drake_skada
                state_ai = "aggressiv"
                spelare_vapen = Händer
                if återattack == 2:
                    återattack = 0
                    state_ai = "normal"
                else:
                    print("Din fiende blir kaxig och attackerar igen.")
                    återattack += 1
                    time.sleep(5)
                    ai()

        else:
            print("Du undvek drakens eld och går nära för att anfalla.")
            state_ai = "normal"
            återattack = 0
        
            
    
    

print("")




#Här är funktionen för hur röstsystemet fungerar, alltså vad som händer om fighten tar för lång tid, och beroende på om kejsaren är där eller inte, och vissa utfall av vad han gör när han är där, så händer olika saker:)
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
            if vad_händer == "Mutad":    #Här börjar händelsen för om kejsaren blir mutad av en affärsman
                print("Du ser en känd affärsman gå fram till kejsaren och ge honom någonting...")
                print("Kejsaren har blivit mutad! Din chans att bli utröstad har nu ökat med 50%!")
                print("")
                print("Kejsaren sticker ut sin hand för att bestämma om du får vara kvar eller inte...")
                time.sleep(5)

                if chans == "75%":
                    ute_ur_spelet = random.randint(1,100)
                    if ute_ur_spelet < 126:
                        print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                        print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som jublar åt din fiende.")
                        is_player_alive = False
                        
                    else:
                        print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

                elif chans == "50%":
                    ute_ur_spelet = random.randint(1,100)
                    if ute_ur_spelet < 101:
                        print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                        print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som jublar åt din fiende.")
                        is_player_alive = False

                    else:
                        print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

                elif chans == "25%":
                    ute_ur_spelet = random.randint(1,100)
                    if ute_ur_spelet < 76:
                        print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                        print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som jublar åt din fiende.")
                        is_player_alive = False

                    else:
                        print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

                elif chans == "10%":
                    ute_ur_spelet = random.randint(1,100)
                    if ute_ur_spelet < 61:
                        print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                        print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som jublar åt din fiende.")
                        is_player_alive = False

                    else:
                        print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")
                                 #Här börjar den versionen av kejsaren där kejsaren inte bryr sig om publiken och röstar för den som han tyckte var den bästa
            elif vad_händer == "Struntar":
                print("Kejsaren verkar inte bry sig om vad publiken tycker, och kommer göra som han tycker!")
                print("Det kan vara vad som helst!")

                if chans == "75%":
                    ute_ur_spelet = random.randint(1,100)
                    if ute_ur_spelet < 101:
                        print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                        print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som jublar åt din fiende.")
                        is_player_alive = False

                    else:
                        print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

                elif chans == "50%":
                    ute_ur_spelet = random.randint(1,100)
                    if ute_ur_spelet < 76:
                        print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                        print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som jublar åt din fiende.")
                        is_player_alive = False

                    else:
                        print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

                elif chans == "25%":
                    ute_ur_spelet = random.randint(1,100)
                    if ute_ur_spelet < 51:
                        print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                        print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som är tysta, de gillade dig.")
                        is_player_alive = False

                    else:
                        print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

                elif chans == "10%":
                    ute_ur_spelet = random.randint(1,100)
                    if ute_ur_spelet < 26:
                        print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                        print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som buar åt kejsaren.")
                        is_player_alive = False

                    else:
                        print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

                   
         #Här börjar den rättvisa versionen där kejsaren inte är mutad och faktiskt lyssnar på publiken.
        else:
            print("Kejsaren sticker ut sin hand för att bestämma om du får vara kvar eller inte...")

            time.sleep(5)
            if chans == "75%":
                ute_ur_spelet = random.randint(1,100)
                if ute_ur_spelet < 76:
                    print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                    print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som jublar åt din fiende.")
                    is_player_alive = False

                else:
                    print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

            elif chans == "50%":
                ute_ur_spelet = random.randint(1,100)
                if ute_ur_spelet < 51:
                    print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                    print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som jublar åt din fiende.")
                    is_player_alive = False

                else:
                    print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

            elif chans == "25%":
                ute_ur_spelet = random.randint(1,100)
                if ute_ur_spelet < 26:
                    print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")
                    print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som jublar åt din fiende.")
                    is_player_alive = False

                else:
                    print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

            elif chans == "10%":
                ute_ur_spelet = random.randint(1,100)
                if ute_ur_spelet < 11:
                    print("Kejsaren vänder sin hand med tummen neråt, och vakter går ut på arenan och släppar bort dig.")

                    print("Du vågar inte tänka på vad som kommer hända dig, och det sista du ser innan ljuset försvinner är publiken som buar åt kejsaren.")
                    is_player_alive = False

                else:
                    print("Kejsaren vänder sin hand med tummen uppåt, och du vinner fighten! Din motståndare blir utsläppad av vakter och publiken jublar.")

    else:
        print("Publiken har tröttnat och vill rösta.")
        print("Du har " + Fore.GREEN + str(omtyckt) + Fore.RESET + " omtyckthetspoäng hos publiken, vilket innebär en " + Fore.RED + (chans) + Fore.RESET + " att bli utröstad.\n")
        time.sleep(3)

        if chans == "75%":
            ute_ur_spelet = random.randint(1, 100)
            if ute_ur_spelet < 76:
                print("Publiken röstar...")
                time.sleep(6)
                print("Och du får de flesta rösterna, du blir utröstad och bort buad från arenan. Du kommer aldrig kunna visa dig igen, och får leva som slav resten av ditt liv.")
                is_player_alive = False

            else:
                print("Publiken röstar...")
                time.sleep(6)
                print("Och din motståndare får de flesta rösterna! Han blir utröstad och blir bort buad från arenan.")

        elif chans == "50%":
            ute_ur_spelet = random.randint(1, 100)
            if ute_ur_spelet < 51:
                print("Publiken röstar...")
                time.sleep(6)
                print("Och du får de flesta rösterna, du blir utröstad och bort buad från arenan. Du kommer aldrig kunna visa dig igen, och får leva som slav resten av ditt liv.")
                is_player_alive = False

            else:
                print("Publiken röstar...")
                time.sleep(6)
                print("Och din motståndare får de flesta rösterna! Han blir utröstad och blir bort buad från arenan.")

        elif chans == "25%":
            ute_ur_spelet = random.randint(1, 100)
            if ute_ur_spelet < 26:
                print("Publiken röstar...")
                time.sleep(6)
                print("Och du får de flesta rösterna, du blir utröstad och bort buad från arenan. Du kommer aldrig kunna visa dig igen, och får leva som slav resten av ditt liv.")
                is_player_alive = False

            else:
                print("Publiken röstar...")
                time.sleep(6)
                print("Och din motståndare får de flesta rösterna! Han blir utröstad och blir bort buad från arenan.")

        elif chans == "10%":
            ute_ur_spelet = random.randint(1, 100)
            if ute_ur_spelet < 11:
                print("Publiken röstar...")
                time.sleep(6)
                print("Och du får de flesta rösterna, du blir utröstad och bort buad från arenan. Du kommer aldrig kunna visa dig igen, och får leva som slav resten av ditt liv.")
                is_player_alive = False

            else:
                print("Publiken röstar...")
                time.sleep(6)
                print("Och din motståndare får de flesta rösterna! Han blir utröstad och blir bort buad från arenan.")

    input("")

sound_6 = playsound("C:/Gladiatorerna/Fight.mp3", block=False)
#Här är den allra första fighten, därför är det en annorlunda text, man möter inte en stor drake eller tiger sin första match, och kejsaren är inte närvarande för att man är okänd.
print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
print("Du går in i mäktiga Coloseum för första gången, och publiken iaktar dig misstänksamt, de känner inte igen dig.\nKejsaren är inte närvarande, och framför dig så ser du din första fiende, en Gladiator.")
print(f"Dina trasor till kläder fläktar i vinden, och {vapen} är vid din sida. Du och din motståndare är redo att slåss.")
print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
while spelare_hälsopoäng > 0 and fiende_hälsopoäng > 0:    #anpassad första fight, för att låta det vara lätt att komma in i spelet.
    träffar = False
    fienden = "Gladiator"
    gladiatorns_vapen_för_striden = "ett Spjut"
    print(f"Runda {runda}")
    print("Du har " + Fore.GREEN + str(spelare_hälsopoäng) + Fore.RESET + " hälsopoäng kvar, och din motståndare har " + Fore.RED +  str(fiende_hälsopoäng) + Fore.RESET + " hälsopoäng kvar.")
    print(f"Du har {omtyckt} omtyckthetspoäng hos publiken.")
                
    print("Vad använder du för attack?\n(1)" + Fore.YELLOW + "Kvickt slag " + Fore.RESET + "(Skada (" + Fore.RED + str(vapen_skada) + Fore.RESET + "))")
    attack_val = input(":")
    if attack_val == "1":
        slag = random.randint(1, 10)
        if slag != 1 or slag != 3 or slag != 5 or slag != 10:
            träffar = True
            fiende_hälsopoäng -= vapen_skada
            if gore == True:
                print("Du träffar din fiende i bröstkorgen och du hör hur flera revben krossas inuti din fiendes kropp.\nDin fiende skriker till av smärta.")
            elif gore == False:
                print("Du träffar ditt slag och din fiende flämtar till.")
        else:
            träffar = False
            print("Du missar din fiende.")
    else:
        print("Du stod kvar, defensivt och stabilt.")
    
    if fiende_hälsopoäng < 1:
        break

    print("Din fiende förbereder sig för att anfalla dig...")
    ai()


    input("")
    if spelare_hälsopoäng < 1:
        is_player_alive = False
    runda += 1
    if runda > 20:
        röstsystem()

    clear_screen()
sound_6.stop()
romdaler += 20
print("Du var så bra så du får ett kortsvärd av publiken!")
vapen_attack = "Kortsvärd"         
spelare_vapen = Kortsvärd 
vapen = "ett kortsvärd"
time.sleep(5)
#Här är själva fightfunktionen som den spelas om och om igen tills spelaren dör.
def fight():
    global träffar, fiende_hälsopoäng, runda, fiende, kejsaren, kejsaren_närvarande, gladiatorns_vapen, gladiatorns_vapen_för_striden, omtyckt, fiende_omtyckthet, is_player_alive, spelare_hälsopoäng, tiger_skada, drake_skada, vapen_skada, sound_6, fienden
    sound_6 = playsound("C:/Gladiatorerna/Fight.mp3", block=False)
    if svårighet == (1):
        spelare_hälsopoäng = 20
        fiende_hälsopoäng = 10
        vapen_skada = 3
        tiger_skada = 2
        drake_skada = 3
        omtyckt = 0

    elif svårighet == (2):
        spelare_hälsopoäng = 15
        fiende_hälsopoäng = 10
        vapen_skada = 2
        tiger_skada = 3
        drake_skada = 4
        omtyckt = 0

    elif svårighet == (3):
        spelare_hälsopoäng = 10 
        fiende_hälsopoäng = 10
        vapen_skada = 1
        tiger_skada = 4
        drake_skada = 5
        omtyckt = 1


    if vapen_attack == "Kortsvärd":
        vapen_träffchans = "(Träffchans(6/10))"
    elif vapen_attack == "Yxor":
        vapen_träffchans = "(Träffchans(5/10))"
    elif vapen_attack == "Kroksabel":
        vapen_träffchans = "(Träffchans(4/10))"
    elif vapen_attack == "Spjut":
        vapen_träffchans = "(Träffchans(2/10))"

    print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
    fienden = random.choice(fiende)
    kejsaren = random.choice(kejsaren_närvarande)
    if fienden == "Gladiator":
        gladiatorns_vapen_för_striden = random.choice(gladiatorns_vapen)

    if fienden == "Gladiator":
        print(f"Du går in i mäktiga Colosseum, publiken jublar och hejar fram dig. Framför dig så står en Gladiator med {gladiatorns_vapen_för_striden}!\nKejsaren är {kejsaren} Du och din motståndare är redo att slåss.") 
    else:
        print(f"Du går in i mäktiga Colosseum, publiken jublar och hejar fram dig. Framför dig så står en {fienden}!\nKejsaren är {kejsaren} Du och din motståndare är redo att slåss.")
    omtyckt = 0
    fiende_omtyckthet = 0
    runda = 1
    print(Fore.RESET + Style.BRIGHT + "==============================================================================================================================="+ Fore.RESET + Style.RESET_ALL)
    while spelare_hälsopoäng > 0 and fiende_hälsopoäng > 0:
        träffar = False
        print(f"Runda {runda}")
        print("Du har " + Fore.GREEN + str(spelare_hälsopoäng) + Fore.RESET + " hälsopoäng kvar, och din motståndare har " + Fore.RED +  str(fiende_hälsopoäng) + Fore.RESET + " hälsopoäng kvar.")
        print(f"Du har {omtyckt} omtyckthetspoäng hos publiken.")
        
        print("Vad använder du för attack?\n(1)" + Fore.YELLOW + "Kvickt slag " + Fore.RESET + "(Skada (" + Fore.RED + str(vapen_skada) + Fore.RESET + "))" + "(Träffchans(6/10)\n(2)" + Fore.YELLOW + str(vapen_attack) + Fore.RESET + " (Skada (" + Fore.RED + str(spelare_vapen) + Fore.RESET + "))" + str(vapen_träffchans))
        print("(3)" + Fore.YELLOW + "Briljera" + Fore.RESET + " (Briljera dig med en 6/10 chans att lyckas)")
        print("(4)" + Fore.YELLOW + "Ge upp" + Fore.RESET + "(Börjar röstningen direkt, högre chans för dig att åka ut)")
        attack_val = input("(1) eller (2) eller (3) eller (4):")
        if attack_val == "1":
            slag = random.randint(1, 10)
            if slag != 1 or slag != 3 or slag != 5 or slag != 10:
                träffar = True
                fiende_hälsopoäng -= vapen_skada
                if gore == True:
                    print("Du träffar din fiende i bröstkorgen och du hör hur flera revben krossas inuti din fiendes kropp.\nDin fiende skriker till av smärta.")
                elif gore == False:
                    print("Du träffar ditt slag och din fiende flämtar till.")
            else:
                träffar = False
                print("Du missar din fiende.")

            print("Din fiende förbereder sig för att anfalla dig...")
            ai()
        elif attack_val == "2":
            träff()
            print("Din fiende förbereder sig för att anfalla dig...")
            ai()
        elif attack_val == "3":
            briljera = 0
            briljera = random.randint(1, 10)
            if briljera != 1 or briljera != 3 or briljera != 5 or briljera !=7:
                omtyckt += random.randint(1, 3)
                print("Du börjar svinga runt ditt vapen och publiken jublar, din motståndare känner sig extremt hotad.")
            elif briljera == 2 or briljera == 4 or briljera == 6 or briljera == 8 or briljera == 9 or briljera == 10:
                print("Du tappar ditt vapen under din uppvisning och arenan blir tyst.")
                print("Din motståndare skäms för dig och ger dig tillbaka ditt vapen...")
                omtyckt -= random.randint(1, 3)

            print("Din fiende förbereder sig för att anfalla dig...")
            ai()
        elif attack_val == "4":
            runda = 20
            if svårighet == 1:
                omtyckt -= 10
            elif svårighet == 2:
                omtyckt -= 15
            elif svårighet == 3:
                omtyckt -= 20
        else:
            print("Du stod kvar, defensivt och stabilt.")
        
            print("Din fiende förbereder sig för att anfalla dig...")
            ai()

        draken_kommer = random.randint(1,100)
        if draken_kommer < 5 and fienden != "Drake":
            fienden = "Drake"
            clear_screen()
            print("Plötsligt under er fight så känner ni vinden avta i fart, och hör vingar fladdra!")
            print("Människor ute i staden skriker efter hjälp, och sedan ser du det...")
            input("")
            print("En Drake!!!")
            clear_screen()
            print("Draken landar i mitten av arenan och äter hastigt upp din fiende, och får sina ögon på dig.")
            print("Du måste slåss för ditt liv...")
            fiende_hälsopoäng = 30
            if svårighet == (1):
                spelare_hälsopoäng = 20
            elif svårighet == (2):
                spelare_hälsopoäng = 15
            elif svårighet == (3):
                spelare_hälsopoäng = 10 

        input("")
        if spelare_hälsopoäng < 1:
            is_player_alive = False
            print("Du dog på första nivån...")
            print("Fighting är inte gjort för alla...")
            print("(Starta om spelet)")
        runda += 1
        if runda > 19:
            röstsystem()
            break

        clear_screen()
    sound_6.stop()

affären()

while is_player_alive == True:

    fight()
    if is_player_alive == False:
        print("Du dog, medan du slogs för din frihet. Människor kommer ihåg dig, men kommer glömma dig inom några månader.")
        time.sleep(5)
        break
    else:
        print("Din fiende faller till marken helt livlös.")
        print("Du går ut ur arenan och går förbi affären, som du går in i...")
        time.sleep(5)
        vunna_fighter += 1
        romdaler += random.randint(10, 30)
    #Detta är systemet som kollar i slutet av varje match om spelaren har nått sitt mål och har klarat spelet.
    if svårighet == (1) and vunna_fighter == 5:
        print("Du hindras av kejsaren när du ska gå in i affären, och du får reda på att han har\nobserverat dig under en längre tid nu,")
        print("och han vill släppa dig fri, som tack för det mod och den underhållning du bjudit på.")
        input("")
        print("Han ger dig dock ett val att du kan fortsätta vara en gladiator till dina sista dagar, med en lyxvilla med alla bekvämligheter du kan tänka\ndig.")
        print("Eller så kan du lämna och leva ett fritt liv precis så som du vill.")
        sista_val = input("Vad väljer du? (Stanna) eller (Lämna)").lower()
        if sista_val == "stanna":
            print("Kejsaren är nöjd med dig och hans vakter eskorterar dig till din villa.\nDu sover och vaknar upp, gör dig i ordning, och går till arenan.")
        elif sista_val == "lämna":
            print("Kejsaren tittar missnöjt på dig men respekterar ditt val. Vakterna låser upp den järnport som stod mellan dig och frihet.\nDu är äntligen, fri.")

    elif svårighet == (2) and vunna_fighter == 10:
        print("Du hindras av kejsaren när du ska gå in i affären, och du får reda på att han har\nobserverat dig under en längre tid nu,")
        print("och han vill släppa dig fri, som tack för det mod och den underhållning du bjudit på.")
        input("")
        print("Han ger dig dock ett val att du kan fortsätta vara en gladiator till dina sista dagar, med en lyxvilla med alla bekvämligheter du kan tänka\ndig.")
        print("Eller så kan du lämna och leva ett fritt liv precis så som du vill.")
        sista_val = input("Vad väljer du? (Stanna) eller (Lämna)").lower()
        if sista_val == "stanna":
            print("Kejsaren är nöjd med dig och hans vakter eskorterar dig till din villa.\nDu sover och vaknar upp, gör dig i ordning, och går till arenan.")
        elif sista_val == "lämna":
            print("Kejsaren tittar missnöjt på dig men respekterar ditt val. Vakterna låser upp den järnport som stod mellan dig och frihet.\nDu är äntligen, fri.")

    elif svårighet == (3) and vunna_fighter == 15:
        print("Du hindras av kejsaren när du ska gå in i affären, och du får reda på att han har\nobserverat dig under en längre tid nu,")
        print("och han vill släppa dig fri, som tack för det mod och den underhållning du bjudit på.")
        input("")
        print("Han ger dig dock ett val att du kan fortsätta vara en gladiator till dina sista dagar, med en lyxvilla med alla bekvämligheter du kan tänka\ndig.")
        print("Eller så kan du lämna och leva ett fritt liv precis så som du vill.")
        sista_val = input("Vad väljer du? (Stanna) eller (Lämna)").lower()
        if sista_val == "stanna":
            print("Kejsaren är nöjd med dig och hans vakter eskorterar dig till din villa.\nDu sover och vaknar upp, gör dig i ordning, och går till arenan.")
        elif sista_val == "lämna":
            print("Kejsaren tittar missnöjt på dig men respekterar ditt val. Vakterna låser upp den järnport som stod mellan dig och frihet.\nDu är äntligen, fri.")
    
    affären()   

if is_player_alive == True and sista_val == "stanna":
    while is_player_alive == True:
        fight()
        affären()