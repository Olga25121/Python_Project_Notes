import datetime
import controller
import json


class Notebook:
    def get_id(self, length_notebook: int):
        if length_notebook == 0:
            new_id = 1
        else:
            new_id = self.note_book[len(self.note_book) - 1]['id'] + 1
            i = len(self.note_book) - 1
            if self.note_book[i]['id'] == new_id:
                while True:
                    new_id += 1
        return new_id
    
    def new(self, new_note: dict):
        self.note_book.append(new_note)

    def get(self):
        return self.note_book
    
    def delete(self, index_note_del: int):
        if index_note_del in range(len(self.note_book)):
            for num in range(len(self.note_book)):
                if num == index_note_del:
                    del self.note_book[num]
        else:
            return False
        
    def change(self, id_note_change: int, ch_note: dict):
        date_note = datetime.datetime.now().strftime("%d.%m.%Y : %H.%M.%S")
        self.note_book[id_note_change]['title'] = ch_note['title'] if ch_note['title'] != '' else \
            self.note_book[id_note_change]['title']
        self.note_book[id_note_change]['msg'] = ch_note['msg'] if ch_note['msg'] != "" else \
            self.note_book[id_note_change]['msg']
        self.note_book[id_note_change]['data_change'] = date_note

    def search(self, find: str):
        result = []
        for note in self.note_book:
            if find in note['data_change'][:10]:
                result.append(note)
        return result


