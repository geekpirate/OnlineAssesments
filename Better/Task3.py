def Solution(N):
    # out = []
    S = str(N)
    out = float("-inf")
    for index, s in enumerate(S):
        if s == '5':
            num = int(S[:index]+S[index+1:])
            out = max(num, out)
            # out.append(int(S[:index]+S[index+1:]))
        # print(out)
    return out

print(Solution(-5859))
