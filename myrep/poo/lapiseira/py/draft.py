class Grafite:
    def __init__(self, calibre, dureza, tamanho):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def __str__(self):
        return f"{self.calibre}:{self.dureza}:{self.tamanho}"


class Lapiseira:
    def __init__(self):
        self.calibre = None
        self.bico = None
        self.tambor = []

    def init(self, calibre):
        self.calibre = calibre
        self.bico = None
        self.tambor = []

    def insert(self, calibre, dureza, tamanho):
        if round(calibre, 1) != round(self.calibre, 1):
            print("fail: calibre incompatível")
            return
        self.tambor.append(Grafite(calibre, dureza, tamanho))

    def pull(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        if len(self.tambor) == 0:
            return
        self.bico = self.tambor.pop(0)

    def remove(self):
        self.bico = None

    def write(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return

        consumo_por_dureza = {
            "HB": 1,
            "2B": 2,
            "4B": 4,
            "6B": 6
        }

        if self.bico.dureza not in consumo_por_dureza:
            print("fail: dureza desconhecida")
            return

        consumo = consumo_por_dureza[self.bico.dureza]

        if self.bico.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return

        if self.bico.tamanho - consumo >= 10:
            self.bico.tamanho -= consumo
        else:
            self.bico.tamanho = 10
            print("fail: folha incompleta")

    def show(self):
        calibre_str = f"{self.calibre:.1f}" if self.calibre is not None else "None"

        bico_str = "[]" if self.bico is None else f"[{self.bico}]"

        if len(self.tambor) == 0:
            tambor_str = "<>"
        else:
            inner = "".join(f"[{g}]" for g in self.tambor)
            tambor_str = f"<{inner}>"

        print(f"calibre: {calibre_str}, bico: {bico_str}, tambor: {tambor_str}")


def main():
    lap = Lapiseira()

    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if line == "":
            continue

        print(f"${line}")
        parts = line.split()

        cmd = parts[0]

        if cmd == "end":
            break

        elif cmd == "init":
            lap.init(float(parts[1]))

        elif cmd == "insert":
            lap.insert(float(parts[1]), parts[2], int(parts[3]))

        elif cmd == "pull":
            lap.pull()

        elif cmd == "remove":
            lap.remove()

        elif cmd == "write":
            lap.write()

        elif cmd == "show":
            lap.show()   

if __name__ == "__main__":
    main()
