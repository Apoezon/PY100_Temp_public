import pprint
# TODO решить с помощью list comprehension и распечатать его

tmp = []

[tmp.append({'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}) for i in range(16)]
pprint.pprint(tmp)
