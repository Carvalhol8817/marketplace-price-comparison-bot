from playwright.sync_api import sync_playwright


def comparar_precos(produto):
    resultados = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Mercado Livre
        busca = produto.replace(" ", "-")
        page.goto(f"https://lista.mercadolivre.com.br/{busca}")
        page.wait_for_selector("li.ui-search-layout__item")

        itens = page.locator("li.ui-search-layout__item").all()

        for item in itens[:5]:
            try:
                nome = item.locator("h3").inner_text()
                preco = item.locator(".andes-money-amount__fraction").first.inner_text()

                resultados.append({
                    "site": "Mercado Livre",
                    "produto": nome,
                    "preco": f"R${preco}"
                })
            except Exception as e:
                print(f"Erro ao capturar item: {e}")
                continue

        browser.close()

    return resultados