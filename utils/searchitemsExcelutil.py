import openpyxl

def searchitemExcel_load():
    workbook = openpyxl.load_workbook("testdata\\searchitem.xlsx")
    sheet = workbook["Sheet1"]
    search_items = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        product = row[0]
        search_items.append(str(product))
    workbook.close()
    #print(search_items)
    return search_items




