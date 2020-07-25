"""
Neste módulo terá fixtures compartilhadas.
"""

import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope="session"):
  
  #Ler o arquivo json
  with open('config.json') as config_file:
    config = json.load(config_file)
  
  #Garante que os valores estão de acordo
  assert config['browser'] in ['Chrome', 'Headless Chrome']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  return config

@pytest.fixture
def browser(config):

  # Inicializa uma instância do browser.
  if config['browser'] == 'Chrome':
    b = selenium.webdriver.Chrome(executable_path="drivers/chromedriver")
  elif config['browser'] == 'Headless Chrome':
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('headless')
    b = selenium.webdriver.Chrome(executable_path="drivers/chromedriver", options=opts)
  else:
    raise Exception(f'Browser "{config["browser"]}" não suportado!')

  # Maximiza a janela 
  b.maximize_window()
  # Aguarda até a aparição do elemento
  b.implicitly_wait(config['implicit_wait'])
  
  # Retorna uma instância do WebDriver para o setup
  yield b

  # Finaliza a instância do browser
  b.quit()