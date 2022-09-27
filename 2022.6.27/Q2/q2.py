# real Q2
# This is Q2

def main():
    while True:
        try:
            a, b, c, d, e, f = map(int,input().split())
        except:
            break
              
        delta = a * e - b * d
        delta_x = c * e - b * f
        delta_y = a * f - c * d

        if delta == 0:
            if delta_x == 0 and delta_y == 0:
                print("Too many")
            else: 
                print("No answer")
        else:
            print("x={:.2f}".format(delta_x / delta))
            print("y={:.2f}".format(delta_y / delta))
    return 0
main()