x = 0
print("\n")
meno = (input("Tvoje meno: "))
print("\n")
while x < 1:
    print('Ahoj '+str(meno)+' vidím, že ťa zaujíma veľkosť Lukiho čuraka')
    print("\n")
    a = input("(ano/nie)\n: ")
    print("\n")
    if a == ("ano") :
        print("###############################")
        print('# Veľkosť Lukiho čuraka = 0cm #')
        print("###############################")
        print("\n")
        a = input ("Ešte raz ? (ano/nie) \n: ")
        print("\n")
        if a == ("ano"):
            x = 0
        elif a == ("nie"):
            x += 1
        else:
            print ("Prečo ? ... prečo ?")
            x += 1
    elif a == ("nie"):
        print("###########################")
        print("# Luki aj tak žiaden nemá #")
        print("###########################")
        print("\n")
        a = input ("Ešte raz ? \n(ano/nie) \n: ")
        print("\n")
        if a == ("ano"):
            x = 0
        elif a == ("nie"):
            x += 1
        else:
            print ("Prečo ? ... prečo ?")
            x += 1
    else:
        print("Si kokot ?\n")
        a = input("(ano/nie) ? \n: ")
        if a == ("ano"):
            x += 1
        elif a == ("nie"):
            x += 1
        else:
            print ("Prečo ? ... prečo ?")
            x += 1
