# Q2.py
import Q1

def main():
    while True:
        try:
            pass
        except:
            break

        for i in range(1, 100):
            key = Q1.real[i]
            j = i - 1
            while(key < Q1.real[j] and j >= 0):
                Q1.real[j+1] = Q1.real[j]
                j -= 1
            Q1.real[j+1] = key

        print(Q1.real)
        break

    return 0

main()