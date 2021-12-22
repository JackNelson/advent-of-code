from bidict import bidict
import re
import statistics

syntax_map = bidict({
    '(':')',
    '<':'>',
    '[':']',
    '{':'}',
})

def test_syntax(line):

    global syntax_map

    scores = {
        '':0,
        ')':3,
        ']':57,
        '}':1197,
        '>':25137,
    }

    tmp = ''
    res = ''

    for char in line:
        
        if char in syntax_map.keys():
            tmp += char
        
        elif (len(tmp) > 0) and (tmp[-1] == syntax_map.inverse[char]):
            tmp = tmp[:-1]

        else:
            res = char
            break

    return (tmp, res, scores[res])

def score_incomplete(string):

    global syntax_map

    scores = {
        ')':1,
        ']':2,
        '}':3,
        '>':4,
    }

    tmp = ''
    res = 0

    for char in string[::-1]:
        tmp += syntax_map[char]

    for char in tmp:
        res *= 5
        res += scores[char]

    return res

with open('2021/data/day10.txt') as f:
    
    lines = [''.join(re.findall(r'.', line)) for line in f.readlines()]

results = [test_syntax(line) for line in lines]

# part 1
ans = [res[2] for res in results if res[2] != 0]
print(f"Total Error Found: {len(ans)}, Error Score: {sum(ans)}")

# part 2
ans = [score_incomplete(res[0]) for res in results if res[2] == 0]
print(f"Median Syntax Completion Score: {statistics.median(ans)}")
