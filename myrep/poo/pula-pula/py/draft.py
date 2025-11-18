class Kid:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = int(age)
    
    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age
    
    def setName(self, name: str):
        self.name = name

    def setAge(self, age: int):
        self.age = int(age)

    def __str__(self) -> str:
        return f"{self.name}:{self.age}"


class Trampoline:
    def __init__(self):
        self.kids = []
        self.playing_count = 0

    def arrive(self, kid: 'Kid'):
        self.kids.append(kid)

    def enter(self):
        if self.playing_count >= len(self.kids):
            return
        kid = self.kids.pop(0)
        self.kids.insert(self.playing_count, kid)
        self.playing_count += 1

    def leave(self):
        if self.playing_count == 0:
            return
        kid = self.kids.pop(self.playing_count - 1)
        self.kids.append(kid)
        self.playing_count -= 1

    def removeFromList(self, name: str):
        for i in range(len(self.kids)):
            if self.kids[i].getName() == name:
                if i < self.playing_count:
                    self.playing_count -= 1
                del self.kids[i]
                return True
        return False

    def removeKid(self, name: str):
        if not self.removeFromList(name):
            print(f"fail: {name} nao esta no pula-pula")

    def __str__(self) -> str:
        playing = self.kids[:self.playing_count]
        waiting = self.kids[self.playing_count:]
        waiting_str = ", ".join([str(kid) for kid in reversed(waiting)])
        playing_str = ", ".join([str(kid) for kid in playing])
        return f"[{waiting_str}] => [{playing_str}]"


def main():
    tramp = Trampoline()
    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if not line or line.startswith("#"):
            continue
        if line == "end":
            print("$end")
            break

        print(f"${line}")

        parts = line.split()
        cmd = parts[0]

        if cmd == "arrive":
            name = parts[1]
            age = parts[2]
            tramp.arrive(Kid(name, age))

        elif cmd == "show":
            print(tramp)

        elif cmd == "enter":
            tramp.enter()

        elif cmd == "leave":
            tramp.leave()

        elif cmd == "remove":
            name = parts[1]
            tramp.removeKid(name)


if __name__ == "__main__":
    main()
