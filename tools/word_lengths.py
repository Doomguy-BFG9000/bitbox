# tool: word_lengths
# description: Length of each word in a string
# author: @ShauryaPrakashVerma
# example: word_lengths "hi there" -> "2,5"

def run(text: str = None) -> str:
    """Return the length of each word as a comma-separated string."""
    if text is None:
        return "Error: requires a string argument"

    if not isinstance(text, str):
        return "Error: argument must be a string"

    if not text.strip():
        return "0"

    return ",".join(str(len(word)) for word in text.split())