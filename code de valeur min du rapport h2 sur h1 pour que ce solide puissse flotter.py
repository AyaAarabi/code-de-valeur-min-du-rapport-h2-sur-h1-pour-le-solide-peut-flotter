mv=float(input("entrez la valeur du la masse volumiue du mercure :"))
mv1=float(input("entrez la valeur du la masse volumique du platine :"))
mv2=float(input("entrez la valeur de la masse volumique du zinc :"))
try:
    min=((mv1-mv)/(mv-mv2))
    print("la valeur mnimal de h2/h1 est :",min,"m")
except:
    print("la valeur de la masse volumique de mercure et/ou de zinc et/ou du platine est incorrect:")