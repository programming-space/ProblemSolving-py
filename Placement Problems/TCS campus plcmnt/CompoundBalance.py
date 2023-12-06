def add_to_single_digit(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    return sum

def find_x_y(target, ascii_list_1, ascii_list_2):
    x_arr=[]
    y_arr=[]
    for x in range(0, target + 1):
        for y in range(0, target + 1):
            if ascii_list_1 * x + ascii_list_2 * y == target:
                x_arr.append(x)
                y_arr.append(y)
    return x_arr, y_arr
            
def main():
    txt = input()
    target = int(input())
    txt_list = list(txt)
    ascii_list = [ord(i) for i in txt_list]
    ascii_list_1 = ascii_list[0]
    ascii_list_2 = ascii_list[1]
    while ascii_list_1 > 9:
        ascii_list_1 = add_to_single_digit(ascii_list_1)
    while ascii_list_2 > 9:
        ascii_list_2 = add_to_single_digit(ascii_list_2)
    x, y = find_x_y(target, ascii_list_1, ascii_list_2)
    if len(x) == 0 or len(y) == 0:
        print("Not Possible")
    else:
        for i in range(len(x)-1,0,-1):
            if x[i] == 0 or y[i] == 0:
                pass
            else:
                print(txt_list[0],end="")
                print(x[i],end=" ")
                print(txt_list[1],end="")
                print(y[i],end=" \n")
        print(txt_list[0],end="")
        print(x[0],end=" ")
        print(txt_list[1],end="")
        print(y[0])

if __name__ == '__main__':
    main()