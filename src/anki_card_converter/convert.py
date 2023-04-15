import click
from pathlib import Path

from anki_card_converter.cards import AllInOneCard, BasicCard


@click.command()
@click.option(
    "-i",
    "--input-path",
    default="data/in.txt",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
@click.option(
    "-o",
    "--output-path",
    default="data/out.txt",
    type=click.Path(dir_okay=False, path_type=Path),
)
def convert(input_path: Path, output_path: Path) -> None:
    cards = load_cards(input_path)
    with open(output_path, "w") as f:
        f.write("#separator:tab\n")
        f.write("#html:true\n")
        f.write("#guid column:1\n")
        f.write("#notetype column:2\n")
        f.write("#deck column:3\n")
        f.write("#tags column:17\n")
        for card in cards:
            f.write(f"{AllInOneCard.from_basic(card, 7)}\n")


def load_cards(filename):
    with open(filename, "r") as f:
        return [
            BasicCard.parse(line) for line in f if not line.startswith("#")
        ]
