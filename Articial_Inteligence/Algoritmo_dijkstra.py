class nodo:
    def __init__(self,IDnodo) -> None:
        self.ID = IDnodo
        self.before = None
        self.distancia = float('inf')
        self.vecinos = []
        self.visitado = False
    
    def agregarVecinos(self, vecinos, peso):
        if vecinos not in self.vecinos:
            self.vecinos.append([vecinos,peso])


class grafo:
    def __init__(self) -> None:
        self.Nodos = {}
    
    def agregarNodo(self, IDnodo):
        if IDnodo not in self.Nodos:
            self.Nodos[IDnodo] = nodo(IDnodo)
    
    def agregarArista(self,nodoA,nodoB,distancia):
        if nodoA in self.Nodos and nodoB in self.Nodos:
            self.Nodos[nodoA].agregarVecinos(nodoB,distancia)
            self.Nodos[nodoB].agregarVecinos(nodoA,distancia)
    
    def dijkstra(self, nodoInicial):
        if nodoInicial in self.Nodos:
            self.Nodos[nodoInicial].distancia = 0

            nodosNoVisitados = []
            actual = nodoInicial

            for nodo in self.Nodos:
                if nodo != nodoInicial:
                    self.Nodos[nodo].distancia = float('inf')
                self.Nodos[nodo].before = None
                nodosNoVisitados.append(nodo)
            
            while len(nodosNoVisitados) > 0:
                for vecino in self.Nodos[actual].vecinos:
                    if self.Nodos[vecino[0]].visitado == False:
                        if self.Nodos[actual].distancia + vecino[1] < self.Nodos[vecino[0]].distancia:
                            self.Nodos[vecino[0]].distancia = self.Nodos[actual].distancia + vecino[1]
                            self.Nodos[vecino[0]].before = actual
            
                self.Nodos[actual].visitado = True
                nodosNoVisitados.remove(actual)
                actual = self.min(nodosNoVisitados)

        else:
            print("Nodo no se encuentra en el grafo")
            return False
        
    def printNodo(self):
        for key, items in self.Nodos.iteams():
            vecinos = [vecino[0] for vecino in items]
            pesovecinos = [peso[1] for peso in items]
            print(f'Al nodo {key}: tiene vecinos: {" ".join(vecinos)} y un peso de {" ".join(pesovecinos)} respectivamente')

    def ruta(self, nodoDestino):
        ruta = []
        actual = nodoDestino
        while actual != None:
            ruta.insert(0,actual)
            actual = self.Nodos[actual].before
        return (ruta, self.Nodos[nodoDestino].distancia)
    
    def min(self, NodosNoVisitado):
        if len(NodosNoVisitado) > 0:
            distanciaNodo = self.Nodos[NodosNoVisitado[0]].distancia
            nuevoNodo = NodosNoVisitado[0]
            for nodoNV in NodosNoVisitado:
                if distanciaNodo > self.Nodos[nodoNV].distancia:
                    distanciaNodo = self.Nodos[nodoNV].distancia
                    nuevoNodo = nodoNV
            return nuevoNodo
        return None
        

if __name__ == "__main__":
    miGrafo = grafo()
    miGrafo.agregarNodo(1)
    miGrafo.agregarNodo(2)
    miGrafo.agregarNodo(3)
    miGrafo.agregarNodo(4)
    miGrafo.agregarNodo(5)
    miGrafo.agregarNodo(6)
    miGrafo.agregarArista(1, 6, 14)
    miGrafo.agregarArista(1, 2, 7)
    miGrafo.agregarArista(1, 3, 9)
    miGrafo.agregarArista(2, 3, 10)
    miGrafo.agregarArista(2, 4, 15)
    miGrafo.agregarArista(3, 4, 11)
    miGrafo.agregarArista(3, 6, 2)
    miGrafo.agregarArista(4, 5, 6)
    miGrafo.agregarArista(5, 6, 9)

    nodoinicio = 5
    nodofinal = 1
    miGrafo.dijkstra(nodoinicio)
    rutaOptima = miGrafo.ruta(nodofinal)
    
    print(f'La ruta mas rapida iniciando en el nodo {nodoinicio} al {nodofinal} es: {"-".join([str(ele) for ele in rutaOptima[0]])} con un peso de {rutaOptima[1]}')
   
