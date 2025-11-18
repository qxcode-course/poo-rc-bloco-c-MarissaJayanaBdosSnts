CONSUMO = {
    "HB": 1,
    "2B": 2,
    "4B": 4,
    "6B": 6
}

def fmt(n):
    return "{:.1f}".format(n)

def gstr(g):
    return "{}:{}:{}".format(fmt(g[0]), g[1], g[2])

def show(calibre, bico, tambor):
    if bico is None:
        b = "[]"
    else:
        b = "[" + gstr(bico) + "]"

    if len(tambor) == 0:
        t = "<>"
    else:
        t = "<" + "".join("[" + gstr(g) + "]" for g in tambor) + ">"

    print(f"calibre: {fmt(calibre)}, bico: {b}, tambor: {t}")

def main():
    calibre = None
    bico = None
    tambor = []

    while True:
        try:
            line = input().strip()
        except:
            break

        if line == "":
            continue

        print("$" + line)

        p = line.split()
        cmd = p[0].strip()     # <<<<<< AQUI A CORREÇÃO

        if cmd == "end":
            break

        if cmd == "init":
            calibre = float(p[1])
            bico = None
            tambor = []
            continue

        if cmd == "show":
            show(calibre, bico, tambor)
            continue

        if cmd == "insert":
            c = float(p[1])
            d = p[2]
            t = int(p[3])

            if abs(c - calibre) > 1e-9:
                print("fail: calibre incompatível")
            else:
                tambor.append((c, d, t))
            continue

        if cmd == "pull":
            if bico is not None:
                print("fail: ja existe grafite no bico")
            else:
                if len(tambor) > 0:
                    bico = tambor.pop(0)
            continue

        if cmd == "remove":
            bico = None
            continue

        if cmd == "write":
            if bico is None:
                print("fail: nao existe grafite no bico")
                continue

            cal, dur, tam = bico
            cons = CONSUMO[dur]

            if tam <= 10:
                print("fail: tamanho insuficiente")
                continue

            if tam - cons < 10:
                bico = (cal, dur, 10)
                print("fail: folha incompleta")
                continue

            bico = (cal, dur, tam - cons)
            continue

main()
