
chosen_volume = input("\nWhich volume of scripture would you like to learn about?")

max_chapters = -1
book_with_max = ""

with open("books_and_chapters.txt") as books_file:

  for line in books_file:
    parts = line.split(":")
    
    book = parts[0].strip()

    chapters = int(parts[1])

    scripture = parts[2].strip()

    if scripture.lower() == chosen_volume.lower():
      print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

      if chapters > max_chapters:
        max_chapters = chapters
        book_with_max = book

print(f"\nThe book with the most chapters is: {book_with_max}")
print(f"It has {max_chapters} chapters")