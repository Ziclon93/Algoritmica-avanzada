import networkx as nx
import matplotlib.pyplot as plt

def get_metro_graph(_file):
    G = nx.Graph()
    lines = open(_file, 'r').read().splitlines()
    _n=_l=None
    for line in lines:
        [n, d, l, c, _long, _lat] = line.split(',')
        #[_long, _lat] = p.split(',')

        # Convert to string
        _long = float(_long)
        _lat = float(_lat)

        G.add_node(n, longitud=_long, latitud=_lat)

        if not(not _l or l != _l):
            G.add_edge(_n, n, distance=d, line=l, color=c)

        _n,_l=n,l
    return G


def draw_metro_graph(G, figsize=(10,6)):
    colors = [G[u][v]['color'] for u,v in G.edges()]
    # Diferentes layouts para dibujar el grafo
    '''
    'circular_layout',
    'random_layout',
    'shell_layout',
    'spring_layout',
    'spectral_layout',
    'fruchterman_reingold_layout'
    '''
    plt.figure(figsize=figsize)
    pos = {}
    for i in G:
        pos[i] = ([G.node[i]['latitud'], G.node[i]['longitud']])

    nx.draw_networkx_edges(G,pos, edge_color=colors, width=3)
    nx.draw_networkx_nodes(G,pos,
                       node_color='b',
                       node_size=30,
                       alpha=0)
    nx.draw_networkx_labels(G,pos,font_size=8)


def get_path_subgraph(G, path):
    P = nx.Graph()
    for i in range(len(path)-1):
        orig = path[i]
        dest = path[i+1]
        P.add_node(orig, G.node[orig])
        P.add_node(dest, G.node[dest])
        P.add_edge(orig, dest, G[orig][dest])

    return P
