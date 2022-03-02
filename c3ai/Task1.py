compressed = "A[2[3[B]C]"
# "ABBBCBBBC"
count = []
aplhas = []
out = ""
end = 0
temp = ""
open = 0
while end < len(compressed)-1:
    if compressed[end] == "[":
        if compressed[end+1].isalpha():
            aplhas.append(compressed[end+1])

        if compressed[end+1].isdigit():
            count.append(int(compressed[end+1]))
        end += 1
    elif compressed[end] == "]":
        open -= 1
        # print(count[-1], aplhas[-1])
        temp = aplhas.pop()*count.pop()
        aplhas.append(temp)
        end += 1
        # aplhas[-1] = aplhas[-1]*count.pop()
    else:
        if len(count)>0 and len(aplhas)>0:
            temp = (aplhas.pop()+compressed[end])*count.pop()
            aplhas.append(temp)
    print(aplhas, count)
        # out += compressed[end]
    end += 1
# print(count, aplhas)
