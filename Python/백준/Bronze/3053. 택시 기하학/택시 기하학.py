import math

def calculate_areas(R):
    euclidean_area = math.pi * (R ** 2)
    taxi_area = 2 * (R ** 2)
    
    return euclidean_area, taxi_area

if __name__ == "__main__":
    R = int(input().strip())
    euclidean_area, taxi_area = calculate_areas(R)
    
    print(f"{euclidean_area:.6f}")
    print(f"{taxi_area:.6f}")
