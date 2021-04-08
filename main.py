import json
import unittest


def write(html):
    '''
    Функция для записи конечного объекта в html
    '''
    with open('index.html', 'w') as f:
        f.write(html)


def task_1():  # Решение первой задачи
    '''
    Проверяем в цикле ключ объекта, если он равен title, то записываем
    его значение в строку заголовка, а если ключ равен body, то записываем
    значение в строку параграфа.
    '''

    # Загружаем из json все данные
    with open('source_1.json') as f:
        json_data = json.load(f)

    html = ''
    for i in range(len(json_data)):
        html += f"<h1>{json_data[i]['title']}</h1>"
        html += f"<p>{json_data[i]['body']}</p>"
    write(html)
    return html


class NameTestCase(unittest.TestCase):
    def test_task_1(self):
        html = task_1()
        self.assertEqual(html, '<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>')


unittest.main()