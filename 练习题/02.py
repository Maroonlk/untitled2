a = (i for i in range(1,10000000) if i%3==0 or i%5==0)

b = []
while True:
    for i in range(1, 10000):
        if i%3==0 or i%5==0:
            b.append(i)
