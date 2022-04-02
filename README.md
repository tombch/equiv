# `equiv`

A function for determining if two statements are logically equivalent.

## Usage

To compare two logical statements, first define them as functions that take their variables as input.

The variables of the two statements must match (or one is a subset of the other) in order to be compared. 

Then, pass them into the `equiv` function.

For example, to show that `s1 : ¬(p \/ q)` is logically equivalent to `s2 : ¬p /\ ¬q`:

```python
def s1(p, q):
    return not (p or q)

def s2(p, q):
    return (not p) and (not q)

print(equiv(s1, s2)) # True
```
