string_numbers = input()
list_num = string_numbers.split(" ")

smaller = list_num[0]
smaller_position = 0

for number in list_num:
    if number < smaller:
        smaller = number
        smaller_position = list_num.index(number)

print(f"Um menor elemento vale {smaller} e está na posição {smaller_position}.")
