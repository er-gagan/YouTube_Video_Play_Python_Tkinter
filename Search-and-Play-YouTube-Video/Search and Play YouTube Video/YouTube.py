ts = '3:03'
secs = sum(int(x) * 60 ** i for i, x in enumerate(reversed(ts.split(':'))))
print(secs)