def forward_chaining(clauses, query):
    inferred = set()
    new_symbols = True  # Loop while new symbols are inferred

    while new_symbols:
        new_symbols = False
        for premises, conclusion in clauses:
            # Check if all premises are inferred
            if all(premise in inferred for premise in premises) and conclusion not in inferred:
                inferred.add(conclusion)
                print(f"Inferred: {conclusion}")
                if conclusion == query:
                    return True
                new_symbols = True
    return False


# Test Problem
clauses = [
    ([], "A"),
    ([], "B"),
    (["A", "P"], "L"),
    (["A", "B"], "L"),
    (["B", "L"], "M"),
    (["L", "M"], "P"),
    (["P"], "Q")
]

query = "Q"

print("Is Q entailed?", forward_chaining(clauses, query))

# Egg Problem
egg_clauses = [
    ([], "Fragile"),
    ([], "Falls"),
    ([], "ContainsLiquid"),
    (["Fragile", "Falls"], "Breaks"),
    (["Breaks", "ContainsLiquid"], "MakesMess"),
    (["Spoiled", "Breaks"], "Smells")
]

queries = ["Breaks", "MakesMess", "Smells"]

for q in queries:
    print(f"Does the egg {q}?", forward_chaining(egg_clauses, q))
