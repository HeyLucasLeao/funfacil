def transpose(matriz: List[List[int]]) -> List[List[int]]:
        vet = []
        nova_matriz = []
        c = len(matriz[0])
        l = len(matriz)
        for row in range(c):
            for col in range(l):
                vet.append(matriz[col][row])
            if len(vet) == l:
                nova_matriz.append(list(vet))
                vet.clear()
        return nova_matriz
                
