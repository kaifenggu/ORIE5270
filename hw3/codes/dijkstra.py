def make_dictionary(text):
    text = text.replace('\n', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text_list = text.split(',')
    num_out_edges = int(len(text_list)/2)
    out_edges = {}
    for j in range(num_out_edges):
        out_edges[text_list[2*j]] = int(text_list[2*j+1])
    return out_edges


def txt_to_graph(filename):
    with open(filename) as f:
        data = f.readlines()
    graph = {}
    num_nodes = int(len(data)/2)
    for i in range(num_nodes):
        key_node = data[2*i].replace('\n', '')
        point_to = data[2*i+1]
        graph[key_node] = make_dictionary(point_to)
    return graph


def wgt(graph, node1, node2):
    return graph[node1][node2]


def find_shortest_path(name_txt_file, source, destination):
    graph = txt_to_graph(name_txt_file)
    v = source
    S = set()
    F = set(v)
    d = {}
    bk = {}
    d[v] = 0
    while (len(F) > 0):
        d_F = {}
        for node in F:
            d_F[node] = d[node]
        f = min(d_F, key=d_F.get)
        F.remove(f)
        S.add(f)
        for w in graph[f]:
            if (w not in S) and (w not in F):
                d[w] = d[f] + wgt(graph, f, w)
                F.add(w)
                bk[w] = f
            elif (d[f] + wgt(graph, f, w) < d[w]):
                d[w] = d[f] + wgt(graph, f, w)
                bk[w] = f

    shortest_path = [destination]
    n_back = destination
    while n_back != v:
        n_back = bk[n_back]
        shortest_path.append(n_back)
    shortest_path.reverse()
    return n_back, shortest_path


'''
if __name__ == '__main__':
    name_txt_file = '../graph1.txt'
    source = '1'
    destination = '3'
    res = find_shortest_path(name_txt_file,source,destination)
    print(res)
'''
