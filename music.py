import os
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        self.current_track = None

    def load_playlist(self, playlist_name):
        if os.path.exists(playlist_name):
            with open(playlist_name, 'r') as file:
                self.playlist = [line.strip() for line in file.readlines()]
        else:
            print("Playlist not found.")

    def save_playlist(self, playlist_name):
        with open(playlist_name, 'w') as file:
            for track in self.playlist:
                file.write(track + '\n')

    def add_to_playlist(self, song_path):
        if song_path.endswith('.mp3') and os.path.exists(song_path):
            self.playlist.append(song_path)
        else:
            print("Invalid file or format.")

    def play(self, index=None):
        if index is None:
            index = 0
        if 0 <= index < len(self.playlist):
            pygame.mixer.music.load(self.playlist[index])
            pygame.mixer.music.play()
            self.current_track = index
            print(f"Now playing: {self.playlist[index]}")
        else:
            print("Invalid index.")

    def stop(self):
        pygame.mixer.music.stop()
        self.current_track = None
        print("Music stopped.")

    def next_track(self):
        if self.current_track is not None:
            self.stop()
            self.play(self.current_track + 1)

    def previous_track(self):
        if self.current_track is not None:
            self.stop()
            self.play(self.current_track - 1)

    def display_playlist(self):
        if self.playlist:
            print("Current Playlist:")
            for index, track in enumerate(self.playlist):
                print(f"{index}. {track}")
        else:
            print("Playlist is empty.")


def main():
    player = MusicPlayer()

    while True:
        print("\n==== Music Player Menu ====")
        print("1. Load Playlist")
        print("2. Save Playlist")
        print("3. Add to Playlist")
        print("4. Play")
        print("5. Stop")
        print("6. Next Track")
        print("7. Previous Track")
        print("8. Display Playlist")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            playlist_name = input("Enter playlist file name: ")
            player.load_playlist(playlist_name)
        elif choice == '2':
            playlist_name = input("Enter playlist file name to save: ")
            player.save_playlist(playlist_name)
        elif choice == '3':
            song_path = input("Enter path of the song to add: ")
            player.add_to_playlist(song_path)
        elif choice == '4':
            player.display_playlist()
            track_index = int(input("Enter track number to play: "))
            player.play(track_index)
        elif choice == '5':
            player.stop()
        elif choice == '6':
            player.next_track()
        elif choice == '7':
            player.previous_track()
        elif choice == '8':
            player.display_playlist()
        elif choice == '9':
            print("Exiting Music Player. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
