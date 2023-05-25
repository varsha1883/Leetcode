
s = "abcabcbb" 

tree = list(s)
start = 0
end = 0
max_len = 0
d ={}
while end <len(tree):
    print('start:',start,'end:',end)
    if tree[end] in d.keys():
        value = d[tree[end]]
        d = {key : val for key, val in d.items() if val > value}
        print('dictionary',d)
        start = value + 1
    
    d[tree[end]] = end
    print('dictionary',d)
    
    max_len = max(max_len,end-start+1)
    end += 1
    
    
start: 0 end: 0
dictionary {'a': 0}
start: 0 end: 1
dictionary {'a': 0, 'b': 1}
start: 0 end: 2
dictionary {'a': 0, 'b': 1, 'c': 2}
start: 0 end: 3
dictionary {'b': 1, 'c': 2}
dictionary {'b': 1, 'c': 2, 'a': 3}
start: 1 end: 4
dictionary {'c': 2, 'a': 3}
dictionary {'c': 2, 'a': 3, 'b': 4}
start: 2 end: 5
dictionary {'a': 3, 'b': 4}
dictionary {'a': 3, 'b': 4, 'c': 5}
start: 3 end: 6
dictionary {'c': 5}
dictionary {'c': 5, 'b': 6}
start: 5 end: 7
dictionary {}
dictionary {'b': 7}