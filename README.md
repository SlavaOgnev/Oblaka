# DEVOPS ЛАБЫ
Команда "Академ бойцы" - Гайдаренко Никита, Гриндий Екатерина.

# Лабораторная работа 1

Пользуясь терминалом на компьютере А перенести файл с компьютера Б на компьютер С, находящиеся в одной локальной сети. (Подсказка: вам понадобится ssh). Просьба использовать MacOS/Linux/WSL.

**Выполнение лабораторной работы**:

1. Убедились, что все три компьютера находятся в одной локальной сети и имеют соединение друг с другом. Для этого на компьютерах MacOS активировали SSH-сервер, который установлен и включен по умолчанию. И также его активировали и на компьютере Windows (начиная с Windows 10, OpenSSH поставляется в качестве опциональной функции).
2. Узнали IP-адрес всех компьютеров в локальной сети. Для этого напишем на каждом команду ```ifconfig``` для MacOs и ```ipconfig``` для Windows.
<img src="https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A42.jpg">
![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A42.jpg)
<img scr="https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A29.jpg">
![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A29.jpg)
<img scr="https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A44.jpg">
![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A44.jpg)
4. Установили соединения компьютеров А и Б. Для этого в командной строке компьютера А ввели команду ```ssh ekaterina@192.168.0.102``` . Вводим пароль для компьютера А
5. С помощью команды``` scp kateg@192.168.0.105:/home/kateg/Desktop/privet.txt /Users/ekaterina/Desktop``` перенесли файл с компьютера Б на компьютер С.
<img scr="https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A31.jpg">
![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A31.jpg)

Фаил успешно перенесен)
<img scr="https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A46.jpg">
![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A46.jpg)
