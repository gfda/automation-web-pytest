# Automação Selenium - Python - Pytest

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Estudo de automação de testes de aceitação (end-to-end) no site The-Internet, utilizando Selenium WebDriver e Pytest Framework.

O projeto foi estruturado utilizando o padrão de projetos Page Object Model (POM).

## Setup

### Instalação

Para iniciar o projeto, é necessário fazer a instalação de algumas ferramentas.

### *pipenv*

Utilizando o gerenciador de pacotes pip, podemos instalar o ambiente virtual do Python.

É importante garantir que o pip esteja instalado corretamente

```console
user@linux:~$ pip --version
```

![pip --version](images/pip_version.png)

Para instalar o pipenv

```console
user@linux:~$ pip install --user pipenv
```

![pip install --user pipenv](images/pip_install_pipenv.png)

É possível checar a versão do pipenv

```console
user@linux:~$ pipenv --version
```

![pipenv --version](images/pipenv_version.png)

Com o ambiente virtual instalado, basta iniciar o pipenv

```console
user@linux:~$ pipenv install
```

![pipenv install](images/pipenv_install_ini.png)

Após a execução do comando, deverão ser criados os arquivos de configuração **Pipfile** e **Pipfile.lock**.

### *pytest*

Com o ambiente virtual instalado e devidamente configurado, podemos instalar o framework que será utilizado para a execução dos testes, o pytest.

O comando irá instalar o pytest apenas no ambiente virtual

```console
user@linux:~$ pipenv install pytest
```

![pipenv install pytest](images/pipenv_install_pytest.png)

### Selenium WebDriver

O selenium poderá ser instalado dentro do próprio ambiente virtual utilizado durante este setup

```console
user@linux:~$ pipenv install selenium
```

![pipenv install selenium](images/pipenv_install_selenium.png)

## Testando

Para executar os testes é necessário chamar o pytest, este comando irá executar toda a suite de testes

```console
user@linux:~$ pipenv run python -m pytest
```

Se deseja executar casos de testes específicos, basta informar o caso

```console
user@linux:~$ pipenv run python -m pytest tests/<test_case>
```

## Dependências

Para gerar/atualizar o arquivo de dependências do projeto (*.lock*)

```console
user@linux:~$ pipenv lock
```

![pipenv lock](images/pipenv_lock.png)

## Recursos

* [Page Object](https://martinfowler.com/bliki/PageObject.html)
* [pytest](https://docs.pytest.org/en/latest/)
* [pipenv](https://pipenv.pypa.io/en/latest/)
* [Selenium-Python](https://selenium-python.readthedocs.io/)
* [the-internet](https://the-internet.herokuapp.com/)

## Autor

[Gustavo Dias A.](https://www.linkedin.com/in/gustavo-dias-alexandre-543568157/)

## License

Este projeto está sob a licença [MIT](LICENSE).
