import inspect, itertools


def equiv(f, g):
    # Sets of input arguments for the two functions
    f_args = set(inspect.signature(f).parameters)
    g_args = set(inspect.signature(g).parameters)

    # Must be able to match arguments between the functions
    if not (f_args.issubset(g_args) or g_args.issubset(f_args)):
        raise Exception('One of the function\'s input variables must be (at least) a subset of the other function\'s input variables')
    
    # All arguments of both functions are contained in the largest set
    args = f_args if len(f_args) >= len(g_args) else g_args

    # Generate all combinations of True/False
    combinations = list(itertools.product([True,False], repeat=len(args)))
    
    # For every combination of True/False values
    # Create two dictionaries, that will be passed as keyword arguments to their corresponding function
    truth_table = [
        (
            {arg : val for arg, val in zip(args, truth_values) if arg in f_args}, 
            {arg : val for arg, val in zip(args, truth_values) if arg in g_args}
        ) for truth_values in combinations
    ]

    # If the logical formulas are equivalent 
    # Then every combination of truth values should produce the same output
    return all([f(**f_a) == g(**g_a) for f_a, g_a in truth_table])


# Examples

def s1(p, q):
    return not (p or q)

def s2(p, q):
    return (not p) and (not q)

print(equiv(s1, s2)) # True


def p_(p):
    return p

def id1(p):
    return p and True

def id2(p):
    return p or False

print(equiv(p_, id1)) # True
print(equiv(p_, id2)) # True


# These formulas are logically equivalent
def f1(p, q, r):
    return (not p and not q and not r) or (not p and not q and r) or (p and q and not r ) or (p and q and r)

def f2(p, q):
    return (not p and not q) or (p and q)

print(equiv(f1, f2)) # True


def implies1(p, q):
    return (not p) or q

def implies2(p, q):
    return (p and q) or (not p)

print(equiv(implies1, implies2)) # True


def tautology1(p):
    return p or not p

def tautology2(p, q):
    return (p or not p) and (q or not q)

def contradiction1(p):
    return not p and p

def contradiction2(p, q):
    return not ((not (not p and p)) or (not (not q and q)))

print(equiv(tautology1, tautology2)) # True
print(equiv(contradiction1, contradiction2)) # True
print(equiv(tautology1, contradiction1)) # False
