from pathlib import Path

contents = 'i love programming. \n'
contents += 'i love creating new games. \n'
contents += 'i love working with data. \n'
path = Path('C:/Users/nurop/OneDrive/Desktop/pYTHON COURSE/pitext.txt')

contents = path.read_text(encoding='utf-8')
    
path.open()

path.write_text(contents)

