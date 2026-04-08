# EXERCITIUL 1


# picture = [
# [0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,1,0],
# [1,1,1,1,1,1,1],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0]]


# for row in picture:
#    visual = " "
#    for num in row:
#       if num == 1: visual = visual + "*"
#       else: visual = visual + " "
#    print(visual)


# EXERCITIUL 2

# nota = int(input("Introduceti nota: "))
# if nota>10 or nota<1:
#     print("Nota invalida")
# elif nota>=9:
#     print("Excelent")
# elif nota>=7:
#     print("Bine")
# elif nota>=5:
#     print("Suficient")
# else:    print("Insuficient")



# EXERCITIUL 3


# import random

# nr = random.randint(1,50)
# ghicire = 0
# contor = 0
# while ghicire != nr:
#    ghicire = int(input("Ghiceste numarul:"))
#    contor = contor + 1
#    if ghicire < nr: 
#       print("Numarul este mai mare")
#    elif ghicire > nr: 
#       print("Numarul este mai mic")
#    else: 
#       print("Felicitari! Ai ghicit din " + str(contor) + " incercari!")


# EXERCITIUL 4

# orase = ["Bucuresti", "Cluj", "Timisoara" ,"Iasi", "Constanta"]
# print(list(enumerate(orase)))


# EXERCITIUL 5

# import random

# contor = 0
# numere_castigatoare = random.sample(range(1,49), 6)
# numere_alese = [int(x) for x in input("Introduceti cele 6 numere alese separate prin spatiu: ").split()]
# for x in numere_alese:
#    if x in numere_castigatoare:
#         contor = contor + 1
# if contor == 6: print("Felicitari! Ai castigat premiul cel mare!")
# else: print("Ai ghicit " + str(contor) + " numere. Mai incearca!")
# print("Numerele castigatoare sunt: " + str(numere_castigatoare))
  

# EXERCITIUL 6
# import random
# evenimente_pozitive = ["Te-ai intalnit cu fierarul POPESCU si ai primit o sabie magica!", "Ai gasit o comoara ascunsa in padure! In ea se afla un pumnal!", "Ai invatat o vraja puternica de la un mag batran!", "Ai salvat un sat de la un atac de orci si ai fost recompensat cu o armura stralucitoare!",  "Te-ai alaturat unei bande de aventurieri si ai primit un inel magic care iti creste puterea!", "Ai gasit-o pe ELODIA si vine elicopterul OTV dupa tine!"]
# evenimente_negative = ["Ai fost blestemat de o vrajitoare rea si ai pierdut o arma valoroasa!", "Ai fost tradat de un aliat si ti-a furat armura! Era un ROMAN!", "Ai fost ranit grav intr-o lupta si ai pierdut armura!", "Ai fost atacat de un grup de banditi si ai pierdut toate obiectele din inventar!", "Ai fost prins intr-o capcana si ai pierdut o arma valoroasa!", "Ai fost atacat de un dragon si ai pierdut toate obiectele din inventar!", "Ai fost prins intr-o capcana mortala si ai pierit!"]
# inventar = []
# stanga = 0
# dreapta = 0
# while stanga < 10 and dreapta < 10:
    
