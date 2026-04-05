from bot import comparar_precos
from excel import salvar_excel

def main():
    produto = input("Digite o produto para pesquisar: ")

    try:
        dados = comparar_precos(produto)
        salvar_excel(dados)
        print("Comparacao salva em produtos.xlsx")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()