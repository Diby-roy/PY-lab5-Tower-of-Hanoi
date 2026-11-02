def hanoi_solver(num_of_disks):
    #Only Natural numbers are allowed 
    if not isinstance(num_of_disks, int) or num_of_disks < 1:
        return "Only enter a positive number."

    rod1 = [disk for disk in range(num_of_disks, 0, -1)]
    rod2 = []
    rod3 = []

    def get_list_string():
        return f"{rod1} {rod2} {rod3}\n"

    def move_disk(start, target):
        if not start:
            return
        target.append(start.pop())

    def move_tower(start, target, auxiliary, n):
        if n == 0:
            return ""

        result = ""
        result += move_tower(start, auxiliary, target, n - 1)
        move_disk(start, target)
        result += get_list_string()
        result += move_tower(auxiliary, target, start, n - 1)
        return result

    result = get_list_string()
    result += move_tower(rod1, rod3, rod2, num_of_disks)
    return result.rstrip("\n")


if __name__ == "__main__":
    try:
        n = int(input("How many disks? : "))
        print(hanoi_solver(n))
    except ValueError:
        print("Please enter your positive number.")