from collections import defaultdict

# Get Input file
input_file = input()  

# Setup dictionary for list
seasons_dict = defaultdict(list)

# Read the input file
with open(input_file, 'r') as f:    
    input_reader = f.readlines()

    for i in range(0, len(input_reader), 2): 
        if i + 1 < len(input_reader): 
            season_row = input_reader[i].strip()
            show_row = input_reader[i + 1].strip()

        if season_row:
            try:
                seasons = int(season_row) 
                seasons_dict[seasons].append(show_row)
            except ValueError:
                print("Blank in row")

# Sort the dictionary by number of seasons in descending order
sorted_seasons = dict(sorted(seasons_dict.items(), key=lambda x: x[0], reverse=True))

# Write to output_keys.txt
with open('output_keys.txt', 'w') as output_file:
    for seasons, shows in sorted_seasons.items():
        output_file.write(f"{seasons}: {'; '.join(shows)}\n")

# Get the list of shows to be sorted
all_shows = []
for show_list in seasons_dict.values():  # Changed variable name to avoid confusion
    all_shows.extend(show_list)

# Sort the shows in alphabetical order
sorted_shows = sorted(all_shows, reverse = True)  

# Write to output_titles.txt
with open('output_titles.txt', 'w') as output_file:
    for title in sorted_shows:
        output_file.write(f"{title}\n")
