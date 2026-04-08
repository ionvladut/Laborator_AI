## 1. Liste 

# orase = ["Bucuresti", "Cluj", "Timisoara", "Iasi", "Constanta"] #Lista de orase considerate frumoase din tarisoara noastra 
# print(orase)
# print(orase[0])
# print(orase[1])
# print(orase[-1])
# print(len(orase)) 
# print(orase.index("Timisoara"))
# print(orase[::-1])
# print(orase[0:5:2])
# print(orase.count("Cluj"))
# print("Am auzit ca se traieste bine in " + orase[orase.index("Bucuresti")] + ", dar din punctul meu de vedere este un oras groaznic!")
# print(orase*20)
# orase = orase + ["Brasov", "Sibiu", "Oradea"] # Am adaugat adevaratele orase frumoase din minunatul plai Romanesc 
# print(orase)
# print(orase[orase.index("Brasov"):]) # Afisez doar orasele cu adevarat frumoase, nu si cele considerate frumoase de cei fara gusturi :P
# orase.append("Talmaciu")# Am adaugat si un oras care sa fie mai putin frumos decat celelalte (se exclude Bucuresti)
# print(orase)
# orase.extend(["Medias", "Alba Iulia"]) # Ma abtin de la comentarii, cred ca e destul de evident ce am facut aici :)
# print(orase)
# orase.remove("Bucuresti") # Am sters orasul care nu merita sa fie in lista, adica Bucuresti muahhahahahaha!!
# print(orase)
# print(' '.join(orase)) 
# print('Vladut '.join(orase)) # Am facut o gluma proasta, imi cer scuze :c

# orase.sort() # Am sortat lista de orase in ordine alfabetica, pentru ca de ce nu?!
# print(orase)

# orase.sort(reverse=True) # Am sortat lista de orase in ordine alfabetica inversa, pentru ca de ce nu si asta?!
# print(orase)

# orase_nou = orase.copy() 
# orase_nou = orase[:] 
# print(orase_nou)

# orase.pop() # Am sters ultimul element Adin lista, adica orasul Alba Iulia, care nu merita sa fie in lista de orase frumoase :P
# print(orase)

# orase.pop(3) 
# print(orase) 

# orase.clear() # Am sters toate orasele din lista pentru ca de fapt niciunul nu este FRUMOS!!! Hahaha hiihih huhuhuhu!
# print(orase)

# orase = orase_nou.copy() # Am refacut lista de orase pentru ca nu puteam sa traiesc fara ea
# print(orase)
# del orase_nou # Am sters lista noua pentru ca nu mai aveam nevoie de ea, dar am pastrat lista originala pentru ca e prea frumoasa sa o sterg  

# orase.reverse() # Am inversat ordinea elementelor din lista
# print(orase)

# nr_pref = [2, 3, 5, 7, 11]
# print(min(nr_pref))
# print(max(nr_pref))
# print(sum(nr_pref))

# first, *x, last = nr_pref
# print(first)
# print(x)
# print(last)


# Voi lua orase dintr-o lista TXT ;)
# with open("orase.txt", "r") as f:
#     orase = f.read().split(" ") # Am citit orasele din fisierul TXT si le-am pus intr-o lista, pentru ca de ce nu?!
#     print(orase)

# GATA CU DISTRACTIA! 


# 2. Dictionare 

# dictionarul_meu = {"nume": "Vladut", "prenume": "Vladescu", "varsta": 21, "oras": "Sibiu"} 
# print(dictionarul_meu)
# print(dictionarul_meu["nume"])
# print(dictionarul_meu.get("prenume"))
# print(dictionarul_meu.keys())
# print(dictionarul_meu.values())
# print(dictionarul_meu.items())

# print(len(dictionarul_meu))
# dictionarul_meu["Culoare Preferata"] = "gri nor suparat pe viata"
# print(dictionarul_meu)
# dictionarul_meu["varsta"] = 22
# print(dictionarul_meu)
# del dictionarul_meu["oras"] 
# print(dictionarul_meu.get("oras", "Nu am gasit orasul, se pare ca nu mai exista in dictionar!"))
# dictionarul_meu.pop("Culoare Preferata")
# print(dictionarul_meu)


## 3. Tuple (prima data am inteles truple cand am auzit - funny name)

# fructe_pref = ("gutui", "capsuni", "pere", "struguri")
# print(fructe_pref)
# print(fructe_pref[0])
# print(f"Din {fructe_pref[-1]} se face vinul!! Bun ii vinul ghiurghiuliu!")
# print(len(fructe_pref))
# print(fructe_pref.index("pere"))
# fr1, fr2, fr3, fr4 = fructe_pref
# print(fr1)
# print(fr2)
# print(fr3)
# print(fr4)  # Interesante si tuplele astea 
# print(fructe_pref.count("gutui"))
# print(fructe_pref[:])
# #fructe_pref[1] = "zmeura" # Am incercat sa schimb un element din tupla, da' nu se poaaateee ;c
# print(fructe_pref.index("gutui"))
# print(fructe_pref.count("capsuni"))


## 4. Seturi  

# fructe_pref = {"gutui", "capsuni", "pere", "struguri"}
# print(fructe_pref)

# fructe_yuck = {"smochine", "kiwi", "pepene galben"}
# print(fructe_yuck)

# alte_fructe = {"mar", "banana", "portocala", "gutui"}
# print(alte_fructe)

# fructe_din_vtm = fructe_pref.union(fructe_yuck)
# print(fructe_din_vtm)
# print(fructe_pref.intersection(fructe_yuck)) # Multimea vida (set gol) - pentru ca fructele pref nu pot sa fie si yuck, nu? :P
# print(fructe_pref.difference(fructe_din_vtm)) # Multimea vida (set gol) - pentru ca toate fructele pref sunt si in fructe_din_vtm, deci nu exista niciun fruct care sa fie in pref dar sa nu fie in vtm, nu?
# print(fructe_pref.difference({"gutui", "capsuni"})) 
# print(fructe_din_vtm.symmetric_difference(alte_fructe)) 
# print(fructe_pref.issubset(fructe_din_vtm)) # DA, pentru ca toate fructele pref sunt si in fructe_din_vtm 
# print(alte_fructe.issuperset(fructe_pref)) 
# print(fructe_din_vtm.issuperset(fructe_pref)) 
# print(fructe_pref.isdisjoint(alte_fructe)) 


# # None - cel mai complex tip de data, pentru ca reprezinta lipsa unei valori sau a unui obiect, adica NIMIC, NULL! Cum poate sa existe sau sa nu existe NIMIC?! ;c
# type(None)
# a = None 
# print(a)

# # Gata lab sper ca am invatat ceva nou - desigur ca da! :) 