
with open("123.txt","w") as f:
    f.write("这是修改后的内容")


with open("123.txt","r") as b:
    res = b.read(100)
    print(res)
with open("123.txt","a") as f:
    f.write("追加")
with open("123.txt","r") as b:
    res = b.read(100)
    print(res)

import xlrd
def readtools(wjm,sheetname):
    excel = xlrd.open_workbook(wjm)   #打开文件
    table = excel.sheet_by_name(sheetname)  #选择需要打开的sheet页
    #value = table.cell_value(0,0)      #读取0,0的坐标值 
    # print(value) 
    hang = table.nrows
    lie = table.ncols
    newnumber = []
    for i in range(1,hang):
        newnumber.append(table.row_values(i)) 
    return newnumber



res = readtools("接口测试用例模板.xlsx","Cases")
print(res)




