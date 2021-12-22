import re

with open('2021/data/day12.txt') as f:
    connections = [re.findall(r'\w+', line) for line in f.readlines()]

d = {}
for start, end in connections:
    
    if start in d.keys():
        d[start].append(end)
    else:
        d[start] = [end]

    if end in d.keys():
        d[end].append(start)
    else:
        d[end] = [start]

# part one
routes = [['start']]

while not all(['end' in x for x in routes]):

    tmp = []

    for route in routes:

        if 'end' in route:
            tmp.append(route)
        
        else:
            for next in d[route[-1]]:

                if next in d.keys():
                    tmp2 = route.copy()
                    
                    if next.isupper():
                        tmp2.append(next)
                        tmp.append(tmp2)

                    else:
                        if next not in route:
                            tmp2.append(next)
                            tmp.append(tmp2)

    routes = tmp.copy()

print(f"Paths through cave system passing small caves once: {len(routes)}")

# part two
routes = [['start']]

while not all(['end' in x for x in routes]):

    tmp = []

    for route in routes:

        if 'end' in route:
            tmp.append(route)
        
        else:
            for next in d[route[-1]]:

                if next in d.keys():
                    tmp2 = route.copy()
                    
                    if next.isupper():
                        tmp2.append(next)
                        tmp.append(tmp2)

                    elif next != "start":
                        if next not in route:
                            tmp2.append(next)
                            tmp.append(tmp2)

                        elif (
                            sorted(
                                {
                                    i:route.count(i) 
                                    for i in route if i.islower()
                                }.values()
                            )[-1] < 2
                        ):
                            tmp2.append(next)
                            tmp.append(tmp2)
                        

    routes = tmp.copy()

print(f"Paths through cave system passing one small cave twice: {len(routes)}")