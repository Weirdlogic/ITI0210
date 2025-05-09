# Forward Chaining Algorithm for Horn Clauses

## Introduction

This Python script implements a Forward Chaining algorithm for Horn clauses in propositional logic. The algorithm infers new facts based on given rules and attempts to prove a query by deriving it from the knowledge base.

## Input Format

* Clauses are represented as tuples of the form `([premises], conclusion)`, where:

  * `premises` is a list of symbols that must be true for the conclusion to be inferred.
  * `conclusion` is the symbol inferred if all premises are true.
* Facts are represented as `([], "Fact")`, meaning they are always true.

### Example:

```
clauses = [
    ([], "A"),
    ([], "B"),
    (["A", "P"], "L"),
    (["A", "B"], "L"),
    (["B", "L"], "M"),
    (["L", "M"], "P"),
    (["P"], "Q")
]
```

## Algorithm Explanation

1. Initialize an empty set for inferred symbols.
2. Loop through the clauses, and for each clause:

   * If all premises are inferred and the conclusion is not yet inferred, infer the conclusion.
   * If the conclusion matches the query, return `True`.
3. If no new conclusions can be drawn and the query is not proven, return `False`.

## Test Results

### Propositional Logic Problem

* Query: "Q"
* Result: `True` (Q is entailed)

### Egg Problem

* Query: "Breaks" → `True`
* Query: "MakesMess" → `True`
* Query: "Smells" → `False` (not inferred because "Spoiled" is not a fact)
