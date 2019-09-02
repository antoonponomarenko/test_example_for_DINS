**Спецификация файлов и директорий.**

На FTP(в корневой директории) лежат файлы для тестирования, их набор и размеры - фиксированы. В корневой директории отсутствует доступ на запись и удаление файлов. В директорию /upload можно загружать файлы для тестирования скорости загрузки, файлы из этой папки удаляются сразу по завершении загрузки.

Минимальная скорость скачивания с ftp сервера 50 КБ/С (значение установлено ввиду его отсутствия в условиях задачи)

перечень файлов и директорий:

№ |группа доступа|размер(кб)|дата|название
-- | -- | -- | -- | -- 
1|-rw-r--r--|1073741824000| Feb 19 2016|1000GB.zip
2|-rw-r--r--|107374182400| Feb 19 2016 |100GB.zip
3|-rw-r--r--|102400| Feb 19 2016 |100KB.zip
4|-rw-r--r--|104857600| Feb 19 2016| 100MB.zip
5|-rw-r--r--|10737418240| Feb 19 2016 |10GB.zip
6|-rw-r--r--|10485760| Feb 19 2016 |10MB.zip
7|-rw-r--r--|1073741824| Feb 19 2016 |1GB.zip
8|-rw-r--r--|1024| Feb 19 2016 |1KB.zip
9|-rw-r--r--|1048576 |Feb 19 2016 |1MB.zip
10|-rw-r--r--|209715200| Feb 19 2016 |200MB.zip
11|-rw-r--r--|20971520 |Feb 19 2016 |20MB.zip
12|-rw-r--r--|2097152 |Feb 19 2016 |2MB.zip
13|-rw-r--r--|3145728 |Feb 19 2016 |3MB.zip
14|-rw-r--r--|524288000| Feb 19 2016| 500MB.zip
15|-rw-r--r--|53687091200| Jul 24 2014 |50GB.zip
16|-rw-r--r--|52428800| Feb 19 2016| 50MB.zip
17|-rw-r--r--|524288| Feb 19 2016 |512KB.zip
18|-rw-r--r--|5242880| Feb 19 2016| 5MB.zip
19|-drwxr-xr-x|DIR| mm-dd-yy| upload
 



**Тестовые сценарии:**

- [x] 0. Проверка соединения с сервером.
- [x] 1. Кол-во файлов соответствует заданному.
- [x] 2. Размеры файлов соответствуют заданным.
- [x] 3. Названия файлов соответствуют заданным.
- [ ] 4. Доступ к файлам (файлы доступны на скачивание).
- [ ] 5. Директории соответствуют заданным.
- [ ] 6. Отсутствие возможности перезаписи файлов на ftp сервере в директории с ограниченным доступом
- [ ] 7. Возможность удаления файлов с ftp сервера.
- [ ] 8. Возможность загрузки файлов на ftp сервер
- [ ] 9. Отсутствие возможности создания директорий в директории с ограниченным доступом.
- [ ] 10. Отсутствие возможности удаления директории на ftp сервере..
- [ ] 11. Конфликт имен файлов на Ftp сервере.
- [ ] 12. Конфликт имен директории (upload) на Ftp сервере.
- [ ] 13. Соответствия названий файлов после скачивания.
- [ ] 14. Соответствия размеров файлов после скачивания.
- [ ] 15. Соответствие размера и времени при скачивании файла.
- [ ] 16. Загрузка файлов (не в директорию Upload).

**0. Проверка соединения с сервером  .**

**перечень шагов:**
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

