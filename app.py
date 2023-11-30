from random import randint

carrinho = list()

class produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço
        self.numero_serie = None

    
class camisa(produto):
    def __init__(self, nome, preço, tamanho):
        super().__init__(nome, preço)
        self.tamanho = tamanho
        self.numero_serie = self.gerar_numero_serie(5)

    def gerar_numero_serie(self, multiplo):
        return randint(1, 1000) * multiplo

    def TamanhoCamisa(quantia):
        print('[P] R$30,00')
        print('[M] R$35,00')
        print('[G] R$40,00')
        tamanho = str(input(f'Qual tamanho da {quantia+1}ª camisa que você deseja? [P] [M] [G]: ')).strip().upper()[0]
        print('-'*30)
        while True:
            if tamanho not in 'PMG':
                tamanho = str(input('Digite um tamanho válido [P] [M] [G]: ')).strip().upper()[0]
            else:
                break
        return tamanho

    def AdicionarCamisa(nome, carrinho):
        print('Quantas unidades você quer?')
        quantidade = ValidarEscolha(0, 0, False)
        for c in range(quantidade):
            tamanho = camisa.TamanhoCamisa(c)
            if tamanho == 'P':
                preço = 30
            elif tamanho == 'M':
                preço = 35
            elif tamanho == 'G':
                preço = 40
            camisa_vendida = camisa(nome, preço, tamanho)
            cesta = dict()
            cesta['Nome'] = camisa_vendida.nome
            cesta['Preço'] = camisa_vendida.preço
            cesta['Tamanho'] = camisa_vendida.tamanho
            cesta['Nº Serie'] = camisa_vendida.numero_serie
            carrinho.append(cesta)
        menu()
    
class caneca(produto):
    def __init__(self, nome, preço, capacidade):
        super().__init__(nome, preço)
        self.capacidade = capacidade
        self.numero_serie = self.gerar_numero_serie(3)

    def gerar_numero_serie(self, multiplo):
        return randint(1, 1000) * multiplo

    def CapacidadeCaneca(quantia):
        print(f'Qual a capacidade da {quantia+1}ª caneca que você deseja?')
        print('-'*30)
        print('[P] 0,2L - R$10,00')
        print('[M] 0,3L - R$15,00')
        print('[G] 0,4L - R$20,00')
        tamanho = str(input('DIGITE: ')).strip().upper()[0]
        while True:
            if tamanho not in 'PMG':
                tamanho = str(input('Digite uma capacidade válido [P] [M] [G]: ')).strip().upper()[0]
            else:
                if tamanho == 'P':
                    capacidade = 0.2
                elif tamanho == 'M':
                    capacidade = 0.3
                elif tamanho == 'G':
                    capacidade = 0.4
                break
        return capacidade
    
    def AdicionarCaneca(nome, carrinho):
        print('Quantas unidades você quer?')
        quantidade = ValidarEscolha(0, 0, False)
        for c in range(quantidade):
            capacidade = caneca.CapacidadeCaneca(c)
            if capacidade == 0.2:
                preço = 10
            elif capacidade == 0.3:
                preço = 15
            elif capacidade == 0.4:
                preço = 20
            caneca_vendida = caneca(nome, preço, capacidade)
            cesta = dict()
            cesta['Nome'] = caneca_vendida.nome
            cesta['Preço'] = caneca_vendida.preço
            cesta['Capacidade'] = caneca_vendida.capacidade
            cesta['Nº Serie'] = caneca_vendida.numero_serie
            carrinho.append(cesta)
        menu()


class quadrinho(produto):
    def __init__(self, nome, preço, autor, editora):
        super().__init__(nome, preço)
        self.autor = autor
        self.editora = editora
        self.numero_serie = self.gerar_numero_serie(7)

    def gerar_numero_serie(self, multiplo):
        return randint(1, 1000) * multiplo

    def AdicionarQuadrinho(carrinho):
        estoque_hq = [{'Nome': 'HQ Turma da Mônica', 'Preço': 10, 'Autor': 'Mauricio de Sousa', 'Editora': 'Panini'}, {'Nome': 'HQ Invencível', 'Preço': 50, 'Autor': 'Robert Kirkman', 'Editora': 'HQM'}, {'Nome': 'HQ Scott Pilgrim', 'Preço': 40, 'Autor': "Bryan Lee O'Malley", 'Editora': 'Quadrinhos na Cia'}]
        print('Quantas unidades você quer?')
        quantidade = ValidarEscolha(0, 0, False)
        for c in range(quantidade):
            print('-'*30)
            print(f'Qual o {c+1}º quadrinho você quer comprar?')
            for c in range(len(estoque_hq)):
                print(f'[{c+1}] {estoque_hq[c]["Nome"]}')
            escolha = ValidarEscolha(1, 3)
            quadrinho_vendida = quadrinho(estoque_hq[escolha-1]['Nome'], estoque_hq[escolha-1]['Preço'], estoque_hq[escolha-1]['Autor'], estoque_hq[escolha-1]['Editora'])
            cesta = dict()
            cesta['Nome'] = quadrinho_vendida.nome
            cesta['Preço'] = quadrinho_vendida.preço
            cesta['Autor'] = quadrinho_vendida.autor
            cesta['Editora'] = quadrinho_vendida.editora
            cesta['Nº Serie'] = quadrinho_vendida.numero_serie
            carrinho.append(cesta)
        menu()

