def display_array():
    n = int(input("Enter the number of elements of array: "))
    a = []

    for i in range(n):
        a = a + [float(input("a[%d] = " %i))]
    pattern_set = set()
    result = []

    for i in a:
        if i not in pattern_set:
            result.append(str(int(i)))
            pattern_set.add(int(i))

    last_result = " ".join(result)
    print(last_result)
new_array=display_array()