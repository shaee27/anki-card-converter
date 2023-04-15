import re
from typing import List, Optional


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


class AllInOneCard:
    def __init__(
        self,
        uid: str = "",
        deck: str = "",
        question: str = "",
        title: str = "",
        qtype: int = 2,
        answers: Optional[List[str]] = None,
        answers_len: int = 5,
        correct_answers: str = "",
        sources: str = "",
        extra: str = "",
    ):
        self.uid = uid
        self.type = "AllInOne (kprim, mc, sc)"
        self.deck = deck
        self.question = question
        self.title = title
        self.qtype = qtype
        if answers is None:
            answers = []
        self.answers = self.fill_blank_answers(answers, answers_len)
        self.correct_answers = correct_answers
        self.sources = sources
        self.extra = extra

    @staticmethod
    def from_basic(card: BasicCard, answers_len: int = 5):
        answers = [0 + (a == "x") for a in re.findall(r"\[(x| )]", card.back)]
        return AllInOneCard(
            uid=card.uid,
            deck=card.deck,
            question=re.split(r"(?:<br>)*?\[(?:x| )] ", card.front)[0],
            answers=re.split(r"(?:<br>)*?\[(?:x| )] ", card.front)[1:],
            answers_len=answers_len,
            correct_answers=" ".join(map(str, answers)),
            extra=card.back.strip().replace("\n", "<br>"),
        )

    @staticmethod
    def fill_blank_answers(answers: List[str], answers_len: int) -> List[str]:
        diff = answers_len - len(answers)
        if diff < 0:
            raise ValueError(
                "Answers length exceeds specivied "
                f"({len(answers)} > {answers_len})"
            )
        for _ in range(diff):
            answers.append("")
        return answers

    def __str__(self):
        answers = '"\t"'.join(self.answers)
        return "\t".join(
            [
                self.uid,
                self.type,
                self.deck,
                f'"{self.question}"',
                f'"{self.title}"',
                str(self.qtype),
                f'"{answers}"',
                f'"{self.correct_answers}"',
                f'"{self.sources}"',
                f'"{self.extra}"',
            ]
        )
