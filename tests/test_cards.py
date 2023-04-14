from anki_card_converter.cards import AllInOneCard, BasicCard


def test_basic_card_parses_input_correctly() -> None:
    card = BasicCard.parse(
        "O[E~`[J-pF	Basic	test	Question on the front side.	"
        "Answer on the back side.	"
    )
    assert card.uid == "O[E~`[J-pF"
    assert card.type == "Basic"
    assert card.deck == "test"
    assert card.front == "Question on the front side."
    assert card.back == "Answer on the back side."


def test_allinone_card_converts_basic_card_correctly() -> None:
    basic_card = BasicCard.parse(
        "O[E~`[J-pF	Basic	test	Question on the front side<br><br>[ ] "
        "variant 1<br>[ ] variant 2<br>[ ] variant 3<br>[ ] variant 4	[ ] "
        "variant 1<br>[ ] variant 2<br>[x] variant 3<br>[ ] variant 4<br><br>"
        "Explanation...	"
    )
    allinone_card = AllInOneCard.from_basic(basic_card)

    assert allinone_card.uid == "O[E~`[J-pF"
    assert allinone_card.type == "AllInOne (kprim, mc, sc)"
    assert allinone_card.deck == "test"
    assert allinone_card.question == "Question on the front side"
    assert allinone_card.title == ""
    assert allinone_card.qtype == 2
    assert allinone_card.answers == [
        "variant 1", "variant 2", "variant 3", "variant 4", ""
    ]
    assert allinone_card.correct_answers == "0 0 1 0"
    assert allinone_card.sources == ""
    assert allinone_card.extra == (
        "[ ] variant 1<br>[ ] variant 2<br>[x] variant 3<br>[ ] variant 4"
        "<br><br>Explanation..."
    )
