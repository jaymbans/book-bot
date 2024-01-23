def main():
  with open("books/frankenstein.txt") as f:
    letter_hash = {}
    file_contents = f.read()
    #count words
    words = file_contents.split()

    #group by letter and count
    for char in file_contents.lower():
      if(not char.isalpha()):
        continue
      letter_hash[char] = 1+letter_hash.get(char,0)
  
  print(f"---Begin report of {f.name} ---")
  sorted_keys = list(letter_hash.keys())
  sorted_keys.sort()

  for letter in sorted_keys:
    print(f"The '{letter}' character was found {letter_hash[letter]} times")
    
  
main()