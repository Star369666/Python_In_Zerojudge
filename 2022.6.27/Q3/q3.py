# This is Q3
def main():
   while True:
      try:
         count = 0
         first = int(input())
         while first == 0:
            first = int(input())
         input_num = [first]
         while input_num[count] != -1:
            input_num.append(int(input()))
            count += 1
      except:
         break
    
      for i in range(0, len(input_num) - 1, 1):
         j = 2
         is_begin = 1
         while j <= input_num[i]:
            count = 0
            while input_num[i] % j == 0:
               count += 1
               input_num[i] /= j
            if count >= 1:
                if is_begin == 1:
                   if count > 1:
                       print(f"{j}^{count} ")
                       is_begin = 0
                   else:
                       print(f"{j} ")
                       is_begin = 0
                else:
                   if count > 1:
                       print(f"* {j}^{count} ")
                   else:
                       print(f"* {j} ")
            j += 1
      print("")
      return 0
main()