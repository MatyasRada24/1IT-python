import time
ucet = 0
MEDIUMuser_life = 5
HARDuser_life = 3
print("-------------------------------------------------------")
print("Vítejte v AZkvízu!")
print("Za každou správnou otázku získáš peněžní odměnu.")
print("")
print("-------------------------------------------------------")
input("\nPro pokračování stiskněte ENTER. ")
EASYotazka1 = ("1. Jaké zvíře je největší na světě?")
EASYotazka2 = ("2. Kolik kontinentů je na Zemi?")
EASYotazka3 = ("3. Jak se jmenuje prezident České republiky(2025)?")
EASYotazka4 = ("4. Která planeta je nejblíže Slunci?")
EASYotazka5 = ("5. Jak se jmenuje hlavní město Německa?")
EASYotazka6 = ("6. Které moře omývá pobřeží Itálie?")
EASYotazka7 = ("7. Jak se jmenuje hympa ČR?")
EASYotazka8 = ("8. Kdo napsal dílo R.U.R.?")
EASYotazka9 = ("9. Jak se jmenuje slavná věž v Paříži?")
EASYotazka10 = ("10. Jak se jmenuje nejvyšší hora České republiky?")
EASYotazka11 = ("11. Kdo napsal dílo Babička?")
EASYotazka12 = ("12. Kolik nohou má pavouk?")
EASYotazka13 = ("13. Jak se jmenuje nejdelší řeka v České republice?")
EASYotazka14 = ("14. Jak se jmenuje proces, při kterém voda přechází v páru?")
EASYotazka15 = ("15. Jak se nazývá nejlidnatější země na světě?(2025)")

EASYodpoved1 = ("Plejtvák obrovský")
EASYodpoved2 = ("7")
EASYodpoved3 = ("Petr Pavel")
EASYodpoved4 = ("Merkur")
EASYodpoved5 = ("Berlín")
EASYodpoved6 = ("Středozemní moře")
EASYodpoved7 = ("Kde domov můj")
EASYodpoved8 = ("Karel Čapek")
EASYodpoved9 = ("Eiffelova věž")
EASYodpoved10 = ("Sněžka")
EASYodpoved11 = ("Božena Němcová")
EASYodpoved12 = ("8")
EASYodpoved13 = ("Vltava")
EASYodpoved14 = ("Vypařování")
EASYodpoved15 = ("Indie")


MEDIUMotazka1 = ("1. Jaký je chemický vzorec pro vodu?")
MEDIUMotazka2 = ("2. Kdo byl 1. prezident Československa?")
MEDIUMotazka3 = ("3. Kdy začala 2. světová válka?")
MEDIUMotazka4 = ("4. Kolik členů má Evropská unie?(2025)")
MEDIUMotazka5 = ("5. Jak se jmenuje hlavní město Kanady?")
MEDIUMotazka6 = ("6. Kdo napsal dílo Romeo a Julie?")
MEDIUMotazka7 = ("7. Který fyzik objevil zákon gravitace?")
MEDIUMotazka8 = ("8. Kdo složil českou hymnu?")
MEDIUMotazka9 = ("9. Jak se nazívá největší orgán v lidském těle?")
MEDIUMotazka10 = ("10. Který český vynálezce vynalezl lodní šroub?")
MEDIUMotazka11 = ("11. Jak se nazívá věda, která se zabívá mapami?")
MEDIUMotazka12 = ("12. Jakou přezdívku měl Jan Amos Komenský?")
MEDIUMotazka13 = ("13. Jak se nazívá nejvyšší hora světa?")
MEDIUMotazka14 = ("14. Jak dlouho trvala 30letá válka?")
MEDIUMotazka15 = ("15. Jak se jmenuje vojevůdce, které mu se jako jedinému povedlo dostat do Moskvy?")

