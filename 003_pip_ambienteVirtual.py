# pip: instala globalmente se não tivermos um máquina virtual
# isso gera um problema, pois vai dar problema se formos trabalhar em dois (ou mais) projetos onde tem-se versões de pacotes diferente


# pip install virtualenv
# Criar: virtualenv venv
# Ativar: .\venv\Scripts\activate
# Boa prática, colocar os pacotes em um txt: pip freeze > requirements.txt

"""
Para instalar todos os pacotes do requirements.txt

virtualenv venv
..\venv\Scripts\activate
pip install -r requirements.txt
"""