#     directie = input("Alege o directie (s pentru stanga, d pentru dreapta): ")
#     if directie == "s":
#         stanga = stanga + 1
#     elif directie == "d":
#         dreapta = dreapta + 1
#     else: 
#         print("Directie invalida! Te rog sa alegi 's' sau 'd'.")
#         continue
#     if stanga == 2 and dreapta == 2:
#         eveniment = random.choice(evenimente_pozitive)
#         print(eveniment)
#         if eveniment == evenimente_pozitive[0] and "sabie magica" not in inventar: inventar.append("sabie magica")
#         elif eveniment == evenimente_pozitive[1] and "comoara ascunsa" not in inventar: inventar.append("comoara ascunsa")
#         elif eveniment == evenimente_pozitive[2] and "vraja puternica" not in inventar: inventar.append("vraja puternica")
#         elif eveniment == evenimente_pozitive[3] and "armura stralucitoare" not in inventar: inventar.append("armura stralucitoare")
#         elif eveniment == evenimente_pozitive[4] and "inel magic" not in inventar: inventar.append("inel magic")
#         elif eveniment == evenimente_pozitive[5]: 
#             inventar.append("elicopterul OTV") 
#             print("Vrei sa fugi din padure cu elicopterul OTV? (da/nu) ") 
#             alegere = input() 
#             if alegere == "da": 
#                 print("Felicitari! Ai scapat din padure cu elicopterul OTV! Ai castigat jocul!") 
#                 break 
#             else: print("Ai ales sa ramai in padure. Continuam aventura!")
#     elif stanga == 2 and dreapta == 0:
#         eveniment = random.choice(evenimente_negative)
#         print(eveniment)
#         if eveniment == evenimente_negative[0] and "sabie magica" in inventar: inventar.remove("sabie magica")
#         elif eveniment == evenimente_negative[1] and "armura stralucitoare" in inventar: inventar.remove("armura stralucitoare")
#         elif eveniment == evenimente_negative[2] and "armura stralucitoare" in inventar: inventar.remove("armura stralucitoare")
#         elif eveniment == evenimente_negative[3]: inventar.clear()
#         elif eveniment == evenimente_negative[4] and "sabie magica" in inventar: inventar.remove("sabie magica")
#         elif eveniment == evenimente_negative[5]: inventar.clear()
#         elif eveniment == evenimente_negative[6]: 
#             print("Ai pierit! Joc pierdut!") 
#             break

#     elif stanga == 0 and dreapta == 2:
#         eveniment = random.choice(evenimente_negative)
#         print(eveniment)
#         if eveniment == evenimente_negative[0] and "sabie magica" in inventar: inventar.remove("sabie magica")
#         elif eveniment == evenimente_negative[1] and "armura stralucitoare" in inventar: inventar.remove("armura stralucitoare")
#         elif eveniment == evenimente_negative[2] and "armura stralucitoare" in inventar: inventar.remove("armura stralucitoare")
#         elif eveniment == evenimente_negative[3]: inventar.clear()
#         elif eveniment == evenimente_negative[4] and "sabie magica" in inventar: inventar.remove("sabie magica")
#         elif eveniment == evenimente_negative[5]: inventar.clear()
#         elif eveniment == evenimente_negative[6]: 
#             print("Ai pierit! Joc pierdut!") 
#             break
#     elif stanga == 4 and dreapta == 4:
#         eveniment = random.choice(evenimente_pozitive)
#         print(eveniment)
#         if eveniment == evenimente_pozitive[0] and "sabie magica" not in inventar: inventar.append("sabie magica")
#         elif eveniment == evenimente_pozitive[1] and "comoara ascunsa" not in inventar: inventar.append("comoara ascunsa")
#         elif eveniment == evenimente_pozitive[2] and "vraja puternica" not in inventar: inventar.append("vraja puternica")
#         elif eveniment == evenimente_pozitive[3] and "armura stralucitoare" not in inventar: inventar.append("armura stralucitoare")
#         elif eveniment == evenimente_pozitive[4] and "inel magic" not in inventar: inventar.append("inel magic")
#         elif eveniment == evenimente_pozitive[5]: 
#             inventar.append("elicopterul OTV") 
#             print("Vrei sa fugi din padure cu elicopterul OTV? (da/nu) ") 
#             alegere = input() 
#             if alegere == "da": 
#                 print("Felicitari! Ai scapat din padure cu elicopterul OTV! Ai castigat jocul!") 
#                 break 
#             else: print("Ai ales sa ramai in padure. Continuam aventura!")
#     elif stanga == 4 and dreapta == 0:
#         eveniment = random.choice(evenimente_negative)
#         print(eveniment)
#         if eveniment == evenimente_negative[0] and "sabie magica" in inventar: inventar.remove("sabie magica")
#         elif eveniment == evenimente_negative[1] and "armura stralucitoare" in inventar: inventar.remove("armura stralucitoare")
#         elif eveniment == evenimente_negative[2] and "armura stralucitoare" in inventar: inventar.remove("armura stralucitoare")
#         elif eveniment == evenimente_negative[3]: inventar.clear()
#         elif eveniment == evenimente_negative[4] and "sabie magica" in inventar: inventar.remove("sabie magica")
#         elif eveniment == evenimente_negative[5]: inventar.clear()
#         elif eveniment == evenimente_negative[6]: 
#             print("Ai pierit! Joc pierdut!") 
#             break
#     elif stanga == 0 and dreapta == 4:
#         eveniment = random.choice(evenimente_negative)
#         print(eveniment)
#         if eveniment == evenimente_negative[0] and "sabie magica" in inventar: inventar.remove("sabie magica")
#         elif eveniment == evenimente_negative[1] and "armura stralucitoare" in inventar: inventar.remove("armura stralucitoare")
#         elif eveniment == evenimente_negative[2] and "armura stralucitoare" in inventar: inventar.remove("armura stralucitoare")
#         elif eveniment == evenimente_negative[3]: inventar.clear()
#         elif eveniment == evenimente_negative[4] and "sabie magica" in inventar: inventar.remove("sabie magica")
#         elif eveniment == evenimente_negative[5]: inventar.clear()
#         elif eveniment == evenimente_negative[6]: 
#             print("Ai pierit! Joc pierdut!") 
#             break
#     elif stanga == 6 and dreapta == 6:
#         eveniment = random.choice(evenimente_pozitive)
#         print(eveniment)
#         if eveniment == evenimente_pozitive[0] and "sabie magica" not in inventar: inventar.append("sabie magica")
#         elif eveniment == evenimente_pozitive[1] and "comoara ascunsa" not in inventar: inventar.append("comoara ascunsa")
#         elif eveniment == evenimente_pozitive[2] and "vraja puternica" not in inventar: inventar.append("vraja puternica")
#         elif eveniment == evenimente_pozitive[3] and "armura stralucitoare" not in inventar: inventar.append("armura stralucitoare")
#         elif eveniment == evenimente_pozitive[4] and "inel magic" not in inventar: inventar.append("inel magic")
#         elif eveniment == evenimente_pozitive[5]: 
#             inventar.append("elicopterul OTV") 
#             print("Vrei sa fugi din padure cu elicopterul OTV? (da/nu) ") 
#             alegere = input() 
#             if alegere == "da": 
#                 print("Felicitari! Ai scapat din padure cu elicopterul OTV! Ai castigat jocul!") 
#                 break 
#             else: print("Ai ales sa ramai in padure. Continuam aventura!")
#     else: print("Nu s-a intamplat nimic interesant. Continuam aventura!")
#     print("Inventar final: " + str(inventar))
# print("Gata joaca!")


