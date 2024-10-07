def main():
    filename = input() 

    with open(filename, 'r') as f:
        for line in f:
            photo_file = line.strip()


            if photo_file:
                info_file = photo_file.replace("_photo.jpg", "_info.txt")
                print(info_file)


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")