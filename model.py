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