# Exercitiul 7 

# Comentariu = input("Introduceti un comentariu: ")
# cuvinte_frumoase = ["frumos", "minunat", "superb", "extraordinar", "splendid", "magnific", "incantator", "fermecator", "uluitor", "mirific"]
# cuvinte_urate = ["urat", "groaznic", "hidos", "dezastruos", "oribil", "mizerabil", "dezgustator", "neplăcut", "repugnant", "infam"]
# if any(cuvant in Comentariu.lower() for cuvant in cuvinte_frumoase):
#     print("Comentariu pozitiv")
# elif any(cuvant in Comentariu.lower() for cuvant in cuvinte_urate):
#     print("Comentariu negativ")
# else: print("Comentariu neutru")


# Exercitiul 8
# import time as timer
# timp = 0
# timp_final = 0
# suspect = 0
# nr_tranzactii = 0
# while suspect < 3:
#     print("Va rog sa introduceti urmatoarele informatii pentru tranzactia bancara: ")
#     nume = input("Nume: ")
#     prenume = input("Prenume: ")
#     suma = float(input("Suma: "))
#     tara = input("Tara: ")
#     nr_tranzactii = nr_tranzactii + 1
#     timp = timer.time()

#     if timp-timp_final < 180 and nr_tranzactii >= 3:
#         suspect = suspect + 1
#         print("Tranzactie suspecta! Prea multe tranzactii intr-un timp scurt!")
#     elif suma > 10000:
#         suspect = suspect + 1
#         print("Tranzactie suspecta! Suma depaseste 10.000!")
#     elif tara.lower() in ["coreea de nord", "iran", "siria"]:
#         suspect = suspect + 1
#         print("Tranzactie suspecta! Tara de origine este una cu risc crescut!")
#     else: print("Tranzactie aprobata! Multumim pentru colaborare!")
#     timp_final = timer.time()
#     if suspect == 3:
#         print("Tranzactie blocata! Prea multe tranzactii suspecte!")
#         break

    
    
