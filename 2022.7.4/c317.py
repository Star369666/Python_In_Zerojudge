# Q2
def main():
    while True:
        try:
            n = int(input())
            num = []
            for i in range(n):
                num.append(list(map(int, input().split())))
                if num[i][1] < num[i][2]:
                    num[i][1], num[i][2] = num[i][2], num[i][1]
                num[i].append(num[i][0] // num[i][1])
        except:
            break

        # num[i] = [x, a, b, x//a]
        
        for i in range(n):
            is_can = False
            for j in range(num[i][3], -1, -1):
                if (num[i][0] - num[i][1] * j) % num[i][2] == 0:
                    print(j + (num[i][0] - num[i][1] * j) // num[i][2])
                    is_can = True
                    break
            if is_can == False:
                print(-1)

    return 0

main()