def process_numbers(numbers):
    result = []

    for x in numbers:
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            return result
        if x > 5:
            result.append(x * 2)

    return result