def ValidarEscolha(min, max, entre_números=True):
    while True:
        try:
            escolha = int(input('DIGITE: '))
            while (escolha > max or escolha < min) and entre_números is True:
                print('Digite um valor válido')
                escolha = int(input('DIGITE: '))
            while escolha < min and entre_números is False:
                print('Digite um valor válido')
                escolha = int(input('DIGITE: '))
        except:
            print('Digite um valor válido')
        else:
            break
    return escolha

def AdicionarProduto():
    print('-'*30)
    print('ADICIONAR PRODUTO AO CARRINHO')
    print('-'*30)
    print('[1] CAMISA')
    print('[2] CANECA')
    print('[3] QUADRINHO')
    print('-'*30)
    escolha = ValidarEscolha(1, 3)
    if escolha == 1:
        camisa.AdicionarCamisa('CAMISA', carrinho)
    elif escolha == 2:
        caneca.AdicionarCaneca('CANECA', carrinho)
    elif escolha == 3:
        quadrinho.AdicionarQuadrinho(carrinho)

def RemoverProduto():
    if len(carrinho) == 0:
        print('-'*30)
        print('SEU CARRINHO ESTÁ VAZIO!')
        menu()
    else:
        print('-'*30)
        print(f'{"PRODUTO":<25}', end='')
        print(f'{"PREÇO":<20}')
        print('-'*30)
        for c in range(len(carrinho)):
            print(f'[{c+1}] ', end='')
            for v in carrinho[c].values():
                print(f'{v:<20} ', end='')
            print()
        escolha = ValidarEscolha(1, len(carrinho), True)
        carrinho.pop(escolha-1)
        menu()

def Promoção():
    carrinho_ordenado = sorted(carrinho, key=lambda x: x['Preço'])
    hq_menor_preço = contador_camisa = 0

    for c in range(len(carrinho_ordenado)):
        for k, v in carrinho_ordenado[c].items():
            if k == 'Autor':
                hq_menor_preço += 1
            elif v == 'CAMISA':
                contador_camisa += 1

    hq_menor_preço = hq_menor_preço // 5
    contador_camisa = contador_camisa // 4

    for c in carrinho_ordenado:
        if 'Autor' in c and hq_menor_preço > 0:
            c['Preço'] = 0
            hq_menor_preço -= 1

    for c in carrinho_ordenado:
        if contador_camisa > 0:
            caneca_vendida = caneca('CANECA', 0, 0.3)
            cesta = dict()
            cesta['Nome'] = caneca_vendida.nome
            cesta['Preço'] = caneca_vendida.preço
            cesta['Capacidade'] = caneca_vendida.capacidade
            cesta['Nº Serie'] = caneca_vendida.numero_serie
            carrinho_ordenado.append(cesta)
            contador_camisa -= 1

    carrinho_ordenado = sorted(carrinho_ordenado, key=lambda x: x['Preço'])

    return carrinho_ordenado


def FinalizarCompra():
    print('-'*30)
    print('FINALIZANDO O CAIXA')
    print('-'*30)
    carrinho_ordenado = Promoção()

    print(f'NA COMPRA DE 4 CAMISAS, GANHE UMA CANECA DE BRINDE')
    print(f'NA COMPRA DE 5 HQ, O MAIS BARATO SAI DE GRAÇA')
    print('-'*30)
    print(f'{"PRODUTO":<21}', end='')
    print(f'{"PREÇO":<20}')
    for c in range(len(carrinho_ordenado)):
        for v in carrinho_ordenado[c].values():
            print(f'{v:<20} ', end='')
        print()

def menu():
    print('-'*30)
    print(f'{"LOJA GEEK":^30}')
    print('-'*30)
    print('[1] ADICIONAR PRODUTO AO CARRINHO')
    print('[2] REMOVER PRODUTO DO CARRINHO')
    print('[3] FINALIZAR COMPRA')
    escolha = ValidarEscolha(1, 3)
    if escolha == 1:
        AdicionarProduto()
    elif escolha == 2:
        RemoverProduto()
    elif escolha == 3:
        FinalizarCompra()


menu()