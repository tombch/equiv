import inspect, itertools


def equiv(*statements):
    # Sets of input variables for each statement
    all_statement_vars = []
    for statement in statements:
        all_statement_vars.append(set(inspect.signature(statement).parameters))

    # Single set containing all input variables across all statements
    vars_union = set.union(*all_statement_vars)
    
    # Generate all combinations of True/False for the given number of variables
    truth_combinations = list(itertools.product([True,False], repeat=len(vars_union)))
    
    # For every combination of True/False values, create (for each statement) a dictionary of keyword arguments
    truth_table = [
        [
            {variable : truth_value for variable, truth_value in zip(vars_union, truth_combination) if variable in statement_vars}
            for statement_vars in all_statement_vars
        ] for truth_combination in truth_combinations
    ]

    # If the logical statements are all equivalent, then every combination of truth values should produce the same output for each statement
    # For a given combination of truth values, this is equivalent to the set of evaluated statements being of size 1 (as they all share the same output value)
    return all([len({statement(**statement_kwargs) for statement, statement_kwargs in zip(statements, statements_kwargs)}) == 1 for statements_kwargs in truth_table])
