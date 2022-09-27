def main():
    while True:
        try:
            n = int(input())
            x_location = []
            y_location = []
            for i in range(n):
                x, y = map(int, input().split())
                x_location.append(x)
                y_location.append(y)
        except:
            break
            
        x_location.sort()
        y_location.sort()
        blob = 0
        start = -1
        end = -1

        for i in range(n):
            if x_location[i] > end:
                blob += end - start
                start = x_location[i]
                end = y_location[i]
            else:
                if y_location[i] > end:
                    end = y_location[i]
        blob += end - start
        print(blob)

    return 0

main()