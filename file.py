import json

note_book = []
path = 'note_book.json'

def open(self):
       with open(self.path, encoding='UTF-8') as data:
            file = json.load(data)  
            for note in file:
                 self.note_book.append(note)

def save(self):
        nb_str = []
        for note in self.note_book:
            nb_str.append(note)
        with open(self.path, 'w', encoding='UTF-8') as data:
            json.dump(nb_str, data, ensure_ascii=False, indent=2)