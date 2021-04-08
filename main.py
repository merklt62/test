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


def task_2():  # Решение второй задачи
    '''
    Для решения второй задачи получаем все словари из списка,
    затем берём из каждого словаря ключ и значение,
    ключ помещаем в открывающий и закрывающий тег,
    а значение вставляем между ними.
    '''

    # Загружаем из json все данные
    with open('source_2_3.json') as f:
        json_data = json.load(f)

    html = ''
    for i in json_data:
        for tag, value in i.items():
            html += f"<{tag}>{value}</{tag}>"
    write(html)
    return html


def task_3():  # Решение третьей задачи
    '''
    Решение третьей задачи базируется на решении второй.
    Добавлена проверка, если данные лежат в списке словарей,
    то этот список оборачивается в открывающие и закрывающие теги ul,
    затем каждый словарь оборачивается в теги li, иначе (если данные изначально
    были представлены как словари), оборачиваем словари в теги li.
    '''

    # Загружаем из json все данные
    with open('source_2_3.json') as f:
        json_data = json.load(f)

    if type(json_data) == list:
        html = '<ul>'
        for i in json_data:
            html += '<li>'
            for tag, value in i.items():
                html += f"<{tag}>{value}</{tag}>"
            html += '</li>'
        html += '</ul>'
    else:
        html += '<li>'
        for tag, value in json_data.items():
            html += f"<{tag}>{value}</{tag}>"
        html += '</li>'
    write(html)


def task_4():  # Решение четвёртой задачи
    '''
    Решение базируется на решении третьей задачи.
    Добавляем проверку на нахождение списка в значении словаря,
    если в значении лежит список, открываем тег полученный из ключа этого
    значения и, так как это писок, оборачиваем его в тег ul, получаем словари
    из этого списка и оборачиваем их в теги li, далее записываем ключи как
    открывающие и закрывающие теги и между ними помещаем полученное значение,
    когда словари в этом списке закончатся, то закрываем теги li, ul и тег,
    полученный из ключа.
    '''

    # Загружаем из json все данные
    with open('source_4.json') as f:
        json_data = json.load(f)

    if type(json_data) == list:
        html = '<ul>'
        for list_item in json_data:
            html += '<li>'
            for tag, value in list_item.items():
                if type(value) == list:
                    html += f"<{tag}><ul>"
                    for i in value:
                        html += '<li>'
                        for t, v in i.items():
                            html += f"<{t}>{v}</{t}>"
                    html += f"</li></ul></{tag}>"
                else:
                    html += f"<{tag}>{value}</{tag}>"
            html += '</li>'
        html += '</ul>'
    else:
        html += '<li>'
        for tag, value in json_data.items():
            if type(value) == list:
                html += f"<{tag}><ul>"
                for i in value:
                    html += '<li>'
                    for t, v in i.items():
                        html += f"<{t}>{v}</{t}>"
                html += f"</li></ul></{tag}>"
            else:
                html += f"<{tag}>{value}</{tag}>"
        html += '</li>'
    write(html)


def task_5():  # Решение пятой задачи
    '''
    Решение пятой задачи рассматривается как отдельное, не связанное с
    предыдущими.
    Получаем ключ и значение из словаря. Если в ключе содержится точка,
    то разбиваем строку по точкам на список, далее берём первый элемент из
    полученного списка и записываем его как тег. Если в полученном списке
    находим октотроп, то разбиваем найденный элемент по октотропу,
    так как первый элемент из полученного списка представляет собой класс,
    то записываем его как class, иначе (то есть все остальные элементы)
    записываем как id. Если же изначально небыло октотропа, то записываем
    элементы списка как class, добавляем значение, предварительно заменив
    угловые скобки на '&gt;' и '&lt;', закрываем тег первым элементом
    и переходим к проверке следующих элементов в словаре.
    '''
    # Загружаем из json все данные
    with open('source_5.json') as f:
        json_data = json.load(f)

    html = ''
    for key, value in json_data.items():
        if '.' in key:
            key = key.split('.')
            for k in range(len(key)):
                if k == 0:
                    html += f'<{key[k]}'
                elif '#' in key[k]:
                    key[k] = key[k].split('#')
                    for i in range(len(key[k])):
                        if i == 0:
                            html += f' class="{key[k][i]}"'
                        else:
                            html += f' id="{key[k][i]}"'
                else:
                    html += f' class"{key[k]}"'
        value = value.replace('>', '&gt;').replace('<', '&lt;')
        html += f'>{value}</{key[0]}>'
    write(html)

# Тесты


class NameTestCase(unittest.TestCase):
    def test_task_1(self):
        html = task_1()
        self.assertEqual(html, '<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>')
    def test_task_2(self):
        html = task_2()
        self.assertEqual(html, '<h3>Title #1</h3><div>Hello, World 1!</div><h3>Title #2</h3><div>Hello, World 2!</div>')


unittest.main()