MEDIUModpoved1 = ("H2O")
MEDIUModpoved2 = ("Tomáš Garrigue Masaryk")
MEDIUModpoved3 = ("1. září 1939")
MEDIUModpoved4 = ("27")
MEDIUModpoved5 = ("Ottawa")
MEDIUModpoved6 = ("William Shakespeare")
MEDIUModpoved7 = ("Isaac Newton")
MEDIUModpoved8 = ("Josef Kajetán Tyl")
MEDIUModpoved9 = ("Kůže")
MEDIUModpoved10 = ("František Křižík")
MEDIUModpoved11 = ("Kartografie")
MEDIUModpoved12 = ("Učitel národů")
MEDIUModpoved13 = ("Mount Everest")
MEDIUModpoved14 = ("30 let")
MEDIUModpoved15 = ("Napoleon Bonaparte")


HARDotazka1 = ("1. Jaký je vzorec pro výpočet obsahu obdélníku?")
HARDotazka2 = ("2. Jaká je jednotka elektrického proudu?")
HARDotazka3 = ("3. Jak se jmenuje největší světadíl?")
HARDotazka4 = ("4. Který spisovatel je autorem díla „1984“?")
HARDotazka5 = ("5. Jaký je latinský název člověka?")
HARDotazka6 = ("6. Jak se nazývá nejvyšší vrstva atmosféry?")
HARDotazka7 = ("7. Jak se jiným názvem nazývá schopnost organismu přizpůsobit se prostředí?")
HARDotazka8 = ("8. Jaký je hlavní minerál tvořící lidské kosti?")
HARDotazka9 = ("9. Co je základní jednotkou dědičnosti?")
HARDotazka10 = ("10. Jak se jmenuje největší český národní park?")
HARDotazka11 = ("11. Jak se jmenuje nejdelší řeka v Evropě?")
HARDotazka12 = ("12. Jaký jazyk používali staří Římané?")
HARDotazka13 = ("13. Jak se nazývá metoda studia starých písemností?")
HARDotazka14 = ("14. Vypočítej: -2*(3-5)**2 + 4 * (-1)**3")
HARDotazka15 = ("15. Co znamená zkratka DPH? ")

HARDodpoved1 = ("a*b")
HARDodpoved2 = ("Ampér")
HARDodpoved3 = ("Asie")
HARDodpoved4 = ("George Orwell")
HARDodpoved5 = ("Homo")
HARDodpoved6 = ("Exosféra")
HARDodpoved7 = ("Adaptace")
HARDodpoved8 = ("Vápník")
HARDodpoved9 = ("Gen")
HARDodpoved10 = ("Národní park Šumava")
HARDodpoved11 = ("Volha")
HARDodpoved12 = ("Latina")
HARDodpoved13 = ("Paleografie")
HARDodpoved14 = ("-12")
HARDodpoved15 = (" Daň z přidané hodnoty")

obtiznost = input(
    "Zvolte si obtížnost. EASY, MEDIUM, HARD:\n"
    "EASY - znalosti 5. třídy ZŠ.\n"
    "MEDIUM - znalosti 9. třídy ZŠ.\n"
    "HARD - znalosti 1. ročníku SŠ.\n"
    "HARDCORE - nejtěžší obtížnost.\n")
