""" O programa utiliza um interator para iterar os dados da API da tabela FIPE
e retornar todos os modelos de carros de uma determinada marca de veículos"""

import requests

# FUNÇÃO PARA RETORNAR TODOS AS MARCAS E SEUS RESPECTIVOS CÓDIGOS

def marcas():
    # url da api
    url_marcas = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
    headers = {'User-Agent': 'Myapp/1.0'}

    # fazendo a solicitação para api
    response = requests.get(url_marcas, headers=headers)

    # verificando a solicitação
    if response.status_code == 200:
        marcas = response.json()
    else:
        print('Erro')

    # imprimindo relação de marcas
    for marca in marcas:
        print('Marca: {nome:<18} Código: {codigo}'.format(**marca))


#################################################
# CLASSE INTERATOR PARA RETORNAR TODOS OS CARROS DE UMA DETERMINADA MARCA DE VEÍCULO

class CarrosInterator:
    def __init__(self, id):
        
        # url da api
        url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/{}/modelos'.format(id)

        # fazendo a solicitação para api
        response = requests.get(url)

        # verificando a solicitação
        if response.status_code == 200:
            carros = response.json()
        else:
            print('Erro')

        # obtendo valores para o Dict 'modelos'
        self.modelos = carros['modelos']

        # instanciando nosso estatual atual e final
        self.current = 0
        self.end = len(self.modelos)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        
        result = self.modelos[self.current]
        self.current += 1
        return result 



#################################################
# INTERFACE DO USUÁRIO

# chama função para imprimir todas as marcas e seus códigos
print('********** MARCAS DISPONÍVEIS **********\n')
marcas()

# seleciona a marca desejada
print('\n----------------------------------------\n')
marca_selecionada = input('Digite o código da marca desejada: ')

# chama classe interator para imprimir todos os modelos da marca selecionada
print('\n********** MODELOS DA MARCA SELECIONADA **********\n')

modelos = CarrosInterator(marca_selecionada)
for modelo in modelos:
    print('Código: {codigo:<8} Modelo: {nome}'.format(**modelo))

print('\n----------------------------------------\n')