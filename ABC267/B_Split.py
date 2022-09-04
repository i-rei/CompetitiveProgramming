import re
s = list(input())
line = ['1'] * 7
if '1' not in s or s[1:].count('1') == 1:
    print('No')
    exit()
if s[0] == '0':
    if s[6] == '0':
        line[0] = '0'
    if s[3] == '0':
        line[1] = '0'
    if s[7] == s[1] == 0:
        line[2] = '0'
    if s[4] == '0':
        line[3] = '0'
    if s[8] == s[2] == '0':
        line[4] = '0'
    if s[5] == '0':
        line[5] = '0'
    if s[9] == '0':
        line[6] = '0'
    a = ''.join(line)
    s = re.search(r'1(.+)1', a).group(1)
    if '0' in s:
        print('Yes')
    else:
        print('No')
else:
    print('No')
