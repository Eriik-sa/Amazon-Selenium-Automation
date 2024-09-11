from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_experimental_option("detach", True)  
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
driver.maximize_window()  
driver.get('https://www.amazon.com.br/')  

# Clica no menu "Todos" com tentativas de atualização da página
tentativas_todos = 3
for tentativa in range(tentativas_todos):
    try:
        todos = WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'hm-icon-label'))
        )
        todos.click()
        break  # Sai do loop se o clique for bem-sucedido
    except Exception as e:
        print(f'Tentativa {tentativa + 1}/{tentativas_todos} falhou ao clicar em "Todos". Atualizando a página...')
        driver.refresh()  # Atualiza a página
        time.sleep(3)  # Espera alguns segundos após a atualização
else:
    print('Não foi possível encontrar ou clicar em "Todos" após múltiplas tentativas.')

# Interage com o menu "Mais Vendidos"
try:
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "hmenu-item"))
    )
    menu_items = driver.find_elements(By.CLASS_NAME, "hmenu-item")
    for item in menu_items:
        if "Mais Vendidos" in item.text:
            item.click()
            break
    else:
        print("Item 'Mais Vendidos' não encontrado no menu.")        
except Exception as e:
    print('Erro ao interagir com o menu:', e)

# Clica em "Computadores e Informática"
try:
    computadores_informatica = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Computadores e Informática"]'))
    )
    computadores_informatica.click()
except Exception as e:
    print("Não foi possível encontrar o link 'Computadores e Informática':", e)

# Tenta clicar no link da impressora com múltiplas tentativas e atualização de página
tentativas = 3
for tentativa in range(tentativas):
    try:
        impressora = WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="B098YHFT9S"]/a'))
        )
        impressora.click()
        break  # Sai do loop se o clique for bem-sucedido
    except Exception as e:
        print(f'Tentativa {tentativa + 1}/{tentativas} falhou. Atualizando a página...')
        driver.refresh()  # Atualiza a página
        time.sleep(3)  # Espera alguns segundos após a atualização
else:
    print('Não foi possível encontrar ou clicar na impressora após múltiplas tentativas.')

# Tenta adicionar ao carrinho
try:
    carrinho = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]'))
    )
    carrinho.click()
except Exception as e:
    print('Não foi possível encontrar o botão de carrinho')

# Tenta clicar em "Não, obrigado" na oferta de proteção
try:
    nao_obrigado = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="attachSiNoCoverage"]/span/input'))
    )
    nao_obrigado.click()
except Exception as e:
    print('Não foi possível encontrar o "não, obrigado"')

# Tenta clicar no botão para visualizar o carrinho
try:
    olhar_carrinho = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="attach-sidesheet-view-cart-button"]/span/input'))
    )
    olhar_carrinho.click()
except Exception as e:
    print('Não foi possível encontrar o carrinho final', e)

# Barra de pesquisa
try:
    barra_de_pesquisa = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    barra_de_pesquisa.send_keys("notebook")
    barra_de_pesquisa.send_keys(Keys.RETURN)
except Exception as e:
    print('Não foi possível encontrar a barra de pesquisa', e)

# Tenta clicar no notebook
try:
    notebook_acer = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, 'a-autoid-7-announce'))
    )
    notebook_acer.click()
except Exception as e:
    print("Não foi possível encontrar o notebook", e)

# Tenta visualizar o carrinho no canto superior
try:
    carrinho_final = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'nav-cart-count'))
    )
    carrinho_final.click()
except Exception as e:
    print("Não foi possível encontrar o ícone do carrinho no canto superior direito:", e)

input("Pressione Enter para sair.")
