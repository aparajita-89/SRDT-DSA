arr = list(map(int, input().split()))

freq = {}

for i in arr:
    freq[i] = freq.get(i,0)+1

for k,v in freq.items():
    print(k,"occurs",v,"times")