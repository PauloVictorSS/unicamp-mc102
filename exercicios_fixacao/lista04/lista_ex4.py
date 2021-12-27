int_list = list(map(int, input("Digite uma lista: ").split()))

start_of_sequence = 0

last_size_of_sequence = 1
size_of_sequence = 1

for i in range(1, len(int_list)):

    if(int_list[i] > int_list[i-1]):
        size_of_sequence += 1
    else:
        size_of_sequence = 1

    if(size_of_sequence > last_size_of_sequence):
        last_size_of_sequence = size_of_sequence
        start_of_sequence = i + 1 - last_size_of_sequence

text_list = ""

for i in range(start_of_sequence, (start_of_sequence+last_size_of_sequence)):
    text_list += str(int_list[i]) + " "

print(f"Uma maior subsequencia crescente é {text_list}e tem {last_size_of_sequence} elementos.")