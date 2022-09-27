# 只有兩層if else的Q1
# This is final Q1
def main():
    while True:
        try:
            year = int(input())
        except:
            break

        if year % 4 == 0:
            if year % 400 == 0:
                print("閏年")
            elif year % 100 == 0:
                print("平年")
            else:
                 print("閏年")
        else:
            print("平年")

main()