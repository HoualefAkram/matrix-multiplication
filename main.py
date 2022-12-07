def multiply(m1, m2):
    lin = len(m1)
    col = len(m2[0])

    multiplied = []
    for _ in range(lin):  # making empty matrix
        multiplied_lines = []
        for _ in range(col):
            multiplied_lines.append(0)
        multiplied.append(multiplied_lines)

    for J in range(len(m1)):  # lines of matrix 1 (slow)
        for I in range(len(m2[0])):  # columns of matrix 2 (fast)
            for v in range(len(m2)):  # counter
                multiplied[J][I] += m1[J][v] * m2[v][I]

    return multiplied
