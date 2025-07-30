import hashlib
import datetime

class Bloco:
    def __init__(self, index, timestamp, dados, hash_anterior):
        self.index = index
        self.timestamp = timestamp
        self.dados = dados
        self.hash_anterior = hash_anterior
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') + 
                   str(self.timestamp).encode('utf-8') + 
                   str(self.hash_anterior).encode('utf-8') + 
                   str(self.dados).encode('utf-8'))
        return sha.hexdigest()
    
class Cadeia_blocos:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Bloco(0, datetime.datetime.now(), 'Genesis Block', '0')
    
    def adicionar_bloco(self, novo_bloco):
        novo_bloco.hash_anterior = self.chain[-1].hash
        novo_bloco.hash = novo_bloco.calculate_hash()
        self.chain.append(novo_bloco)

    def validar_bloco(self):
        for i in range(1 , len(self.chain)):
            bloco_atual = self.chain[i]
            bloco_anterior = self.chain[i-1]

            if bloco_atual.hash != bloco_atual.calculate_hash():
                return False
            if bloco_anterior.hash != bloco_anterior.calculate_hash():
                return False
            
            return True
        
BlockChain = Cadeia_blocos()

venda_1 = {
    'item' : 'Bolsa maquiagens Franciny',
    'valor': '129.99',
    'local': 'Shopping Morumbi' 
}

venda_2 = {
    'item' : 'Caderno Escolar 10 ',
    'valor': '24.99',
    'local': 'Shopping Morumbi' 
}

venda_3 = {
    'item' : 'Kit material escolar',
    'valor': '19.99',
    'local': 'Shopping Interlagos' 
}

BlockChain.adicionar_bloco(Bloco(1, datetime.datetime.now(), venda_1, BlockChain.chain[-1].hash_anterior))
BlockChain.adicionar_bloco(Bloco(2, datetime.datetime.now(), venda_2, BlockChain.chain[-1].hash_anterior))
BlockChain.adicionar_bloco(Bloco(3, datetime.datetime.now(), venda_3, BlockChain.chain[-1].hash_anterior))

#print(f'Essa blockchain é válida? {str(BlockChain.validar_bloco())}')

def mostrar_blocos():
    for contador in range(len(BlockChain.chain)-1):
        print(f'index: {BlockChain.chain[contador].index}')
        print(f'data: {BlockChain.chain[contador].timestamp}')
        print(f'hash: {BlockChain.chain[contador].hash}')
        mostrar_dados_unico(contador)

        print(f'hash do bloco anterior f{BlockChain.chain[contador].hash_anterior}')

def mostrar_dados_unico(limitador):
    for contador in range(limitador):
        print("-----------------------------")
        for chave in BlockChain.chain[contador+1].dados: 
            print(BlockChain.chain[contador+1].dados[chave])
        print("-----------------------------")

mostrar_blocos()