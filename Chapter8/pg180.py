# Function to create an album dictionary
def make_album(artist, title, number_of_songs=None):
    album = {'artist': artist, 'title': title}
    
    # If the number of songs is provided, add it to the album dictionary
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    
    return album

# Call the function with different albums
album1 = make_album('Taylor Swift', '1989')
album2 = make_album('Ed Sheeran', 'Divide', 12)
album3 = make_album('Adele', '25', 11)

# Print the albums
print(album1)
print(album2)
print(album3)









print('8-8')
# Function to create an album dictionary
def make_album(artist, title, number_of_songs=None):
    album = {'artist': artist, 'title': title}
    
    # If the number of songs is provided, add it to the album dictionary
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    
    return album

# While loop to allow users to input albums
while True:
    print("\nPlease enter the album details (or type 'quit' to exit):")
    
    # Get user input for the artist name
    artist = input("Enter the artist name: ")
    if artist.lower() == 'quit':
        break  # Exit the loop if the user types 'quit'
    
    # Get user input for the album title
    title = input("Enter the album title: ")
    if title.lower() == 'quit':
        break  # Exit the loop if the user types 'quit'
    
    # Get user input for the number of songs (optional)
    songs_input = input("Enter the number of songs (press enter to skip): ")
    
    if songs_input:
        number_of_songs = int(songs_input)  # Convert the input to an integer
    else:
        number_of_songs = None
    
    # Create the album dictionary
    album = make_album(artist, title, number_of_songs)
    
    # Print the album details
    print("\nHere is the album you created:")
    print(album)
