def find_a_b(numbers, c):
    output = ""
    for i in range(len(numbers)):  # use index
        for j in range(len(numbers)):
            if i == j:
                continue
            if numbers[i] * numbers[j] == c:
                output = [numbers[i], numbers[j]]
            if output:
                return sorted(output)
    return None

print(find_a_b([0,0,2,2],4))

# failed twice: compared items directly without None, compared items directly
