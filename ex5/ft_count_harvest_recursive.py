one_time = False
days_until = 0
count = 1


def ft_count_harvest_recursive():
    global one_time
    global days_until
    global count
    if not (one_time):
        days_until = int(input("Days until harvest: "))
        one_time = True
    print(f"Day {count}")
    count += 1
    if count <= days_until:
        ft_count_harvest_recursive()


ft_count_harvest_recursive()
