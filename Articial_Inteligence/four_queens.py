def conflicto(fila,k):
    for i in range(k):
        if fila[i] == fila[k]:
            return True
        diff = k - i
        if fila[i] == fila[k]-diff or fila[i] == fila[k]+diff:
            return True
    return False

def four_queens(fila):
    k = 0 #Columna No.1
    fila[k] = 0 

    while k>=0:
        fila[k] += 1 

        #Se busca moviento legal en la columna k
        while fila[k]<=4 and conflicto(fila,k):
            fila[k] += 1
        if fila[k] <= 4:
            if k == 3:
                return True
            else:
                k += 1
                fila[k] = 0
        else:
            k = k-1
    return False    

if __name__ == "__main__":
    fila = [0,0,0,0]
    
    if four_queens(fila):
        print(f"Si tiene solucion y es: {fila}")
    else:
        print("No tiene solucion")
