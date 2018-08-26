def make_dictionary(text):
    text = text.replace('\n', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text_list = text.split(',')
    num_out_edges = int(len(text_list)/2)
    out_edges = {}
    for j in range(num_out_edges):
        out_edges[float(text_list[2*j])] = float(text_list[2*j+1])
    return out_edges


def txt_to_graph(filename):
    with open(filename) as f:
        data = f.readlines()
    graph = {}
    num_nodes = int(len(data)/2)
    for i in range(num_nodes):
        key_node = float(data[2*i].replace('\n', ''))
        point_to = data[2*i+1]
        graph[key_node] = make_dictionary(point_to)
    return graph


def wgt(graph, node1, node2):
    return graph[node1][node2]


def find_negative_cycles(name_txt_file):
    graph = txt_to_graph(name_txt_file)
    d = {}
    p = {}
    source = 1
    tV = len(graph)
    tE = sum([len(graph[e]) for e in graph])
    for e in graph:
        d[e] = float('inf')
        p[e] = 0
    d[source] = 0

    for i in range(tV-1):
        for u in graph:
            for v in graph[u]:
                if (d[u] != float('inf')) and (d[v] > d[u] + wgt(graph, u, v)):
                    d[v] = d[u] + wgt(graph, u, v)
                    p[v] = u

    for i in range(tE):
        for u in graph:
            for v in graph[u]:
                if(d[u] != float('inf')) and (d[v] > d[u] + wgt(graph, u, v)):
                    cycle_list = [u]
                    prev_node = p[u]
                    while prev_node != u:
                        cycle_list.append(prev_node)
                        prev_node = p[prev_node]
                    cycle_list.append(u)
                    cycle_list.reverse()
                    return cycle_list
    return []


'''
if __name__ == '__main__':
    name_txt_file1 = '/Users/kgu/PycharmProjects/ORIE5270/ORIE5270/hw3/graph1.txt'
    print(find_negative_cycles(name_txt_file1))
    name_txt_file2 = '/Users/kgu/PycharmProjects/ORIE5270/ORIE5270/hw3/graph2.txt'
    print(find_negative_cycles(name_txt_file2))
'''
