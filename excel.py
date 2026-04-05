from openpyxl import Workbook

def salvar_excel(dados):
    wb = Workbook()
    ws = wb.active
    ws.title = "Comparador"

    ws.append(["Site","Produto", "Preco"])

    for item in dados:
        ws.append([
            item["site"],
            item["produto"],
            item["preco"]
        ])

    wb.save("produtos.xlsx")
