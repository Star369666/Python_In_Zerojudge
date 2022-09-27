def whirl(toWhirl: list, row, col):
    current = []
    back = []
    for i in range(col):
        for j in range(row):
            current.append(toWhirl[j][col - 1 - i])
        back.append(current)
        current = []
    return back

def main():
    while True:
        try:
            R, C, M = map(int, input().split())
            matrix = []
            i = 0
            for i in range(R):
                matrix.append(list(map(int, input().split())))
            m = list(map(int, input().split()))
        except:
            break

        m.reverse()
        count = 0
        while(count < M):
            if m[count] == 0:
                matrix = whirl(matrix, R, C)
                temp = R
                R = C
                C = temp
            else:
                matrix.reverse()
            count += 1
        
        print(f"{R} {C}")
        for i in range(R):
            for j in range(C):
                print(f"{matrix[i][j]} ", end="")
            print("")
        break
    return 0
main()