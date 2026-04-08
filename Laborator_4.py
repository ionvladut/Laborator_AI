# ## Introducere in FUNCTII in PY

# def adunare(x, y):
#     return x + y;

# print(adunare(2,3), "\n")

# def myfunc (arg1, *args):
#     print("Primul numar este: ", arg1)
#     for arg in args:
#         if arg%2 is 0:
#             print(arg, " este numar par")
#         else: print(arg, " este numar impar")

# myfunc(1, 2, 3, 4, 5, 6, 7)

# def myfunc2(**dic):
#     for cheie, val in dic.items():
#         print(cheie, "=", val)

# myfunc2(Vlad="Boss", Tudor="Ingrijitor")

# suma_gauss = lambda n : n if n <= 1 else n+suma_gauss(n-1)

# print(suma_gauss(5))

# factorial = lambda n : n if n<=1 else n*factorial(n-1)

# print(factorial(3))

# numere = (2, 3, 4, 5)

# lista = []
# factorial_numere = map(factorial, numere)
# for numar in factorial_numere:
#     lista.append(numar)
# print(lista)

# def utilizatori(secventa):
#     nume = ["Popescu", "Ionescu", "Ciolacu"]
#     if secventa in nume:
#         return True
#     else: return False

# secventa = ["Popescu", "aru", "Pop"]

# lista = []
# secventa_nou = filter(utilizatori, secventa)
# for secv in secventa_nou:
#     lista.append(secv)

# print(lista)

# if "a" in "Vacaru": 
#     print("Da ba")
# else: print("Nu Ba")



## Exercitiul 1

# def RockPaperScissors(gamer1, gamer2):
#     if gamer1.lower() == "piatra":
#         if gamer2.lower() == "hartie":
#             print("Jucator 2 castiga!")
#         elif gamer2.lower() == "foarfeca":
#             print("Jucator 1 castiga!")
#         else: print("REMIZA!")
  
#     if gamer1.lower() == "hartie":
#         if gamer2.lower() == "piatra":
#             print("Jucator 1 castiga!")
#         elif gamer2.lower() == "foarfeca":
#             print("Jucator 2 castiga!")
#         else: print("REMIZA!")

#     if gamer1.lower() == "foarfeca":
#         if gamer2.lower() == "piatra":
#             print("Jucator 2 castiga!")
#         elif gamer2.lower() == "hartie":
#             print("Jucator 1 castiga!")
#         else: print("REMIZA!")
    

# jucator1 = input("Jucatorul 1 alege: ")
# jucator2 = input("Jucatorul 2 alege: ")

# RockPaperScissors(jucator1, jucator2)


## EXERCITIUL 2

# def genereaza_factura(nume, **cumparaturi):
#     print("Nume client: ", nume)
#     print("Produse achitate: ")
#     for produs, pret in cumparaturi.items():
#         print(produs, pret, "RON")

# lista = {'Piept de pui':10, 'Macaroane':3, 'Cas dospit':23}

# genereaza_factura("MARCEL GIGEL", **lista )


## EXERCITIUL 3

# def normalize_data(dates):
#     new_dates = []
#     minim = min(dates)
#     maxim = max(dates)
#     for data in dates:
#         data_new = (data-minim)/(maxim-minim)
#         new_dates.append(data_new)
#     return new_dates

# data = [5, 2, 8, 12, 3]
# normalized_data = normalize_data(data)
# print(normalized_data)


## Exercitiul 4

# patrat = lambda n: n**2
# numere = [1, 2, 3, 4, 5]
# numere_patrat = map(patrat, numere)
# lista=[]
# for numar in numere_patrat:
#     lista.append(numar)
# print(lista)

## Exercitiul 5

# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# a_sortat = a.copy()
# a_sortat.sort(key = lambda x:x[1])
# print(a)
# print(a_sortat)

## Exercitiul 6

# orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_list = list(filter(lambda x:x%2==0, orig_list))
# odd_list = list(filter(lambda x:x%2!=0, orig_list))

# print(even_list)
# print(odd_list)


## Exercitiul 7

# def reducere(element):
#      element = element - (10/100 * element)
#      return element

# def filtruNone(element):
#         if element is not None:
#           return True
#         else: return False


# preturi = [10, 24, None, 57, 120, None]
# preturiNou = list(filter(filtruNone, preturi))
# print(preturiNou)
# preturiReduse = list(map(reducere,preturiNou))
# print(preturiReduse)

## Exercitiul 8

# data = "2024-04-06 16:53:37.223523"
# an = lambda x: x.split("-")[0]
# luna = lambda x: x.split("-")[1]
# zi = lambda x: x.split("-")[2].split(" ")[0]
# ora = lambda x: x.split("-")[2].split(" ")[1]
# print(an(data))
# print(luna(data))
# print(zi(data))
# print(ora(data))

## Exercitiul 9


# def listsSum(list1, list2):
#     listComb = zip(list1, list2)
#     listFinal = []
#     for element in listComb:
#         listFinal.append(element[0]+element[1])
#     return listFinal


# list1 = [1, 2, 3, 4, 5] 
# list2 = [10, 20, 30, 40, 50] 

# print(listsSum(list1, list2))


## Exercitiul 10

# list1 = [i for i in range(100) if i%2==0]
# list2 = [i**3 for i in range(10)]
# list3 = [element for element in list1 if element in list2]

# print(list1)
# print(list2)
# print(list3)

## Exercitiul 11

# myset = (i*2 for i in range(1,11) if i%2==0)
# cuvant = "Sarbatori binecuvantate alaturi de cei dragi"
# litereCuv = (litera for litera in cuvant)
# cuvCheie = (cuv for cuv in cuvant.split(" ") if cuv=="Sarbatori")
# print(list(myset))
# print(list(litereCuv))
# print(list(cuvCheie))


## Exercitiul 12

# dict1 = {i: i**2 for i in range(10)}
# propozitie = "Paste fericit alaturi de cei dragi. Sarbatori pascale in tihna, cu liniste si pace"
# dict2 = {litera: propozitie.count(litera) for litera in propozitie}
# dict3 = {i:len([j for j in range(1,i) if i%j==0])+1 for i in range(1,11)}
# print(dict1)
# print(dict2)
# print(dict3)