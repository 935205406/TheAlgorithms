def bellman_frod(graph, E, V, src):
    """
    贝尔曼福特算法

    :param graph: 一个[{},{},{}]列表对象，{"src": src,"dst": dst, "weight": weight}
    :param E: 边的个数
    :param V: 点的个数
    :param src: 起点
    :return:
    """
    dist = [float("inf") for i in range(V)]  # 存储所有点到src点的最短距离
    dist[src] = 0.0  # src点到自己的距离是0
    parent = [0 for i in range(V)]  # 存储 在最短距离的走法中，该点的上一个点是哪一个
    parent[src] = -1  # src到自己的走法中，没有上一个点，设为-1
    for i in range(V - 1):  # 按照算法，迭代 V-1 次
        changed = False
        for j in range(E):  # 每条边都进行算法规定的计算
            u = graph[j]["src"]  # 边的起点
            v = graph[j]["dst"]  # 边的终点
            w = graph[j]["weight"]  # 边的权重
            # 计算是否可以更新
            if dist[u] != float("inf") and (dist[v] > dist[u] + w):
                changed = True
                dist[v] = dist[u] + w
                parent[v] = u
        # 优化：如果在 V-1 次的迭代中，发现从某次开始，不再更新数据了，则后续的迭代都不会更新数据，可以直接跳过
        if not changed:
            print(
                "total iterator should be %d, %dth iterator find data not update anymore,remain iterator will breake "
                "and program jump to negative check" % (V - 1, i))
            break
    # 迭代了 V-1 次，最后再运行一次， make sure there are no negatively weighted cycles
    negative = 0
    for j in range(E):  # 最后一次对所有边进行计算
        u = graph[j]["src"]  # 边的起点
        v = graph[j]["dst"]  # 边的终点
        w = graph[j]["weight"]  # 边的权重
        # 计算是否可以更新
        if dist[u] != float("inf") and (dist[v] > dist[u] + w):
            negative = 1
            break
    if negative:
        print("there are negatively weighted cycles")
    else:
        print("the shotest distense from vertice %d and route are below:\n" % src)
        show_graph(dist, parent)


def show_graph(dist, parent):
    """打印图中的距离与走法

    :param dist: 距离list
    :param parent: 该节点的上一个节点的list
    :return:
    """
    print("shortest distance\t\troute link")
    for n, distance in enumerate(dist):
        print("%d\t\t%s" % (distance, show_route(parent, n, "")))


def show_route(parent, n, route_link):
    """返回最短距离走法的字符串表示

    :param parent: 该节点的上一个节点的list
    :param n: 目的节点
    :param route_link: 当前字符串
    :return: 最短距离走法的字符串表示，如 2 -> 1 -> 0
    """
    if parent[n] == -1:
        return str(n) + route_link
    route_link = " -> " + str(n) + route_link
    return show_route(parent, parent[n], route_link)


def test_show_route():
    parent = [2, -1, 3, 1]
    route = show_route(parent, 0, "")
    print(route)


def test_show_graph():
    dist = [1, 0, 3, 2]
    parent = [2, -1, 3, 1]
    show_graph(dist, parent)


if __name__ == '__main__':
    # test_show_route()
    # test_show_graph()
    # V = 5
    # E = 8
    # graph = [
    #     {"src": 0,"dst": 1, "weight": float(-1)},
    #     {"src": 0,"dst": 2, "weight": float(4)},
    #     {"src": 1,"dst": 2, "weight": float(3)},
    #     {"src": 1,"dst": 3, "weight": float(2)},
    #     {"src": 1,"dst": 4, "weight": float(2)},
    #     {"src": 3,"dst": 2, "weight": float(5)},
    #     {"src": 3,"dst": 1, "weight": float(1)},
    #     {"src": 4,"dst": 3, "weight": float(-3)},
    #     ]  # 初始化graph
    # src = 0
    V = int(input("请输入节点数："))
    E = int(input("请输入连线数："))
    graph = [dict() for i in range(E)]  # 初始化graph
    print("请输入连线信息：")
    for i in range(E):
        print("输入第 %d 条连线信息：" % (i + 1))
        graph[i]["src"] = int(input("请输入连线起点的节点数字："))
        graph[i]["dst"] = int(input("请输入连线终点的节点数字："))
        graph[i]["weight"] = float(input("请输入连线的距离："))
    src = int(input("请输入起点节点的数字："))
    print("正在计算所有节点到 %d 节点的最短距离与路径图：\n")
    bellman_frod(graph, E, V, src)
