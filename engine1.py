def main():
    grid = float(input("simulation grid size? "))
    density = float(input("Base voxel density? "))

    memory_required = allocate_ram(grid,density)
    print("memory_required=")
    print(f"{memory_required:.2f}")

# or 

    print(f"Voxel engine initialize. Allocating {memory_required:.2f} MB of RAM")
def allocate_ram(grid,density):
    return grid*density*1.048

main()
