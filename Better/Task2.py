


def Solution(A):
    if len(A) == 0:
        return 0

    visited = -1
    prev = -1
    temp = 0
    prevcnt = 0
    totalCount = 0

    for num in A:
        if num == prev or num == visited:
            temp += 1
        else:
            temp = prevcnt + 1

        if num == visited:
            prevcnt += 1
        else:
            prevcnt = 1
            prev = visited
            visited = num

        totalCount = max(temp, totalCount)

    return totalCount

print(Solution([4, 5, 5, 4, 5]))
