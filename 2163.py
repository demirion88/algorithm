A, B = map(int, input().split())

ctmin = min(A, B)
ctmax = max(A, B)

print((ctmin-1) + (ctmax-1)*ctmin)

