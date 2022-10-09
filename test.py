# from asyncio.windows_events import NULL
# import openpyxl

# book = openpyxl.Workbook()

# book.create_sheet('Sheet')
# sheet = book['Sheet']

# sheet.cell(1, 1).value = None
# sheet.cell(2, 1).value = '姓名'
# # sheet.cell(3, 1).value = '林新发'
# # del book['Sheet']
# book.save(u'我的表格.xlsx')
# book.close()

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
