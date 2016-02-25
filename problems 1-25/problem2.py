__author__ = 'matthew'

def fib(x):
   runningSum = 0
   a = 0
   b = 1
   for x in range(x):
       c = a + b
       if c % 2 == 0:
          runningSum += c
       a = b
       b = c
       print(b)
   print(runningSum)


fib(34)