if obtiznost == "EASY" or obtiznost == "easy" or obtiznost == "E" or obtiznost == "e" or obtiznost == "Easy" or obtiznost == "eASY":
     print("Výborně! Tak pojďmě na to.")
     time.sleep(2)
     otazka1 = input(f"{EASYotazka1} ")
     if EASYodpoved1.lower() == otazka1.lower() or otazka1 == "plejtvak obrovsky":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved1}.")

     otazka2 = input(f"{EASYotazka2} ")
     if EASYodpoved2 == otazka2 or otazka2 == "sedum" or otazka2 == "sedm":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved2}.")
    
     otazka3 = input(f"{EASYotazka3} ")
     if EASYodpoved3.lower() == otazka3.lower():
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved3}.")
    
     otazka4 = input(f"{EASYotazka4} ")
     if EASYodpoved4.lower() == otazka4.lower():
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved4}.")
    
     otazka5 = input(f"{EASYotazka5} ")
     if otazka5 == EASYodpoved5 or otazka5 == "Berlin" or otazka5 == "berlín" or otazka5 == "berlin" or otazka5 == "bERLÍN" or otazka5 == "bERLIN":
             time.sleep(2)
             print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
             print("Získáváte 1000 Kč.")
             ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved5}.")

     otazka6 = input(f"{EASYotazka6} ")
     if otazka6 == EASYodpoved6 or otazka6 == "STŘEDOZEMNÍ MOŘE" or otazka6 == "stredozemni more" or otazka6 == "Stredozemni more" or otazka6 == "STREDOZEMNI MORE" or otazka6 == "Středozemní" or otazka6 == "Stredozemni" or otazka6 == "stredozemni" or otazka6 == "STŘEDOZEMNÍ":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved6}.")

     otazka7 = input(f"{EASYotazka7} ")
     if otazka7 == EASYodpoved7 or otazka7 == "KDE DOMOV MŮJ" or otazka7 == "kde domov muj" or otazka7 == "Kde domov muj" or otazka7 == "KDE DOMOV MUJ":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved7}.")

     otazka8 = input(f"{EASYotazka8} ")
     if otazka8 == EASYodpoved8 or otazka8 == "Karel Čapek" or otazka8 == "karel capek" or otazka8 == "Karel capek" or otazka8 == "KAREL ČAPEK":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved8}.")

     otazka9 = input(f"{EASYotazka9} ")
     if otazka9 == EASYodpoved9 or otazka9 == "Eiffelova věž" or otazka9 == "eiffelova vez" or otazka9 == "Eiffelova vez" or otazka9 == "Eiffelova Věž":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved9}.")

     otazka10 = input(f"{EASYotazka10} ")
     if otazka10 == EASYodpoved10 or otazka10 == "Sněžka" or otazka10 == "snezka" or otazka10 == "SNEŽKA" or otazka10 == "SNEZKA":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved10}.")

     otazka11 = input(f"{EASYotazka11} ")
     if otazka11 == EASYodpoved11 or otazka11 == "Božena Němcová" or otazka11 == "bozena nemcova" or otazka11 == "Bozena Nemcova" or otazka11 == "BOŽENA NĚMCOVÁ":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved11}.")

     otazka12 = input(f"{EASYotazka12} ")
     if otazka12 == EASYodpoved12 or otazka12 == "8" or otazka12 == "osm":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved12}.")

     otazka13 = input(f"{EASYotazka13} ")
     if otazka13 == EASYodpoved13 or otazka13 == "Vltava" or otazka13 == "vltava":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved13}.")

     otazka14 = input(f"{EASYotazka14} ")
     if otazka14 == EASYodpoved14 or otazka14 == "Vypařování" or otazka14 == "vypařování" or otazka14 == "vyparovani":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved14}.")

     otazka15 = input(f"{EASYotazka15} ")
     if otazka15 == EASYodpoved15 or otazka15 == "Indie" or otazka15 == "indie":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 1000 Kč.")
                ucet += 1000
     else:print(f"Je mi líto. Správná odpověď je {EASYodpoved15}.")
     print(f"Gratuluji! Došel jsi do konce AZkvízu a získal jsi {ucet} Kč.")


