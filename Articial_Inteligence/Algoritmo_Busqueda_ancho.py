
import networkx as nx 
import matplotlib.pyplot as plt

def busqueda_ancho(V,E,raiz):
    V = sorted(V)

    if raiz in V:
        S = [raiz]
        v = [raiz]
    else:
        print("El nodo raiz no existe, por favor ingresa un nodo raiz valido")
        return 0
    e = []

    nivel = [raiz]
    while True:
        son = []
        aristas = False
        for x in S:
            for y in set(V)-set(v):
                if (x,y) in E:
                    e.append((x,y))
                    v.append(y)
                    aristas = True
                    son.append(y)
        if not aristas:
            return v,e, nivel
        S = son

        nivel.append(son)
        


if __name__== "__main__":

    G = nx.Graph([("a","b"),("a","c"),("a","g"),
                ("b","d"),("b","g"),
                ("d","f"),
                ("c","d"),("c","e"),
                ("e","f"),("e","g"),
                ("f","h")])

    pos = {"a": (0, 0.3), "g": (0, 0), "c": (.5, 0.15), "e": (1, 0), "d": (2.5, 0.15), "f": (2, 0),"b": (3, 0.3),"h": (3, 0)}
    
    options = {
    "font_size": 36,
    "node_size": 2000,
    "node_color": "#A0CBE2",
    "width": 3,
    }

    fig1 = plt.figure("Grafo Original")
    nx.draw_networkx(G, pos, **options)
    plt.axis("off")
    
    

    raiz="b"
    v,e,nivel = busqueda_ancho(G.nodes,G.edges,raiz)
    print(f'Vertices: {v}')
    print(f'Aristas: {e}')
    print(f'Por nivel del arbol: {nivel}')

    fig2 = plt.figure("Arbol del grafo Ordenado")
    G2 = nx.DiGraph(e)
    nx.draw(G2,with_labels=True,**options)

    

    plt.show()


