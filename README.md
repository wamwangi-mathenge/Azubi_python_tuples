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

## Slicing operator and functions & methods

The slicing operator also works with tuples to create a sub-tuple

Just as with lists, indices can be used to access not only a single element of the tuple but also the entire range. There are functions and methods that also work for tuples. Some examples include:
```
len(tuple) => Number of elements in a tuple

tuple.count(x) => Number of elements in the tuple with the value of x

tuple.index(x) => Index of the first element with the value of x. If it does not exist, an error will be shown
```

## Looping through tuples

Similar to lists, a `for` loop can be used to access individual elements in a tuple

```
address = (52066, "Aachen", "Euperor Str. 70", "0241-4009-12345")

for address_part in address:
    print(address_part)
```