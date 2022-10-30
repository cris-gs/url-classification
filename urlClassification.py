import json

#Total de paginas de categoria juegos
totalGames=1
#Total de paginas de categoria computadoras
totalComp=1
#Total de paginas de invalidas
totalInvalid=0
#Total constante de links evaluados
totalLinks=7000
#Provabilidades previas
priorProbGames=0
priorProbComp=0


def analyzeCategory(priorProbGames, priorProbComp,probIncGames, probIncComp):
    propCatGames=priorProbGames*probIncGames
    propCatComp=priorProbComp*probIncComp

    if(propCatGames>propCatComp):
        return "Games"
    elif(propCatGames<propCatComp):
        return "Computers"
    else:
        return "Invalid"


def defineCategory(keyword):
    global totalGames, totalComp, totalInvalid

    #Palabras claves sobre juegos en la página que está siendo analizada
    tempComp=keyword['computers']['total']
    #Palabras claves sobre computadoras en la página que está siendo analizada
    tempGames=keyword['games']['total']

    #actualiza las probabilidades previas de juegos y computadoras
    priorProbGames=totalGames/totalLinks
    priorProbComp=totalComp/totalLinks

    globals()['priorProbGames'] = priorProbGames
    globals()['priorProbComp'] = priorProbComp

    if(tempComp<7 and tempGames<7):
        totalInvalid += 1
        globals()['totalInvalid'] = totalInvalid
        return "Invalid"

    #actuliza el total de páginas de categorizadas para juegos y computadoras
    elif(tempGames != 0 and tempComp != 0):
        category=analyzeCategory(priorProbGames, priorProbComp, tempGames/totalGames, tempComp/totalComp)
        if(category=="Games"):
            totalGames += 1
            globals()['totalGames'] = totalGames
            return "Games"
        elif(category=="Computers"):
            totalComp += 1
            globals()['totalComp'] = totalComp
            return "Computers"
        else:
            totalInvalid += 1
            globals()['totalInvalid'] = totalInvalid
            return "Invalid"

    elif(tempGames != 0 and tempComp == 0):
        totalGames += 1
        globals()['totalGames'] = totalGames
        return "Games"

    elif(tempComp != 0 and tempGames == 0):
        totalComp += 1
        globals()['totalComp'] = totalComp
        return "Computers"

    else:
        totalInvalid += 1
        globals()['totalInvalid'] = totalInvalid
        return "Invalid"





with open("datos.json") as file:
    data = json.load(file)
    id = 1
    listCategory = []

    for key in zip(data['keywords'], data['link']):
        category = defineCategory(key[0])
        link = key[1]
        if category == "Games": 
            keywords = key[0]['games']
        elif category == "Computers":
            keywords = key[0]['computers']
        elif category == "Invalid":
            keywords = {} 
        listCategory.append({"id": id, "category": category, "link": link, "keywords": keywords})
        id+=1
    
    listTotals = [] 
    listTotals.append({'name': 'totalGames', 'value': totalGames-1})
    listTotals.append({'name': 'totalComputer', 'value': totalComp-1})
    listTotals.append({'name': 'totalInvalid', 'value': totalInvalid})

    data2 = ({"totals":listTotals, "categories": listCategory})
    with open('dataCategories.json', 'w') as f:
        json.dump(data2, f, indent= 4)



