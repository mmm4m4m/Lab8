class Notebook:
    def __init__(self):
        self.notebook = {}
        self.__note_id = self.__id_generator()

    def add_note(self, last_name, number, birth_date):
        self.notebook[next(self.__note_id)] = {'last_name': last_name,
                                               'number': number,
                                               'birth_date': birth_date}

    def __id_generator(self):
        i = 1
        while True:
            yield i
            i += 1

    def delete_note(self, num):
        if num not in self.notebook:
            print('Такой записи не существует')
        else:
            print(f'Удаление записи №{num}')
            return self.notebook.pop(num)

    def __search(self, val, by_key): # by_key - по какому ключу ведется поиск
        notes = {}
        for key, value in self.notebook.items():
            if value[by_key] == val:
                notes[key] = value
        return notes

    def sort_by_field(self, field): # сортировка по полю
        print(f'Сортировка записей по полю {field}')
        return sorted(self.notebook.values(), key=lambda x: x[field])

    def search_by_number(self, number):
        print('Поиск записей по номеру')
        notes = self.__search(number, 'number')
        if not notes:
            print('Записей с таким номером нет')
        return notes

    def search_by_birth_date(self, date):
        print('Поиск записей по дате рождения')
        notes = self.__search(date, 'birth_date')
        if not notes:
            print('Записей с такой датой рождения нет')
        return notes

    def search_by_lastname(self, last_name):
        print('Поиск записей по фамилии')
        notes = self.__search(last_name, 'last_name')
        if not notes:
            print('Записей с такой фамилией нет')
        return notes


if __name__ == '__main__':
    notebook = Notebook()
    
    notebook.add_note('Дмитриев', 79561824728, 2007)
    notebook.add_note('Александров', 79782653826, 2006)
    notebook.add_note('Александров', 79385632658, 2011)
    
    sorted_by_birth_date = notebook.sort_by_field('birth_date')
    print(f'Отсортированный список записей: {sorted_by_birth_date}')
    
    notes_by_lastname = notebook.search_by_lastname('Александров')
    print(f'Все записи с фамилией Александров: {notes_by_lastname}')
    
    notebook.delete_note(1)
    print(f'Записная книжка после удаления записи: {notebook.notebook}')
