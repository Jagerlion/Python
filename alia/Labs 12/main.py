# Type your code here. 
if __name__ == "__main__":
    input_file = input()
    lower_bound = input()
    upper_bound = input()
    
    f = open(input_file)
    lines = f.readlines()
    f.close()
    
    for line in lines:
        i = line.strip()
        if lower_bound <= i <= upper_bound:
            print(f"{i} - in range")
        else:
            print(f"{i} - not in range")