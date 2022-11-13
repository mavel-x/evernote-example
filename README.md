# evernote_example
Консольный клиент для [Evernote](https://evernote.com/).

## Как запустить
1. Для этого проекта понадобится Python2 и учетная запись на [Evernote](https://dev.evernote.com/doc/).
2. Скачайте файлы из репозитория, перейдите в каталог проекта и установите необходимые 
библиотеки командой:
    ```commandline
    $ pip install -r requirements.txt
    ```
3. Создайте файл `.env` в каталоге проекта и заполните его необходимыми ключами с Evernote. 
Для удобства можно воспользоваться файлом `.env.sample` (переименуйте его и заполните своими значениями).
   ```text
   EVERNOTE_CONSUMER_KEY=replace_me
   EVERNOTE_CONSUMER_SECRET=replace_me
   EVERNOTE_PERSONAL_TOKEN=replace_me
   JOURNAL_TEMPLATE_NOTE_GUID=replace_me
   JOURNAL_NOTEBOOK_GUID=replace_me
   INBOX_NOTEBOOK_GUID=replace_me
   ```
- `JOURNAL_NOTEBOOK_GUID` -- это ID вашего блокнота "Дневник".
- `JOURNAL_TEMPLATE_NOTE_GUID` -- ваш шаблон для новых заметок.
- `INBOX_NOTEBOOK_GUID` -- ваш блокнот для входящих заметок.

## Как пользоваться

### Файл list_notebooks.py
```commandline
$ python list_notebooks.py
```
Этот файл выведет в терминал ID и названия всех ваших блокнотов.

### Файл dump_inbox.py
```commandline
$ python dump_inbox.py
```
```commandline
$ python dump_inbox.py 20
```
Этот файл выведет в терминал входящие заметки из вашего блокнота для входящих. 
В качестве аргумента вы можете передать число последних заметок, которые хотите увидеть.
Количество по умолчанию -- 10.

### Файл add_note2journal.py
```commandline
$ python add_note2journal.py
```
Этот файл создает заметку в блокноте "Дневник". Заметка будет копией вашего шаблона для заметок.
После успешного создания в терминал будет выведен заголовок заметки.

По умолчанию заметка создается от текущего дня. 
Чтобы создать заметку с другой датой, передайте в качестве аргумента либо дату в формате ГГГГ-ММ-ДД...
```commandline
$ python add_note2journal.py 2017-10-21
```
...либо число дней, на которое вы хотите сместить дату заметки от сегодняшней даты 
(поставьте `-` перед числом, чтобы сместить дни в прошлое):
```commandline
$ python add_note2journal.py 5
```
```commandline
$ python add_note2journal.py -5
```

## Запланированные функции
В будущем планируется добавить возможность передавать текст заметки для публикации, 
а также прикреплять медиа-файлы.


## Цель проекта
Проект написан в учебных целях для школы Python-разработчиков [dvmn.org](dvmn.org).
