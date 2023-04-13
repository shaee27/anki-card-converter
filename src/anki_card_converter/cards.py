class BasicCard:
    def __init__(self, uid: str, deck: str, front: str, back: str):
        self.uid = uid
        self.type = "Basic"
        self.deck = deck
        self.front = front
        self.back = back

    @staticmethod
    def parse(s: str) -> "BasicCard":
        uid, ctype, deck, front, back = s.strip().split("\t")
        if front.startswith('"'):
            front = front[1:-1].strip()
        if back.startswith('"'):
            back = back[1:-1].strip()
        return BasicCard(uid, deck, front, back)
