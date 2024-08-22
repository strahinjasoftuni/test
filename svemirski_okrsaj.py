import random  # Uvozimo modul random za generisanje nasumičnih brojeva


# Funkcija za generisanje nasumičnog broja u zadatom opsegu
def nasumican_broj(min_vrednost, max_vrednost):
    return random.randint(min_vrednost, max_vrednost)


# Funkcija koja simulira laserski napad
def laserski_napad():
    if nasumican_broj(1, 100) <= 80:  # 80% šansa za pogodak
        steta = nasumican_broj(10, 20)  # Nasumična šteta između 10 i 20
        print(f"Pogodak! Naneli ste {steta} štete neprijatelju.")
        return steta
    else:
        print("Promašaj! Niste pogodili neprijatelja.")
        return 0  # Vraćamo 0 ako je promašaj


# Funkcija koja simulira ispaljivanje rakete
def ispaliti_raketu(rakete):
    if rakete > 0:  # Proveravamo da li imamo raketa
        rakete -= 1  # Smanjujemo broj raketa za 1
        if nasumican_broj(1, 100) <= 90:  # 90% šansa za pogodak
            steta = nasumican_broj(30, 40)  # Nasumična šteta između 30 i 40
            print(f"Pogodak! Raketa je nanela {steta} štete neprijatelju.")
            return steta, rakete
        else:
            print("Promašaj! Raketa nije pogodila neprijatelja.")
            return 0, rakete
    else:
        print("Nemate više raketa!")
        return 0, rakete


# Funkcija koja simulira pokušaj bekstva
def pokusaj_bekstva():
    if nasumican_broj(1, 100) <= 50:  # 50% šansa za uspešno bekstvo
        print("Uspešno ste pobegli!")
        return True
    else:
        print("Bekstvo nije uspelo!")
        return False


# Funkcija za prikazivanje trenutnog statusa igre
def prikazi_status(sektor, energija_stita, rakete):
    print(f"\n--- Sektor {sektor}/5 ---")
    print(f"Energija štita: {energija_stita}")
    print(f"Rakete: {rakete}")


# Funkcija koja simulira borbu sa neprijateljem
def borba_sa_neprijateljem(energija_stita, rakete):
    neprijatelj_hp = 50  # Početni HP neprijatelja
    while neprijatelj_hp > 0 and energija_stita > 0:
        print(f"\nHP neprijatelja: {neprijatelj_hp}")
        print("Izaberite akciju:")
        print("1. Laserski napad")
        print("2. Ispaliti raketu")
        print("3. Pokušaj bekstva")

        akcija = input("Unesite broj akcije (1-3): ")

        if akcija == "1":
            neprijatelj_hp -= laserski_napad()
        elif akcija == "2":
            steta, rakete = ispaliti_raketu(rakete)
            neprijatelj_hp -= steta
        elif akcija == "3":
            if pokusaj_bekstva():
                return energija_stita, rakete, False
        else:
            print("Nevažeća akcija. Propuštate potez.")

        if neprijatelj_hp <= 0:
            print("Neprijateljski brod je uništen!")
            return energija_stita, rakete, True

        # Neprijatelj uzvraća udarac
        if nasumican_broj(1, 100) <= 70:  # 70% šansa da neprijatelj pogodi
            steta_neprijatelja = nasumican_broj(10, 15)
            energija_stita -= steta_neprijatelja
            print(f"Neprijatelj vas je pogodio i naneo {steta_neprijatelja} štete!")
        else:
            print("Neprijatelj je promašio!")

    return energija_stita, rakete, neprijatelj_hp <= 0


# Glavna funkcija igre
def igraj_svemirski_okrsaj():
    energija_stita = 100  # Početna energija štita
    rakete = 3  # Početni broj raketa
    unisteni_neprijatelji = 0  # Brojač uništenih neprijatelja

    # Prolazimo kroz 5 sektora
    for sektor in range(1, 6):
        prikazi_status(sektor, energija_stita, rakete)

        # Generišemo nasumičan događaj (80% šansa za pojavu neprijatelja)
        if nasumican_broj(1, 100) <= 80:
            print("\nNeprijateljski brod se pojavio!")
            energija_stita, rakete, pobeda = borba_sa_neprijateljem(energija_stita, rakete)
            if pobeda:
                unisteni_neprijatelji += 1
        else:
            print("Mirno ste prošli kroz ovaj sektor.")

        # Proveravamo da li je igra završena
        if energija_stita <= 0:
            print("Vaš štit je uništen! Igra je završena.")
            break

    # Kraj igre - prikazujemo rezultate
    if energija_stita > 0:
        print("\nČestitamo! Preživeli ste svih 5 sektora!")
    else:
        print("\nIgra je završena. Niste uspeli da preživite svih 5 sektora.")

    print(f"Uništili ste {unisteni_neprijatelji} neprijateljskih brodova.")


# Pokretanje igre
if __name__ == "__main__":
    igraj_svemirski_okrsaj()