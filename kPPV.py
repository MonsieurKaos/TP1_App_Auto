""" programme à compléter du kPPV"""
import csv
import math

nbExParClasse = 50
nbApprent = 25
nbCaract = 4
nbClasse = 3

def lectureFichierCSV():
    with open("iris.data", 'r')as fic:
        lines = csv.reader(fic)
        dataset = list(lines)
    print(dataset[0], len(dataset))
    for i in range(len(dataset)):
        for j in range(nbCaract):
            dataset[i][j] = float(dataset[i][j])
            #print (dataset[i][j])
    print(dataset[0])
    return(dataset)

def calculdistances(data, dataset):
    """ retourne les distances entre data et la partie apprentissage de dataset"""
    distances = []
    for i in range(nbClasse*nbExParClasse):
        if i % nbExParClasse < nbApprent:
            dist = 0
            for k in range(nbCaract):
                dist += (data[k]-dataset[i][k])**2
            distances.append(dist**0.5)
    return distances

def calculClasse(distances):
    """ retourne le numéro de la classe déterminé à partir des distances """
    t = min(distances)
    for i in range (len(distances)):
        if distances[i] == t:
            m = i
    if m < nbApprent-1 :
        classe = 0
    elif m<(nbApprent*2)-1 and m>nbApprent-1 :
        classe = 1
    else :
        classe = 2
	#-------- A faire... --------

    return (classe)

if __name__ == "__main__":
    print("Début programme kPPV")
    dataset = lectureFichierCSV()
    print (dataset[0][0])
    distance = calculdistances([5.0,3.6,1.4,0.2],dataset)
    print (distance)
    classe = calculClasse(distance)
    print (classe)

    # Calcule et affiche la matrice de confusion et le taux de reco


	#-------- A faire... --------

#--------------------------------- Fin kPPV -----------------------------------