from abc import ABC, abstractmethod

# Classe abstrata para pagamento
class Pagamento(ABC):
    def __init__(self, valor, metodo_de_pagamento):
        self.valor = valor
        self.metodo_de_pagamento = metodo_de_pagamento
        
    @abstractmethod
    def processar_pagamento(self):
        pass

# Subclasse para pagamento com cartão de crédito
class Credito(Pagamento):
    def __init__(self, valor, metodo_de_pagamento):
        super().__init__(valor, metodo_de_pagamento)

    def processar_pagamento(self, limite, numero, validade, cvv):
        self.limite = limite
        self.numero = numero
        self.validade = validade
        self.cvv = cvv
        print("Pagamento com cartão de crédito selecionado com sucesso.")

# Subclasse para pagamento via Pix
class Pix(Pagamento):
    def __init__(self, valor, metodo_de_pagamento):
        super().__init__(valor, metodo_de_pagamento)
    
    def processar_pagamento(self, chave, tipo):
        self.chave = chave
        self.tipo = tipo
        print("Pagamento via Pix selecionado com sucesso.")

# Classe para representar um pedido
class Pedido:
    def __init__(self, total, fechado=False):
        self.total = total
        self.fechado = fechado
    
    # Método para realizar ações no pedido, como processar o pagamento e fechá-lo
    def acoes(self, pagamento):
        if self.fechado:
            print("Pagamento cancelado, pedido já finalizado.")
            return
        self.fechado = True
        print("Pagamento concluido, pedido finalizado com sucesso.")

# Função que simula um sistema de pedidos
def main():
    # Criar um pedido
    pedido_1 = Pedido(100.0)
    pedido_2 = Pedido(500)

    # Criar instâncias de pagamento com cartão de crédito e Pix
    pagamento_credito = Credito(100.0, "cartão de crédito")
    pagamento_pix = Pix(100.0, "Pix")


    # Processar o pagamento do pedido com cartão de crédito e Pix
    pedido_1.acoes(pagamento_credito.processar_pagamento(limite=1000, numero="1234 5678 9012 3456", validade="12/24", cvv="123"))
    pedido_2.acoes(pagamento_pix.processar_pagamento(chave="(00) 9 0000-0000", tipo="Telefone"))
    pedido_2.acoes(pagamento_credito.processar_pagamento(limite=1000, numero="1234 5678 9012 3456", validade="12/24", cvv="123"))

# Chamar a função que simula o sistema
main()
