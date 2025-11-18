class Pessoa:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Mercado:
    def __init__(self, counter_count: int):
        self.counters = [None] * counter_count
        self.queue = []

    def __str__(self):
        caixas = ", ".join(str(p) if p else "-----" for p in self.counters)
        espera = ", ".join(str(p) for p in self.queue)
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"

    def arrive(self, p: Pessoa):
        self.queue.append(p)

    def call(self, idx: int):
        if idx < 0 or idx >= len(self.counters):
            print("fail: caixa inexistente")
            return
        if self.counters[idx] is not None:
            print("fail: caixa ocupado")
            return
        if not self.queue:
            print("fail: sem clientes")
            return
        self.counters[idx] = self.queue.pop(0)

    def finish(self, idx: int):
        if idx < 0 or idx >= len(self.counters):
            print("fail: caixa inexistente")
            return
        if self.counters[idx] is None:
            print("fail: caixa vazio")
            return
        self.counters[idx] = None


def main():

    mercado = None

    while True:
        try:
            line = input()
        except EOFError:
            break

        line = line.rstrip("\n")

        if not line:
            continue

        print("$" + line)

        parts = line.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "end":
            break
        elif cmd == "init":
            mercado = Mercado(int(args[0]))
        elif cmd == "show":
            print(mercado)
        elif cmd == "arrive":
            mercado.arrive(Pessoa(args[0]))
        elif cmd == "call":
            mercado.call(int(args[0]))
        elif cmd == "finish":
            mercado.finish(int(args[0]))


main()
