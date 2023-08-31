# Tuples

Similar to the list but different intention.
- Lists are used for many similar items
- Tuples are used for items with many attributes

Example: Address consists of zip code, city, street, house number.

```
address = (52066, "Aachen", "Eupener Str. 70", "0241-6009-12345")
```

Syntax
- Similar to lists but with parentheses ()

Semantics
- Tuples are immutable. i.e. you cannot change a value of the tuple

## Basic Operaions

Tuples have an index like lists
- Actually, square brackets [] are used for indexing tuples!

Sub-tuples can be defined with slicing

Combination of list of tuples leads to a powerful structure

## What are tuples used for?

Tuples are quite similar to lists.

The following rule of thumb can be used to determine when to use lists and when to use tuples

- Lists are used for many similar items.
- Tuples are used for items with many attributes

Consider the following data as suitable examples of tuples
```
address = (zip code, city, street, house number)
position = (x_coordinates, y_coordinates)
date = (year, month, date)
```