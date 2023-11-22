carrinho = list()

class produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    
class camisa(produto):
    def __init__(self, nome, preço, tamanho):
        super().__init__(nome, preço)
        self.tamanho = tamanho

    def TamanhoCamisa(quantia):
        tamanho = str(input(f'Qual tamanho da {quantia+1}ª camisa que você deseja? [P] [M] [G]: ')).strip().upper()[0]
        while True:
            if tamanho not in 'PMG':
                tamanho = str(input('Digite um tamanho válido [P] [M] [G]: ')).strip().upper()[0]
            else:
                break
        return tamanho

    def AdicionarCamisa(nome, preço, carrinho):
        print('Quantas unidades você quer?')
        quantidade = ValidarEscolha(0, 0, False)
        for c in range(quantidade):
            tamanho = camisa.TamanhoCamisa(c)
            camisa_vendida = camisa(nome, preço, tamanho)
            cesta = dict()
            cesta['Nome'] = camisa_vendida.nome
            cesta['Preço'] = camisa_vendida.preço
            cesta['Tamanho'] = camisa_vendida.tamanho
            carrinho.append(cesta)
        print(carrinho)
        menu()
    
class caneca(produto):
    def __init__(self, nome, preço, capacidade):
        super().__init__(nome, preço)
        self.capacidade = capacidade

    def CapacidadeCaneca(quantia):
        print(f'Qual a capacidade da {quantia+1}ª caneca que você deseja?')
        print('[P] 0,2L')
        print('[M] 0,3L')
        print('[G] 0,4L')
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
    
    def AdicionarCaneca(nome, preço, carrinho):
        print('Quantas unidades você quer?')
        quantidade = ValidarEscolha(0, 0, False)
        for c in range(quantidade):
            capacidade = caneca.CapacidadeCaneca(c)
            caneca_vendida = caneca(nome, preço, capacidade)
            cesta = dict()
            cesta['Nome'] = caneca_vendida.nome
            cesta['Preço'] = caneca_vendida.preço
            cesta['Capacidade'] = caneca_vendida.capacidade
            carrinho.append(cesta)
        print(carrinho)
        menu()


class quadrinho(produto):
    def __init__(self, nome, preço, autor, editora):
        super().__init__(nome, preço)
        self.autor = autor
        self.editora = editora

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
    print('[1] CAMISA - R$30,00')
    print('[2] CANECA')
    print('[3] QUADRINHO')
    print('-'*30)
    escolha = ValidarEscolha(1, 3)
    if escolha == 1:
        camisa.AdicionarCamisa('Camisa', 30, carrinho)
    elif escolha == 2:
        caneca.AdicionarCaneca('Caneca', 15, carrinho)



def menu(carrinho=None):
    if carrinho is None:
        carrinho = list()
    print('-'*30)
    print('LOJA GEEK')
    print('-'*30)
    print('[1] ADICIONAR PRODUTO AO CARRINHO')
    print('[2] REMOVER PRODUTO DO CARRINHO')
    print('[3] FINALIZAR COMPRA')
    escolha = ValidarEscolha(1, 3)
    if escolha == 1:
        AdicionarProduto()
    '''elif escolha == 2:
        RemoverProduto()
    elif escolha == 3:
        FinalizarCompra()'''



menu()