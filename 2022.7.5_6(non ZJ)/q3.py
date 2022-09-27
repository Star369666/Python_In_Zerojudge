# Q3
import Q1

def min_index(sort: list, start, end):
    index = start
    for i in range(start, end):
        if sort[index] > sort[i]:
            index = i
    return index

def main():
    while True:
        try:
            pass
        except:
            break

        end = len(Q1.real)
        for i in range(end):
            start = i
            index = max_index(Q1.real, start, end)
            if Q1.real[index] != Q1.real[i]:
                Q1.real[index], Q1.real[i] = Q1.real[i], Q1.real[index]
        print(Q1.real)
        break

    return 0

main()