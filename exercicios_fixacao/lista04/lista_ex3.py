int_list = list(map(int, input().split()))

movement = int(input())

for i in range(movement):

    int_list.append(int_list[0])
    int_list.remove(int_list[0])

print(int_list)
