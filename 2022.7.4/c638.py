# Q1
def main():
    while True:
        try:
            year = int(input())
        except:
            break
        
        sky_list = {"1":"甲", "2":"乙", "3":"丙", "4":"丁", "5":"戊", "6":"己", "7":"庚", "8":"辛", "9":"壬"}
        ground_list = {"1":"子", "2":"丑", "3":"寅", "4":"卯", "5":"辰", "6":"巳", "7":"午", "8":"未", "9":"申", "10":"酉", "11":"戌"}

        sky = year % 10 - 3
        ground = year % 12 - 3
        
        if sky > 0 and sky + 3 != 3:
            print(sky_list[str(sky)], end="")
        elif sky < 0:
            print(sky_list[str(sky + 10)], end="")
        else:
            print("癸", end="")
        
        if ground > 0 and ground + 3 != 3:
            print(ground_list[str(ground)])
        elif ground < 0:
            print(ground_list[str(ground + 12)])
        else:
            print("亥")
        
        print("")

    return 0

main()