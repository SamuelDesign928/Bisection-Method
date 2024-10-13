def find_square_root(target, tolerance=1e-7, max_iter=100):
    if target < 0:
        raise ValueError("Cannot compute square root of a negative number in real numbers.")
    elif target in [0, 1]:
        print(f'The square root of {target} is {target}')
        return target
    
    lower_bound, upper_bound = 0, max(1, target)
    estimate = None

    for iteration in range(max_iter):
        midpoint = (lower_bound + upper_bound) / 2
        squared_value = midpoint * midpoint

        if abs(squared_value - target) <= tolerance:
            estimate = midpoint
            break

        if squared_value < target:
            lower_bound = midpoint
        else:
            upper_bound = midpoint

    if estimate is not None:
        print(f'The square root of {target} is approximately {estimate}')
    else:
        print(f'Unable to find square root within {max_iter} iterations.')

    return estimate