№ | Действие| Ожидаемый результат
-- | -- | --
1 |Произвести подключение к ftp серверу (ftp://speedtest.tele2.net/) через анонимного пользователя | Получаем код статуса операции '230'






**1. Кол-во файлов соответствует заданному.**

**изначальное состояние:**

Произведено подключение к ftp серверу ! ! !!!!!(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.

**перечень шагов:**
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

№ | Действие| Ожидаемый результат
-- | -- | --
1 | Делаем запрос списка файлов с ftp сервера | Получаем от сервера список файлов
2 | Сверяем количество полученных файлов со спецификацией | Количество файлов 18 шт.

   
 **2. Размеры файлов соответствуют заданным.**    

**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    

**перечень шагов:**


№ | Действие| Результат
-- | -- | --
1 | Делаем запрос списка файлов с ftp сервера | Получаем от сервера список файлов
2 | Сверяем размеры полученных файлов со спецификацией | Полное совпадение размеров  файлов с сервера с файлами из  спецификации.




 **3. Названия файлов соответствуют заданным.**

  
**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    


**перечень шагов:**

№ | Действие| Результат
-- | -- | --
1 | Делаем запрос списка файлов с ftp сервера | Получаем от сервера список файлов
2 |Сверяем названия файлов со спецификацией.| Полное совпадение названий  файлов с сервера с файлами из  спецификации.


**4. Доступ к файлам (файлы доступны на скачивание).**

**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    

**перечень шагов:**


№ | Действие| Результат
-- | -- | --
1 | Проверка наличия файла на сервере| Файл на сервере есть
2 |Команда скачивания файла с сервера.| Получение от сервера сообщения  о успешном завершении операции (загрузка завершена)
3|Проверка наличия загруженного файла на компьютере тестировщика| Файл успешно загружен на компьютер тестировщика
4 |Открываем файл на компьютере тестировщика| Файл успешно открывается





**5. Директории соответствуют заданным.**


**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    

**перечень шагов:**

№ | Действие| Результат
-- | -- | --
1 |Делаем запрос о директориях с сервера| Получаем список директорий от сервера
2 |Сверяем директории со спецификацией| Полное совпадение директорий с сервера с директориями  из  спецификации)



**6. Отсутствие возможности перезаписи файлов на ftp сервере в директории с ограниченным доступом.**

**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    

**перечень шагов:**

№ | Действие| Результат
-- | -- | --
1 |Проверка наличия файла на сервере| Файл есть
2 |Команда перезаписи файла на  сервере | Получение от сервера сообщения  блокировки операции(отказ доступа).
3 |Повторная проверка наличия файла на сервере. | Файл на сервере в исходном виде (соответствие размера).



**7. Возможность удаления файлов с ftp сервера.**


**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    


**перечень шагов:**

№ | Действие| Результат
-- | -- | --
1 |Проверка наличия файла на сервере| Файл есть
2 |Команда удаления  файла сервера | Получение от сервера сообщения  блокировки операции(отказ доступа)
3 |Повторная проверка наличия файла на сервере. | Файл остался на сервере


**8. Возможность загрузки файлов на ftp сервер.**
!!!!! зафиксировать размеры и названия файлов

**изначальное состояние:**

Произведено подключение к ftp серверу (ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    


**перечень шагов:**

№ | Действие| Результат
-- | -- | --
1 | Команда переход в директорию upload| Пользователь находится в директории /upload
2 | Проверка отсутствия (произвольного) загружаемого файла на сервере| Файла нет
3 | Команда загрузки файла на сервер |Получение от сервера сообщения  успешного завершения операции(загрузка завершена успешно)

******Тестирование загрузки файла ДОПИСАТЬ!!!!

**9. Отсутствие возможности создания директорий в директории с ограниченным доступом.**
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!доделывать!

**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    

**перечень шагов:**


№ | Действие| Результат
-- | -- | --
1 | Проверка отсутствия директорий на сервере в директории с ограниченным доступом| Директория отсутствует
2 | Команда загрузки директории в директорию| получение от сервера сообщения  блокировки операции(отказ доступа)
3 | Повторная проверка наличия директории на сервере | Отсутствие загружаемой директории на сервере


**10. Отсутствие возможности удаления директории на ftp сервере.**
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!доделывать
**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    

**перечень шагов:**

№ | Действие| Результат
-- | -- | --
1 | Проверка наличия директории upload на сервере | Директория есть
2 | Команда удаления директории upload с сервера| Получение от сервера сообщения  блокировки операции(отказ доступа)
3 | Повторная проверка наличия директории upload на сервере. |  Директория не удалилась (осталась на сервере)




**11. Конфликт имен файлов на Ftp сервере.**

!!!!!!!!!!!!! паралельно два в upload


**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    


**перечень шагов:**

№ | Действие| Результат
-- | -- | --
1 |Проверка наличия файла на сервере | Файл на сервере есть
2 | Зафиксировать размер файла с сервера| 
3 | Команда загрузки файла на сервер. |  Получение от сервера сообщения  блокировки операции(отказ доступа)
4 | Повторная проверка наличия файла на сервере |  Файл на сервере сохранился в исходном состоянии

**12. Конфликт имен директории (upload) на Ftp сервере.**
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! конфликт имен директорий паралельная загрузка в upload
**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    


**перечень шагов:**

№ | Действие| Результат
-- | -- | --
1 |Проверка наличия директории на сервере | Директории на сервере есть
2 | Команда загрузки директории на сервер | Получение от сервера сообщения  блокировки операции(отказ доступа)
3 |Повторная проверка наличия директории на сервере | Директория на сервере сохранилась в исходном состоянии



**13. Соответствия названий файлов после скачивания.**


**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    

**перечень шагов:**

№ | Действие| Результат
-- | -- | --
1 |Проверка наличия файла на сервере | Файл есть
2 | Команда загрузки файла с сервера.| Получение от сервера сообщения  о успешном завершении операции (загрузка завершена)
3 |Проверка наличия загруженного файла на компьютере тестировщика| Файл есть
4 |Сверка имени загруженного файла на компьютере тестировщика с  именем на сервере | Полное совпадение имен файлов


**14. Соответствия размеров файлов после скачивания.**

   

**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    


**перечень шагов:**


№ | Действие| Результат
-- | -- | --
1 |Проверка наличия файла на сервере | Файл есть
2 |Команда загрузки файла с сервера| Получение от сервера сообщения  о успешном завершении операции (загрузка завершена)
3 |Проверка наличия загруженного файла на компьютере тестировщика. | Файл есть
4 |Проверка размера загруженного файла на компьютере тестировщика с  размером  файла на сервере | Полное совпадение размеров


**15. Соответствие размера и времени при скачивании файла.**

    
**изначальное состояние:**

Произведено подключение к ftp серверу(ftp://speedtest.tele2.net/) через анонимного пользователя. Пользователь находится в корневой директории.    

**перечень шагов:**


№ | Действие| Результат
-- | -- | --
1 |Проверка наличия файла на сервере | Файл есть
2 |Команда скачивания файла с сервера |  Получение от сервера сообщения  о успешном завершении операции (загрузка завершена)
3 |Проверка наличия скаченного файла на компьютере тестировщика | Скорость скачивания файла не ниже минимально допустимого предела



!!!!!!!!!!!!!!!!!!дописать проверку директорий
