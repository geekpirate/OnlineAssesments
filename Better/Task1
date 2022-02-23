def Solution(S, K):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    currDay = days.index(S)

    for i in range(K):
        currDay = (currDay+1) % 7

    return days[currDay]
