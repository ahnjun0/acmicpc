import sys
input = lambda: sys.stdin.readline()

ret = []
cnt = 0
for st in input():
    if st == 'X':
        cnt += 1
    
    else: # st == '.' or EOF or '\n'
        if cnt & 1 == 0:
            ret.extend(['AAAA'] * (cnt // 4))
            ret.extend(['BB'] * ((cnt % 4) // 2))
            if st == '.': ret.append('.')
            cnt = 0
        else:
            print(-1)
            sys.exit(0)

print(''.join(ret))