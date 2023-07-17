import networkx as nx 
import matplotlib.pyplot as plt

def busqueda_profundidad(G,raiz):
    V = G.nodes
    E = G.edges

    V = sorted(V)

    if raiz in V:
        v = [raiz]
        w = raiz   
    else:
        print("El nodo raiz no existe, por favor ingresa un nodo raiz valido")
        return 0
    e = []

    
    while True:
        elements = set(G.neighbors(w))-set(v)
        while(elements != set()):

            vk = min(elements)
            e.append((w,vk))
            v.append(vk)
            w = vk

            elements = set(G.neighbors(w))-set(v)
        if (w == raiz):
            return v,e

        father = [i[1:2] for i in e].index((w,)) 

        w = e[father][0] 
       
        
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
    
    

    raiz="c"
    v,e = busqueda_profundidad(G,raiz)
    print(f'Vertices: {v}')
    print(f'Aristas: {e}')
  

    fig2 = plt.figure("Arbol del grafo Ordenado")
    G2 = nx.DiGraph(e)
    nx.draw(G2,with_labels=True,**options)

    

    plt.show()