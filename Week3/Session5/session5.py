import math

def main():
    x = 0.0
    print("-----------------------------")
    print("|             |             |")
    print("|      x      |    sin(x)   |")
    print("|             |             |")
    print("-----------------------------")
    while(x <= (2 * math.pi)):
        print("| %-11.9f | %-11.9f |" % (x, math.sin(x)))
        print("-----------------------------")
        x += (2 * math.pi / 1000)
    
if __name__ == '__main__':
    main()


"""
-----------------------------
|             |             |
-----------------------------
for x in range(0, 2 * math.pi, (2 * math.pi) / 1000):
for 0, (2 * pi) in enumerate((2 * math.pi) / 1000):
"""