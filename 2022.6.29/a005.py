# Q1
def main():
    while True:
        try:
            t = int(input())
            array = []
            for i in range(t):
                current = list(map(int, input().split()))
                current.sort()
                array.append(current)
                current = []
        except:
            break
        
        fifth_array = []
        for i in range(t):
            if array[i][1] - array[i][0] == array[i][2] - array[i][1]:
                d = array[i][1] - array[i][0]
                fifth = array[i][3] + d
            else:
                if array[i][0] == 0:
                    fifth = 0
                else:
                    r = array[i][1] / array[i][0]
                    fifth = int(array[i][3] * r)
            fifth_array.append(fifth)
        final = []
        current = [[]]
        for i in range(t):
            for j in range(4):
                print(f"{array[i][j]} ", end="")
            print(fifth_array[i])

    return 0

main()