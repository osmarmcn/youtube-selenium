from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do WebDriver
opcoes = Options()  # Cria um objeto Options para passar opções ao ChromeDriver
opcoes.add_experimental_option("detach", True)  # Mantém o navegador aberto após o script finalizar
driver = webdriver.Chrome(options=opcoes)  # Inicializa o ChromeDriver com as opções configuradas

# Navegue para o YouTube
driver.get("https://www.youtube.com")  # Abre o YouTube no navegador
driver.maximize_window()  # Maximiza a janela do navegador

# Aguardar a barra de pesquisa estar presente e interativa
search_box = WebDriverWait(driver, 10).until(  # Aguarda até 10 segundos para que o elemento esteja presente
    EC.presence_of_element_located((By.NAME, 'search_query'))  # Condição de espera: elemento estar presente pelo nome
)
search_box.send_keys("blue bird")  # Digita "blue bird" na barra de pesquisa

# Aguardar o botão de pesquisa estar presente e interativo
search_button = WebDriverWait(driver, 10).until(  # Aguarda até 10 segundos para que o botão esteja clicável
    EC.element_to_be_clickable((By.XPATH, '//*[@id="search-icon-legacy"]'))  # Condição de espera: elemento estar clicável pelo XPath
)
search_button.click()  # Clica no botão de pesquisa

video_title_to_click = "Naruto Shippuden Opening 3 | Blue Bird (HD)"  # Define o título do vídeo a ser clicado
video_titles = WebDriverWait(driver, 10).until(  # Aguarda até 10 segundos para que os elementos do vídeo estejam presentes
    EC.presence_of_all_elements_located((By.XPATH, '//a[@id="video-title"]'))  # Condição de espera: todos os elementos de vídeo presentes pelo XPath
)

# Itera sobre a lista de títulos de vídeo encontrados
for video_title in video_titles:
    # Verifica se o título do vídeo desejado está na lista de vídeos encontrados (ignorando maiúsculas/minúsculas)
    if video_title_to_click.lower() in video_title.get_attribute("title").lower():
        video_title.click()  # Clica no vídeo desejado
        print(f"Vídeo '{video_title_to_click}' encontrado e clicado!")  # Imprime mensagem de confirmação
        break  # Sai do loop após encontrar e clicar no vídeo

# Aguardar o vídeo começar a tocar ou o botão de pular anúncio aparecer
try:
    skip = WebDriverWait(driver, 10).until(  # Aguarda até 10 segundos para que o botão de pular anúncio esteja clicável
        EC.element_to_be_clickable((By.CLASS_NAME, 'ytp-skip-ad-button'))  # Condição de espera: botão de pular anúncio estar clicável pelo nome da classe
    )
    skip.click()  # Clica no botão de pular anúncio
    print("Anúncio pulado.")  # Imprime mensagem de confirmação
except:
    print("Sem anúncio para pular ou botão de pular não encontrado.")  # Imprime mensagem se não houver anúncio ou o botão não for encontrado

# Aguardar o botão de tela cheia estar presente e interativo
full = WebDriverWait(driver, 15).until(  # Aguarda até 15 segundos para que o botão de tela cheia esteja clicável
    EC.element_to_be_clickable((By.CLASS_NAME, 'ytp-fullscreen-button'))  # Condição de espera: botão de tela cheia estar clicável pelo nome da classe
)
full.click()  # Clica no botão de tela cheia
print("Vídeo colocado em tela cheia.")  # Imprime mensagem de confirmação

# Encerrar a sessão do driver
# driver.quit() # Descomente esta linha se quiser fechar o navegador automaticamente
