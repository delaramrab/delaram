import sys
sys.setrecursionlimit(10**6)

move_counter = 0


def solve_towers(disks_number: int, tower_source: int, tower_destination: int, tower_temp: int):
    global move_counter

    if disks_number == 1:
        print(f"{tower_source} --> {tower_destination}")

        move_counter += 1
        return

    solve_towers(disks_number - 1, tower_source, tower_temp, tower_destination)

    print(f"{tower_source} --> {tower_destination}")
    move_counter += 1

    solve_towers(disks_number - 1, tower_temp, tower_destination, tower_source)


start_peg = 1
end_peg = 3
temp_peg = 2
total_disks = 4


solve_towers(total_disks, start_peg, end_peg, temp_peg)
print(move_counter)
