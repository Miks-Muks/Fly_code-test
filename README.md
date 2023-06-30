# Fly_code

Тестовое задание для компании Fly_code

# Цель
1. Реализовать сущности авторы, книги, комментарии
1.1 Связь Авторы-Книги (Many-To-Many)
1.2 Реализовать возможность оставлять от имени автора комментарий к книгам.
1.3 В сущность книги обязательно добавить флаг Archived, заархированные книги не выводить в публичной части.
 
2. Реализовать административную часть
    a. CRUD операции для авторов и книг
    b. вывести список книг с обязательным указанием имени авторов в списке и кол-вом комментариев к этой книге
    c. вывести список авторов с указанием кол-ва книг и кол-ва комментариев
 
3.    Реализовать публичную часть сайта с отображение авторов и их книг (простой вывод списка на странице)
    a. Получение списка книг (только те книги, которые не являются заархивированными)
       а.1 Получение списка книг выбранного автора (только те книги, которые не являются заархивированными)
    b. Получение конкретной книги 
    c. Редактирование книги
    d. Изменение флага Archived
    e. Удаление книги
3.1 Реализовать комментарии
    а. Создание комментария к книге
    b. Изменение комментария
    с. Удаление комментария.

4.  Реализовать регистрацию и JWT авторизацию.*
    а. Реализовать функционал  регистрации и JWT авторизации авторов
    b. Доработать методы публичной части:
       b.1 Получение списка книг (только те книги, которые не являются заархивированными), получить книги того автора, который авторизован в данный момент
       b.1 Изменения/удаление/получение выбранной книги, только если она связана с автором