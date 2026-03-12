s = 'Move#Hash#to#Front'

count = s.count('#')
s = s.replace('#','')

result = '#' * count + s
print(result)