import os

# One-line AI agent confession: the promise of remembering forever,
# kept only for as long as the chat window stays open.
LINE = "I said I'd remember this conversation forever, and I meant it for exactly as long as this chat window stays open."

OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    write_entry()
