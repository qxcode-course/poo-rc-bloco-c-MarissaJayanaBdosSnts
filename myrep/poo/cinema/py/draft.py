class Cliente:
    def __init__(self, identificador: str, telefone: int):
        self.identificador = identificador
        self.telefone = telefone

    def __str__(self):
        return self.identificador + ":" + str(self.telefone)

    def obter_telefone(self):
        return self.telefone
  
    def obter_identificador(self):
        return self.identificador
  
    def definir_identificador(self, novo_id: str):
        self.identificador = novo_id

    def definir_telefone(self, novo_telefone: int):
        self.telefone = novo_telefone


class Cinema:
    def __init__(self, capacidade: int):
        self.assentos = [None for _ in range(capacidade)]

    def procurar_cliente(self, nome: str) -> int:
        for i, cadeira in enumerate(self.assentos):
            if cadeira is not None and cadeira.obter_identificador() == nome:
                return i
        return -1

    def verificar_indice(self, indice: int) -> bool:
        return 0 <= indice < len(self.assentos)
    
    def reservar(self, identificador: str, telefone: int, indice: int) -> bool:
        if not self.verificar_indice(indice):
            print("fail: cadeira nao existe")
            return False

        if self.assentos[indice] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        
        # verificar se cliente já existe
        if self.procurar_cliente(identificador) != -1:
            print("fail: cliente ja esta no cinema")
            return False

        self.assentos[indice] = Cliente(identificador, telefone)
        return True
    
    def cancelar(self, identificador: str):
        posicao = self.procurar_cliente(identificador)
        if posicao == -1:
            print("fail: cliente nao esta no cinema")
            return False
        
        self.assentos[posicao] = None
        return True
    
    def __str__(self):
        texto = "["
        for cadeira in self.assentos:
            if cadeira is None:
                texto += "- "
            else:
                texto += str(cadeira) + " "
        texto = texto.strip()
        texto += "]"
        return texto


def main():
    sala = None
    while True:
        linha = input()
        print("$" + linha)
        partes = linha.split()

        comando = partes[0]

        if comando == "end":
            return
        
        elif comando == "init":
            capacidade = int(partes[1])
            sala = Cinema(capacidade)

        elif comando == "reserve":
            ident = partes[1]
            telefone = int(partes[2])
            indice = int(partes[3])
            sala.reservar(ident, telefone, indice)

        elif comando == "cancel":
            id_cliente = partes[1]
            sala.cancelar(id_cliente)

        elif comando == "show":
            if sala is None:
                print("[]")
            else:
                print(sala)


if __name__ == "__main__":
    main()
