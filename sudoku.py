lista=[]
for i in range(9):
    lista1=[]
    for j in range(9):
        lista1.append(chr(120))
    lista.append(lista1)

numeracion=[[0,2,5], [0, 4, 4], [0, 6, 7], [0, 8, 3], [1, 4, 8], [2, 1, 3], [2, 3, 6], [3, 3, 3], [3, 5, 4], [3, 6, 1], [4, 0,4], [4, 3, 9], [4,4,2], [5,1,7],[5,6,8], [6,0,6],[6,1,1],[6,6,4],[6,7,7],[7,0,2],[7,2,3],[7,7,8],[8,7,6]]
for i in range(len(numeracion)):
    lista[numeracion[i][0]][numeracion[i][1]]=numeracion[i][2]
for i in range(9):
    cad="\r"
    for j in range(9):
        cad+=str(lista[i][j])+  " "
    print(cad)

