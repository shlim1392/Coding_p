import math

def calculate_paint_cans(n, width, length, height, area_per_can, windows_doors):
    ceiling_area = width * length
    wall_area = 2 * (height * width) + 2 * (height * length)
    
    total_area = ceiling_area + wall_area
    
    for wd_width, wd_height in windows_doors:
        total_area -= wd_width * wd_height
    
    total_area_all_apartments = total_area * n
    
    cans_required = math.ceil(total_area_all_apartments / area_per_can)
    
    return cans_required

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    index = 0
    results = []
    
    while index < len(data):
        n, width, length, height, area, m = map(int, data[index].split())
        if n == 0 and width == 0 and length == 0 and height == 0 and area == 0 and m == 0:
            break
        index += 1
        
        windows_doors = []
        for _ in range(m):
            wd_width, wd_height = map(int, data[index].split())
            windows_doors.append((wd_width, wd_height))
            index += 1
        
        cans_needed = calculate_paint_cans(n, width, length, height, area, windows_doors)
        results.append(cans_needed)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
