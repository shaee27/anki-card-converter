from anki_card_converter.cards import BasicCard


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
