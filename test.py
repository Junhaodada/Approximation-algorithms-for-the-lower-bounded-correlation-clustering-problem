from Graph import Graph, test1, test2


def CreateG2(n, L):
    G = Graph(n, L)
    G.CreateRandomG2()
    print('创建成功')
    # G.createG1()


n = 80
L = 32
CreateG2(n, L)
# test2(n, L, tag=2)


# test1(n, L)
# b = 0.2
# for i in range(10, 101, 10):
#     print('N={} L={}:'.format(i, int(i*b)))
#     test1(i, int(i*b))
