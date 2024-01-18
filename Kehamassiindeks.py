print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis on sinu nimi?") 
print(nimi, ", oi kui ilus nimi!")
vastus = input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
try:
    if vastus == "1":
        pikkus =int (input("Pikkus: "))
        mass =float(input("Mass: "))
        indeks = mass /(0.01 * pikkus)**2
        print(nimi,"! Sinu keha indeks on:", indeks)
        if indeks < 16:
            print("Tervisele ohtlik alakaal")
        elif 16 < indeks <19:
            print("Alakaal") 
        elif 19 < indeks < 25:
            print("Normaalkaal")
        elif 25 < indeks < 30:
            print("Ülekaal")
        elif 30 < indeks < 35:
            print("Rasvumine")
        elif 35 < indeks < 40:
            print("Tugev rasvumine")
        elif indeks > 40:
            print("Tervisele ohtlik rasvumine")
        else:
            print("Viga")
    else: 
        print("Kahju! See on väga kasulik info!")
        print()
except:
    print("ValueError")
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")