class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
    
f = Fib()
print(f[12])


def str2num(number):
     try:
         return int(number)
     except:
         return float(number)

print(str2num("7.6"))



