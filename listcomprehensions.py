X = int(input()) #Take input from user (X)
Y = int(input())
Z = int(input())
N = int(input())
lis = [[x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x + y + z != N]
print lis
