import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np

def algoritmo_Prim(G,s):
    V = list(G.nodes)
    v = np.zeros(len(V))
    v[V.index(s)] = 1

    E = []
    agregar_vertice = 0
    e = 0

    for i in V[:len(V)-1]:
        v_min = float('inf')
        for j in V:

            if v[V.index(j)] == 1:
                for k in V:
                    w_arista = peso_arista(G,j,k)

                    if(v[V.index(k)]==0 and w_arista<v_min):
                        agregar_vertice = V.index(k)
                        e = (j,k,{'weight': w_arista})
                        v_min = w_arista
        
        v[agregar_vertice] = 1
        E.append(e)

    return E

def peso_arista(G,j,k):
    vertices = list(G.edges)
    if (j,k) in G.edges:
        try:
            pos = vertices.index((j,k))  
        except ValueError:
            pos = vertices.index((k,j))        
        return list(G.edges.data())[pos][2]['weight']
    else:
        return float('inf')
        
if __name__== "__main__":

    G = nx.Graph([(1,2,{'weight': 4}),(1,3,{'weight': 2}),(1,5,{'weight': 3}),
                (2,4,{'weight': 5}),
                (3,4,{'weight': 1}),(3,5,{'weight': 6}),(3,6,{'weight': 4}),
                (4,6,{'weight': 6}),
                (5,6,{'weight': 2})])
              
    pos = nx.kamada_kawai_layout(G)

    options = {
    "font_size": int(36*.4),
    "node_size": int(2000*.3),
    "node_color": "#A0CBE2",
    "width": 3,
    }

    edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges.data()])

    options_labels = {
        "edge_labels":edge_labels,
        "label_pos":.45,
        "bbox":{'boxstyle':'round', 'ec':(1.0, 1.0, 1.0), 'fc':(1.0, 1.0, 1.0),'pad':0.1},
    }

    fig1 = plt.figure("Grafo Original")
    nx.draw_networkx(G, pos, **options)
    nx.draw_networkx_edge_labels(G,pos,**options_labels)
    plt.axis("off")
    
    

    s=1
    E = algoritmo_Prim(G,s)
    print(f'Vertices: {E}')
    


    fig2 = plt.figure("Arbol de expansion minima")

    G2 = nx.DiGraph(E)
    
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in G2.edges.data()])
    options_labels = {
        "edge_labels":edge_labels,
        "label_pos":.45,
        "bbox":{'boxstyle':'round', 'ec':(1.0, 1.0, 1.0), 'fc':(1.0, 1.0, 1.0),'pad':0.1},
    }

    nx.draw(G2,pos,with_labels=True,**options)
    nx.draw_networkx_edge_labels(G2,pos,**options_labels)

    
    ax = plt.gca()
    ax.margins(0.20)
    plt.show()
