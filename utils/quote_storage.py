import json

def load_quotes(filename="quotes.json"):
    # Load all the quotes in the json
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_quotes(quotes, filename="quotes.json"):
    # Write the quote to the json
    with open(filename, "w") as f:
        json.dump(quotes, f, indent=2)

def get_next_id(quotes):
    # Generates next id to assign to a new quote
    if not quotes:
        return 1
    return max(q["id"] for q in quotes) + 1
