""" A playlist class, implementing a Linked List"""

class Song:
  """ Stores the title and artist for one song and a reference to the next song."""

  def __init__(self, songtitle, songartist):
    self.title = songtitle
    self.artist = songartist
    self.next = None  

  def __str__(self):
    return f"{self.title} by {self.artist}"

class Playlist:
  "A playlist that implements a linked list"

  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  def size(self):
    return self._size

  def add_next(self, title, artist):
    """ Adds a new song as the first element in the list"""
    new_song = Song(title, artist)
    if self.head is None:
      # if the list is empty, make the new song the head and tail
      self.head = new_song
      self.tail = new_song
    else:
      # otherwise, make the new song the new head, and update the next reference
      # to point to the old head
      new_song.next = self.head
      self.head = new_song
    self._size += 1

  def play_next(self):
    """ 'Plays' the next song (remove the first Song from the playlist and return the Song) """
    if self.head is None:
      return "Empty Playlist"
    else:
      song = self.head
      self.head = song.next
      if self.head is None:
        self.tail = None
      self._size -= 1
      return song

  def add_song(self, title, artist):
    """Add a song to the end of the playlist"""
    new_song = Song(title, artist)
    if self.tail is None:
      self.head = new_song
      self.tail = new_song
    else:
      self.tail.next = new_song
      self.tail = new_song
    self._size += 1

  def add_song_at(self, title, artist, index):
    """ Adds a song at the given index """
    if index < 0 or index > self._size:
      raise IndexError("Index out of range")
    elif index == 0:
      self.add_next(title, artist)
    elif index == self._size:
      self.add_song(title, artist)
    else:
      new_song = Song(title, artist)
      current_node = self.head
      for i in range(index - 1):
        current_node = current_node.next
      new_song.next = current_node.next
      current_node.next = new_song
      self._size += 1

  def clear_playlist(self):
    """ Clears the entire playlist """
    self.head = None
    self.tail = None
    self._size = 0


  def __str__(self):

    current_node = self.head

    if current_node is None:
      return "+++ Playlist +++\nEmpty Playlist\n"

    i = 0
    output = ["+++ Playlist +++"]
    while current_node != None:
      if i == 0:
        output.append(f"Next:\t{current_node}")
      else:
        output.append(f"{i}:\t\t{current_node}")
      i += 1
      current_node = current_node.next
    output.append("\n")
    return "\n".join(output)


def menu(playlist):
  """ The main menu. This will use the Playlist class to simulate a simple Music Player"""
  print(playlist)
  print()
  print("+++ Main Menu +++")
  print("(1) Play Next")
  print("(2) Add Song")
  print("(3) Add Next Song")
  print("(4) Add Song at Position")
  print("(5) Clear Playlist")
  print("(Q) Quit")

  user_input = input("Please select an option... ")
  acceptable_input = ["1", "2", "3", "4", "5", "Q"]
  if user_input in acceptable_input:
    if user_input == "1":
      print(f"+++ Now Playing: {playlist.play_next()} +++")
      menu(playlist)
    elif user_input == "2":
      title = input("Please input song title ")
      artist = input("Please input song artist ")
      playlist.add_song(title, artist)
      menu(playlist)
    elif user_input == "3":
      title = input("Please input song title ")
      artist = input("Please input song artist ")
      playlist.add_next(title, artist)
      menu(playlist)
    elif user_input == "4":
      title = input("Please input song title ")
      artist = input("Please input song artist ")
      pos = input("Please input new song position")
      playlist.add_song_at(title, artist, pos)
      menu(playlist)

    elif user_input == "5":
      playlist.clear_playlist()
      menu(playlist)
    elif user_input == "Q":
      print("Bye!")

  else:
    print("Please type either 1, 2, 3, 4, or Q and then press enter.")
    menu(playlist)

# entry point of the program
if __name__ == "__main__":

  playlist = Playlist()
  playlist.add_song("Helterskelter", "The Beatles")
  print(playlist)
  # +++ Playlist +++
  # Next:   Helterskelter by The Beatles
 
  playlist.add_next("Battle of Evermore", "Led Zeppelin")
  print(playlist)
  # +++ Playlist +++
  # Next:   Battle of Evermore by Led Zeppelin
  # 1:      Helterskelter by The Beatles

  playlist.add_song("By the Way", "Red Hot Chili Peppers")
  print(playlist)
  # +++ Playlist +++
  # Next:   Battle of Evermore by Led Zeppelin
  # 1:      Helterskelter by The Beatles
  # 2:      By the Way by Red Hot Chili Peppers

  playlist.add_song_at("Bat Out of Hell", "Meatloaf", 1)
  print(playlist)
  # +++ Playlist +++
  # Next:   Battle of Evermore by Led Zeppelin
  # 1:      Bat Out of Hell by Meatloaf
  # 2:      Helterskelter by The Beatles
  # 3:      By the Way by Red Hot Chili Peppers

  playlist.clear_playlist()
  print(playlist)
