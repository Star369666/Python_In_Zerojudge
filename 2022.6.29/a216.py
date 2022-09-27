def f_function(n):
    if n == 1:
        return 1
    else:
        return int(n * (n + 1) / 2)

def g_function(n):
    if n == 1:
        result = 1
    elif n == 2:
        result = f_function(n) + 1
    else:
        result = f_function(2) + 1
        times = n + 1
        for i in range(3, times):
            result = f_function(i) + result
    return int(result)

def main():
    while True:
        try:
            n = int(input())
        except:
            break
        print(f_function(n), g_function(n))
    return 0
main()