if obtiznost == "MEDIUM" or obtiznost == "medium" or obtiznost == "M" or obtiznost == "m" or obtiznost == "Medium" or obtiznost == "mEDIUM":
        otazka16 = input(f"{MEDIUMotazka1} ")
        if otazka16 == MEDIUModpoved1 or otazka16 == "h2o":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved1}.")

        otazka17 = input(f"{MEDIUMotazka2} ")
        if otazka17 == MEDIUModpoved2 or otazka17 == "Tomáš Garrigue Masaryk" or otazka17 == "tomas garrigue masaryk" or otazka17 == "Tomas Garrigue Masaryk" or otazka17 == "TOMÁŠ GARRIGUE MASARYK":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved2}.")
    
        otazka18 = input(f"{MEDIUMotazka3} ")
        if otazka18 == MEDIUModpoved3 or otazka18 == "1. září 1939" or otazka18 == "1.září 1939" or otazka18 == "1.9.1939":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved3}.")

        otazka19 = input(f"{MEDIUMotazka4} ")
        if otazka19 == MEDIUModpoved4 or otazka19 == "27" or otazka19 == "dvacet sedm" or otazka19 == "27 členů":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved4}.")

        otazka20 = input(f"{MEDIUMotazka5} ")
        if otazka20 == MEDIUModpoved5 or otazka20 == "Ottawa" or otazka20 == "ottawa" or otazka20 == "OTTAWA":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2x pěněz.")
            ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved5}.")

        otazka21 = input(f"{MEDIUMotazka6} ")
        if otazka21 == MEDIUModpoved6 or otazka21 == "William Shakespeare" or otazka21 == "william shakespeare" or otazka21 == "William Shakespeare":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved6}.")

        otazka22 = input(f"{MEDIUMotazka7} ")
        if otazka22 == MEDIUModpoved7 or otazka22 == "Isaac Newton" or otazka22 == "isaac newton" or otazka22 == "ISAAC NEWTON":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved7}.")

        otazka23 = input(f"{MEDIUMotazka8} ")
        if otazka23 == MEDIUModpoved8 or otazka23 == "Josef Kajetán Tyl" or otazka23 == "josef kajetan tyl" or otazka23 == "Josef Kajetan Tyl":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved8}.")

        otazka24 = input(f"{MEDIUMotazka9} ")
        if otazka24 == MEDIUModpoved9 or otazka24 == "Kůže" or otazka24 == "kuze" or otazka24 == "KŮŽE":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved9}.")

        otazka25 = input(f"{MEDIUMotazka10} ")
        if otazka25 == MEDIUModpoved10 or otazka25 == "František Křižík" or otazka25 == "frantisek krizik" or otazka25 == "Frantisek Krizik" or otazka25 == "FRANTIŠEK KŘIŽÍK":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2x pěněz.")
            ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved10}.")

        otazka26 = input(f"{MEDIUMotazka11} ")
        if otazka26 == MEDIUModpoved11 or otazka26 == "Kartografie" or otazka26 == "kartografie" or otazka26 == "KARTOGRAFIE":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved11}.")

        otazka27 = input(f"{MEDIUMotazka12} ")
        if otazka27 == MEDIUModpoved12 or otazka27 == "Učitel národů" or otazka27 == "ucitel narodu" or otazka27 == "Učitel Národů" or otazka27 == "UČITEL NÁRODŮ":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved12}.")

        otazka28 = input(f"{MEDIUMotazka13} ")
        if otazka28 == MEDIUModpoved13 or otazka28 == "Mount Everest" or otazka28 == "mount everest" or otazka28 == "MOUNT EVEREST":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet += 2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved13}.")

        otazka29 = input(f"{MEDIUMotazka14} ")
        if otazka29 == MEDIUModpoved14 or otazka29 == "30 let" or otazka29 == "30let" or otazka29 == "30 let trvala" or otazka29 == "30":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2000 Kč.")
            ucet +=2000
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved14}.")

        otazka30 = input(f"{MEDIUMotazka15} ")
        if otazka30 == MEDIUModpoved15 or otazka30 == "Napoleon Bonaparte" or otazka30 == "napoleon bonaparte" or otazka30 == "Napoleon Bonaparte":
            time.sleep(2)
            print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
            print("Získáváte 2x pěněz.")
            ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {MEDIUModpoved15}.")
        print(f"Gratuluji! Došel jsi do konce AZkvízu a získal jsi {ucet} Kč.")

