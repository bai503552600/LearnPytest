import xlrd

# todo 打开excle
xl = xlrd.open_workbook(r'D:\bai\Fiddler_test\金融1.1.xlsx')
table = xl.sheets()[0]
rows = table.nrows
nums=[]
for i in range(4, 9):
    datas = {}
    data1 = table.cell(i, 7).value
    datas['casedata'] = data1
    data2 = table.cell(i, 9).value
    datas['expect'] = data2
    nums.append(datas)
print(nums)




