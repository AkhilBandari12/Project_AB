def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
s=[[1,2],[3,4]]
print("Flattened list is: ",flatten(s))