if obtiznost == "HARD" or obtiznost == "hard" or obtiznost == "H" or obtiznost == "h" or obtiznost == "Hard" or obtiznost == "hARD":
        otazka31 = input(f"{HARDotazka1} ")
        if otazka31 == HARDodpoved1 or otazka31 == "a*b" or otazka31 == "ab":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 5000 Kč.")
                ucet += 5000
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved1}.")

        otazka32 = input(f"{HARDotazka2} ")
        if otazka32 == HARDodpoved2 or otazka32 == "Ampér" or otazka32 == "amper" or otazka32 == "AMPÉR" or otazka32 == "ampér":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Výborně! Od teďka za každou správnou odpověď dostáváte 2x.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved2}.")

        otazka33 = input(f"{HARDotazka3} ")
        if otazka33 == HARDodpoved3 or otazka33 == "Asie" or otazka33 == "asie" or otazka33 == "ASIE":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved3}.")

        otazka34 = input(f"{HARDotazka4} ")
        if otazka34 == HARDodpoved4 or otazka34 == "George Orwell" or otazka34 == "george orwell" or otazka34 == "George Orwell":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved4}.")

        otazka35 = input(f"{HARDotazka5} ")
        if otazka35 == HARDodpoved5 or otazka35 == "homo" or otazka35 == "HOMO":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved5}.")

        otazka36 = input(f"{HARDotazka6} ")
        if otazka36 == HARDodpoved6 or otazka36 == "Exosféra" or otazka36 == "exosfera" or otazka36 == "EXOSFÉRA":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet*= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved6}.")

        otazka37 = input(f"{HARDotazka7} ")
        if otazka37 == HARDodpoved7 or otazka37 == "Adaptace" or otazka37 == "adaptace" or otazka37 == "ADAPTACE":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved7}.")

        otazka38 = input(f"{HARDotazka8} ")
        if otazka38 == HARDodpoved8 or otazka38 == "Vápník" or otazka38 == "vápník" or otazka38 == "VÁPNÍK":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved8}.")

        otazka39 = input(f"{HARDotazka9} ")
        if otazka39 == HARDodpoved9 or otazka39 == "GEN" or otazka39 == "gen":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved9}.")

        otazka40 = input(f"{HARDotazka10} ")
        if otazka40 == HARDodpoved10 or otazka40 == "Národní park Šumava" or otazka40 == "narodni park sumava" or otazka40 == "Narodni park sumava" or otazka40 == "NÁRODNÍ PARK ŠUMAVA" or otazka40 == "šumava" or otazka40 == "ŠUMAVA":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved10}.")

        otazka41 = input(f"{HARDotazka11} ")
        if otazka41 == HARDodpoved11 or otazka41 == "Volha" or otazka41 == "volha" or otazka41 == "VOLHA":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved11}.")

        otazka42 = input(f"{HARDotazka12} ")
        if otazka42 == HARDodpoved12 or otazka42 == "Latina" or otazka42 == "latina" or otazka42 == "LATINA":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved12}.")

        otazka43 = input(f"{HARDotazka13} ")
        if otazka43 == HARDodpoved13 or otazka43 == "Paleografie" or otazka43 == "paleografie" or otazka43 == "PALEOGRAFIE":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved13}.")

        otazka44 = input(f"{HARDotazka14} ")
        if otazka44 == HARDodpoved14 or otazka44 == "-12":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved14}.")

        otazka45 = input(f"{HARDotazka15} ")
        if otazka45 == HARDodpoved15 or otazka45 == "Daň z přidané hodnoty" or otazka45 == "dan z pridane hodnoty" or otazka45 == "Dan z přidané hodnoty" or otazka45 == "DAN Z PŘIDANÉ HODNOTY":
                time.sleep(2)
                print("ANO. TO JE SPRÁVNÁ ODPOVĚĎ!")
                print("Získáváte 2x peněz.")
                ucet *= 2
        else:print(f"Je mi líto. Správná odpověď je {HARDodpoved15}.")

#Vylepšení obtížností: životy, nápovědy, Hardcore