import sys
from collections import defaultdict
input = lambda: map(int, sys.stdin.readline().rstrip().split())

N, M, Q = input()
hidden_layer = [[*input()] for _ in range(M)]
output_layer = [*input()]

NP = [0] * N
output_bias = output_layer[-1]

for i in range(M):
    output_bias += hidden_layer[i][-1] * output_layer[i]
    for j in range(1, hidden_layer[i][0] + 1):
        NP[hidden_layer[i][j]-1] += hidden_layer[i][j + hidden_layer[i][0]] * output_layer[i]


for _ in range(Q):
    output = output_bias
    testcase = [*input()]
    
    for i, val in enumerate(testcase):
        output += val * NP[i]
    print(output)