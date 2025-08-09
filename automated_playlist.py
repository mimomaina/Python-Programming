import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Spotify API credentials
client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'
redirect_uri = 'REDIRECT_URI'

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='playlist-modify-public user-library-read playlist-read-private'))

# Get authenticated user ID
user_id = sp.current_user()['id']

# Menu function
def menu():
    print("\n--- Spotify Playlist Manager ---")
    print("1. Create a Playlist")
    print("2. Search for a Song and Add to a Playlist")
    print("3. Remove a Song from a Playlist")
    print("4. View Your Playlists")
    print("5. Delete a Playlist")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

# Function to create a new playlist
def create_playlist():
    playlist_name = input("Enter the playlist name: ")
    playlist_description = input("Enter the playlist description: ")
    new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)
    print(f"Playlist '{playlist_name}' created with ID: {new_playlist['id']}")

# Function to search for a song
def search_song():
    song_name = input("Enter the song name: ")
    artist_name = input("Enter the artist name: ")
    results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track', limit=1)
    if results['tracks']['items']:
        song_uri = results['tracks']['items'][0]['uri']
        song_name = results['tracks']['items'][0]['name']
        print(f"Found song: {song_name}")
        return song_uri
    else:
        print("No songs found.")
        return None

# Function to add a song to a playlist
def add_song_to_playlist():
    playlist_id = input("Enter the playlist ID: ")
    song_uri = search_song()
    if song_uri:
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=[song_uri])
        print("Song added to playlist.")

# Function to remove a song from a playlist
def remove_song_from_playlist():
    playlist_id = input("Enter the playlist ID: ")
    song_uri = search_song()
    if song_uri:
        sp.user_playlist_remove_all_occurrences_of_tracks(user=user_id, playlist_id=playlist_id, tracks=[song_uri])
        print("Song removed from playlist.")

# Function to view user's playlists
def view_playlists():
    playlists = sp.current_user_playlists(limit=10)
    for playlist in playlists['items']:
        print(f"Playlist Name: {playlist['name']}, ID: {playlist['id']}")

# Function to delete a playlist
def delete_playlist():
    playlist_id = input("Enter the playlist ID to delete: ")
    sp.user_playlist_unfollow(user=user_id, playlist_id=playlist_id)
    print("Playlist deleted.")

# Main program loop
while True:
    choice = menu()
    if choice == '1':
        create_playlist()
    elif choice == '2':
        add_song_to_playlist()
    elif choice == '3':
        remove_song_from_playlist()
    elif choice == '4':
        view_playlists()
    elif choice == '5':
        delete_playlist()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
