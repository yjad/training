import openpyxl as xl
from openpyxl.chart import Reference, BarChart

wb = xl.load_workbook('prices.xlsx')
sheet = wb['Sheet1']
for row in range (3,8):
    cell = sheet[f'd{row}']
    corrected_value = cell.value * 0.9

    new_cell = sheet[f'F{row}']
    new_cell.value = corrected_value

    print (f'Old value: {cell.value}, corrected_value: {new_cell.value}')

values = Reference(sheet, min_row= 6, min_col=3, max_row= 6,max_col= 7)
chart = BarChart()
chart.add_data(values)
sheet.add_chart(chart, 'b10')

wb.save('prices_2.xlsx')
