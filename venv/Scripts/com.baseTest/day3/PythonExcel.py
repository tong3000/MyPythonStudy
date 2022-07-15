"""
python第三方库
Write a workbook

"""

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

#创建对象
wb = Workbook()
#文件名
dest_filename = 'empty_book.xlsx'
#运行excel工作表
ws1 = wb.active
#设置sheet1的名称
ws1.title = "range names"

#39行*599列
for row in range(1, 40):
    ws1.append(range(600))

#设置sheet2的名称
ws2 = wb.create_sheet(title="Pi")

#sheet2的F5单元格值为3.14
ws2['F5'] = 3.14

ws3 = wb.create_sheet(title="Data")
for row in range(10, 20):
    for col in range(27, 54):
        _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
print(ws3['AA10'].value)

ws4 = wb.create_sheet(title="my_sheet")
for i in range(1,31):
    ws4.cell(column=1,row=i).value = "test"

#保存文件
wb.save(filename = dest_filename)