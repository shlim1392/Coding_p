def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  
    tulip_varieties_in_garden = list(map(int, data[1:])) 
    
    total_varieties = 15000
    unique_tulips = set(tulip_varieties_in_garden)
    missing_varieties = total_varieties - len(unique_tulips)
    
    print(missing_varieties)

if __name__ == "__main__":
    main()
