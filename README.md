# DEVOPS ЛАБЫ
Команда "Академ бойцы" - Гайдаренко Никита, Гриндий Екатерина.

# Лабораторная работа 1

Пользуясь терминалом на компьютере А перенести файл с компьютера Б на компьютер С, находящиеся в одной локальной сети. (Подсказка: вам понадобится ssh). Просьба использовать MacOS/Linux/WSL.

**Выполнение лабораторной работы**:

1. Убедились, что все три компьютера находятся в одной локальной сети и имеют соединение друг с другом. Для этого на компьютерах MacOS активировали SSH-сервер, который установлен и включен по умолчанию. И также его активировали и на компьютере Windows (начиная с Windows 10, OpenSSH поставляется в качестве опциональной функции).
2. Узнали IP-адрес всех компьютеров в локальной сети. Для этого напишем на каждом команду ```ifconfig``` для MacOs и ```ipconfig``` для Windows.

![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A42.jpg)
![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A29.jpg)
![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A44.jpg)

4. Установили соединения компьютеров А и Б. Для этого в командной строке компьютера А ввели команду ```ssh ekaterina@192.168.0.102``` . Вводим пароль для компьютера А
5. С помощью команды``` scp kateg@192.168.0.105:/home/kateg/Desktop/privet.txt /Users/ekaterina/Desktop``` перенесли файл с компьютера Б на компьютер С.


![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A31.jpg)

Фаил успешно перенесен)


![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A26%3A46.jpg)

# Лабораторная работа 2
Написать два Dockerfile – плохой и хороший. Плохой должен запускаться и работать корректно, но в нём должно быть не менее 3 “bad practices”. В хорошем Dockerfile они должны быть исправлены. В Readme описать все плохие практики из кода Dockerfile и почему они плохие, как они были исправлены в хорошем  Dockerfile, а также две плохие практики по использованию этого контейнера.

**Выполнение лабораторной работы:**

Плохой Dockerfile:
### Плохой Dockerfile
+ Использование latest версии
  
  Версия не зафиксирована, что может привести к ошибкам, которые будут возникать из-за нововведений
+ Несколько команд RUN

  Это создает несколько слоев в контейнере, увеличивает объем
+ Копирование всех файлов из папки, используя `COPY . .`

  Лучше указывать конкретно нужные файлы, чтобы избежать ненужного увеличения размера образа

![Bad](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A27%3A29.jpg)

### Хороший Dockerfile
+ Теперь указана точная версия python, что обеспечивает стабильность сборки
+ Команда RUN только 1. Так будет создан всего один слой, docker-образ станет меньшего размера и будет содержать в себе все необходимое (как и в первом варианте)
+ При копировании указаны только те файлы, которые действительно нужны, а значит образ не будет забит ненужными файлами, если они случайно попадут в папку

![good](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A27%3A32.jpg)

Однако и у этого контейнера остались недостатки:

-Рекомендуется указывать рабочую директорию с помощью команды WORKDIR, чтобы операции внутри контейнера были более предсказуемыми

-Не указаны версии зависимостей при установке пакетов через pip. Рекомендуется указывать конкретные версии зависимостей для обеспечения стабильности и предотвращения возможных проблем совместимости в будущем.

### Проверяем корректность работы Dockerfile for good and bad
#### Для плохого докерфайла
1) __С помощью команды `docker build .` создаем образ__

![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A27%3A37.jpg)

2) __С помощью команды `docker images` смотрим ID образа, чтоб его запустить__

![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A27%3A38.jpg)

#### Для хорошего докера

![создание образа](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A27%3A40.jpg)

![запуск](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A27%3A41.jpg)

### Сравнение размеров файлов
![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A27%3A47.jpg)

Как мы видим хороший докерфаил занимает меньше места по сравнению с плохим.

Ипольззованый python код

![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/IMAGE%202024-04-11%2015%3A27%3A45.jpg)

 # ЛАБОРАТОРНАЯ РАБОТА №3
 
*Задание: сделать, чтобы после пуша в ваш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь. (например, если результат - текстовый файлик, он должен автоматически сохраниться на локальную машину, в ваш репозиторий или на ваш сервер).*
 
 ### ВЫПОЛНЕНИЕ РАБОТЫ:

Создадим отдельный репозиторий, где будет создаваться докер образ [ссылка на репозиторий](https://github.com/SlavaOgnev/lab3)
 
 1. Возьмем программу написанную на языке python(dvk.py) и сделаем так, чтобы ее вывод происходил в текстовый файл(dvk.txt).
 
 dvk.py:
 
 ![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-04-11%20%D0%B2%2015.32.24.png)

2. Создадим docker файл, для запуска тестов:

![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-04-11%20%D0%B2%2015.33.05.png)

 4. Создадим секреты в виде имени и пароля пользователя, чтоб подключиться к dockerhub:

![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-04-11%20%D0%B2%2015.33.48.png)

5. Создадим файл docker-build.yml, в котором будут задействованы наши секреты секреты, чтобы войти:

![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-04-11%20%D0%B2%2015.34.29.png)

6. Смотрим прошло ли тесты:

![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-04-11%20%D0%B2%2015.35.00.png)

![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-04-11%20%D0%B2%2015.35.23.png)

6. Проверяем dockeкhub

![](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-04-11%20%D0%B2%2015.36.43.png)

---

# Аналитическая работа №1

### Цель работы 
Знакомство с облачными сервисами. Понимание уровней абстракции над инфраструктурой в облаке. Формирование понимания типов потребления сервисов в сервисной-модели. Сопоставление сервисов между разными провайдерами. Оценка возможностей миграции на отечественные сервисы.

### Дано
Слепок данных биллинга от провайдера после небольшой обработки в виде SQL-параметров. Символ % в начале/конце означает, что перед/после него может стоять любой набор символов.

![начальные данные AWS](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%9D%D0%B0%D1%87%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_AWS.png)

### Описание сервисов


**APNFee** (Amazon Partner Network) – это международная партнерская программа, участники которой могут получить доступ к программам AWS. С помощью него партнёры могут запросить коммерческую или маркетинговую поддержку.

---

**AmazonAppStream** - это сервис, который позволяет централизованно управлять приложениями для рабочего стола и безопасно доставлять их на любой компьютер. 
   1. Stream - это функция Amazon AppStream, которая позволяет пользователям получать доступ к своим приложениям в режиме реального времени без необходимости устанавливать их на своем устройстве. Stream также позволяет пользователям управлять своими приложениями, обновлять их и удалять их с устройства.
   2. Win-User - это функция, которая позволяет пользователям запускать Windows-приложения в облаке и использовать их на любом устройстве. Эта функция позволяет пользователям получить доступ к своим рабочим столам и приложениям с любого устройства, подключенного к Интернету, без необходимости установки приложений на каждом устройстве.

---

**AmazonAthena** -  это сервис запросов, который обеспечивает анализ данных, хранящихся в хранилище Amazon S3, с применением стандартного SQL. Для использования сервиса Athena необходимо указать данные, хранящиеся в Amazon S3, задать соответствующую схему и выполнять запросы, используя стандартные средства SQL.
    
---

**AmazonCloudDirectory** - это полностью управляемый специальный облачный каталог. Позволяет легко сохранить иерархические связи данных по множеству направлений, создавать гибкие облачные каталоги для организации иерархических связей данных по множеству направлений.
  1. Amazon Cloud Directory Requests-Tier1 - это уровень обслуживания запросов для высокопроизводительных операций в Amazon Cloud Directory. Этот уровень предлагает более высокую пропускную способность и меньшее время отклика по сравнению с другими уровнями.
  2. Amazon Cloud Directory Requests-Tier2 - это уровень обслуживания, который предлагает средний уровень обслуживания, с меньшим количеством поддержки и более медленным временем отклика.

---

**AmazonDocDB** - Amazon DocumentDB это полностью управляемая база данных, совместимая с MongoDB, предоставляемая Amazon Web Services (AWS). Эта служба предназначена для хранения, запросов и анализа данных, организованных в формате документов, аналогично тому, как это делается в MongoDB. Amazon DocumentDB предлагает высокую доступность, масштабируемость и безопасность, а также обеспечивает совместимость с существующими приложениями и инструментами, разработанными для работы с MongoDB.
  
---

**AmazonEI** - это сервис, который позволяет добавлять ускорение глубокого обучения к вашим приложениям на базе Amazon EC2. С Elastic Inference вы можете присоединить графические процессоры (GPU) к вашим экземплярам EC2 и использовать их для ускорения выполнения интенсивных вычислений глубокого обучения, не создавая и не управляя собственными кластерами GPU. Это позволяет сократить затраты на вычислительные ресурсы и упростить развертывание приложений глубокого обучения в облаке AWS.
  
---

**AWSIoT** - это сервис, который позволяет подключать устройства к облачной инфраструктуре и взаимодействовать с ними. AWS IoT обеспечивает безопасную и масштабируемую инфраструктуру для управления подключенными устройствами, сбора данных с них, аналитики и автоматизации действий на основе этих данных. Этот сервис предназначен для поддержки проектов, связанных с интернетом вещей (IoT), включая умный дом, индустриальные системы, здравоохранение и многое другое.
  
---

**IoTDeviceManagement** - это облачный сервис, который обеспечивает возможность централизованного управления подключенными устройствами IoT. Этот сервис позволяет развертывать, регистрировать, мониторить и удаленно управлять множеством устройств из одного места. С его помощью можно легко управлять жизненным циклом устройств, включая настройку, обновление программного обеспечения, мониторинг состояния и управление правами доступа. Все это способствует эффективной работе и безопасности системы IoT.

---

**AWSCodePipeline** - это сервис, который позволяет автоматизировать процесс сборки, тестирования и развертывания вашего программного обеспечения. CodePipeline позволяет создавать цепочки (pipelines), состоящие из этапов обработки, которые могут быть настроены для автоматического выполнения действий, таких как получение исходного кода из репозитория, сборка приложения, проведение автоматических тестов и развертывание изменений в производственную среду. Этот сервис помогает ускорить и упростить процесс разработки и доставки программного обеспечения, обеспечивая надежность и согласованность в каждом этапе.

---

**AWSXRay** - это сервис, который позволяет разработчикам анализировать и отлаживать распределенные приложения, идентифицируя и устраняя проблемы производительности и ошибки в коде.
С помощью AWS X-Ray можно получить подробное представление о том, как взаимодействуют компоненты вашего приложения, идентифицировать узкие места и оптимизировать его работу. Сервис предоставляет информацию о времени выполнения запросов, трассировках запросов через различные службы и микросервисы, а также о проблемах и ошибках, возникающих в процессе выполнения приложения. AWS X-Ray интегрируется с множеством сервисов AWS и сторонних приложений, обеспечивая полный обзор процесса работы вашего приложения в облачной среде. 

---

**CodeBuild** - это управляемый сервис сборки, который позволяет автоматизировать процесс сборки, тестирования и публикации кода. Он интегрируется с другими сервисами AWS, такими как AWS CodeCommit, AWS CodePipeline и AWS CodeDeploy, обеспечивая непрерывную интеграцию и непрерывное развертывание (CI/CD) вашего приложения.

---

**AmazonML** - это сервис машинного обучения, который позволяет разработчикам легко использовать и интегрировать в существующие или новые продукты и решения. AmazonML API позволяет разработчикам значительно упростить добавление интеллекта в любое приложение с помощью набора сервисов, которые предлагают функции речи, языкового анализа, видения и чат-бота. Они также поддерживаются мощным сервисом шифрования, обеспечивающим хранение и безопасность данных.

---

**AmazonPolly** - это сервис преобразования текста в речь, который использует передовые технологии генерации речи на основе искусственного интеллекта, чтобы создавать естественно звучащий речевой вывод из текстовых данных.
С помощью Amazon Polly пользователи могут создавать аудиозаписи на различных языках и с различными голосами, а также настраивать тон, скорость и интонацию речи. Этот сервис может быть использован для создания аудиоконтента для различных приложений, таких как аудиокниги, текстовые новости, инструкции по использованию и другие, а также для создания голосовых уведомлений и динамического контента для веб-сайтов и приложений.

---

**AmazonPersonalize** - это сервис семейства Machine Learning, который позволяет разработчикам легко добавлять индивидуализированные рекомендации для клиентов, которые используют их приложения. Amazon Personalize не требует большого опыта машинного обучения. Вы можете строить и тренировать модель обучения с помощью консоли AWS или программно с помощью AWS SDK.

---

**AmazonRekognition** - это сервис, который позволяет легко добавлять изображения и анализ видео в ваши приложения. Вы просто предоставляете изображение или видео для Amazon Rekognition API, и сервис может идентифицировать объекты, людей, текст, сцены и мероприятия. Он также может обнаружить любой неприемлемый контент.

---

**AmazonEC2**  -  это веб-сервис, который предоставляет масштабируемые вычислительные ресурсы в облаке. С помощью EC2 пользователи могут арендовать виртуальные серверы (инстансы), на которых можно запускать приложения и выполнять различные вычислительные задачи.

---

![начальные данные AWS](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82_AWS.png)

### Вывод
В ходе выполнения данной работы мы ознакомились с сервисами Amazon, а также провели сравнение и сопоставили сервисам Amazon сервисы Yandex Cloud. Аналоги были найдены не для всех сервисов. Вывод: миграция возможна, однако в том случае, когда аналоги сервисов Amazon в Yandex Cloud полностью покрывают требуемые функции.

---

# Аналитическая работа №2

### Цель работы

Знакомство с облачными сервисами. Понимание уровней абстракции над инфраструктурой в облаке. Формирование понимания типов потребления сервисов в сервисной-модели. Сопоставление сервисов между разными провайдерами. Оценка возможностей миграции на отечественные сервисы.

### Дано
Слепок данных биллинга от провайдера после небольшой обработки в виде SQL-параметров. Символ % в начале/конце означает, что перед/после него может стоять любой набор символов.
![начальные данные Azure](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%9D%D0%B0%D1%87%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_Azure.png)

### Описание сервисов

---

Azure Analysis Services — это полностью управляемый сервис анализа данных в облаке, предоставляемый платформой Microsoft Azure. Он предоставляет средства для создания, моделирования и анализа многомерных и реляционных данных, а также для создания отчетов и визуализаций на основе этих данных.

---

Database Azure for PostgreSQL — это управляемая база данных на основе открытого исходного кода PostgreSQL, предоставляемая Microsoft Azure. Он предлагает высокую доступность, масштабируемость и безопасность, а также обеспечивает простоту в использовании и управлении базой данных.

---

Azure Databricks — эдиная, открытая платформа аналитики для создания, развертывания, совместного использования и обслуживания корпоративных данных, аналитики и решений искусственного интеллекта в масштабе. Платформа аналитики данных Databricks интегрируется с облачным хранилищем и безопасностью в облачной учетной записи, а также управляет и развертывает облачную инфраструктуру от вашего имени.

---

Azure Monitor — Это журнал платформы в Azure, который предоставляет когнитивные аналитические сведения о событиях уровня подписки. Журнал действий включает информацию, например, об изменении ресурса или запуске виртуальной машины. Вы можете просмотреть журнал действий на портале Azure или получить записи с помощью PowerShell и Azure CLI.
  1. Azure Monitor Notifications - это функция, которая позволяет автоматизировать отправку уведомлений о важных событиях и состоянии ресурсов в облачной среде. С помощью этой функции можно настроить отправку уведомлений по электронной почте, SMS или push-уведомлений в приложении, когда происходят определенные события, такие как : ошибки в работе приложений, превышение пороговых значений показателей производительности и другие изменения в состоянии ресурсов.
  2. Azure Monitor Notifications Webhook - это механизм, который позволяет автоматически вызывать HTTP-запрос при наступлении определенного события.
  3. Azure Monitor Notifications Email - это функция, позволяющая автоматически отправлять уведомления о различных событиях в облачной платформе Microsoft Azure на указанный адрес электронной почты.

---

Azure  Virtual Machines — один из нескольких типов запрашиваемых масштабируемых вычислительных ресурсов, которые предоставляет Azure. Обычно виртуальную машину выбирают, когда требуется более строгий контроль за вычислительной средой, чем в других вариантах.
  
---

Azure Virtual Network — это служба, которая обеспечивает фундаментальный строительный блок для вашей частной сети в Azure. Экземпляр службы (виртуальная сеть) позволяет многим типам ресурсов Azure безопасно взаимодействовать друг с другом, Интернетом и локальными сетями. К таким ресурсам Azure относятся виртуальные машины.

---

Azure Load Balancer — это сервис балансировки нагрузки, который обеспечивает распределение трафика между несколькими виртуальными машинами в облаке Azure.
Основная функция Azure Load Balancer - обеспечить высокую доступность и масштабируемость приложений, обрабатывая входящий трафик и распределяя его между экземплярами приложения, работающими на виртуальных машинах в одной или нескольких зон облака. Это позволяет распределить рабочую нагрузку и обеспечить отказоустойчивость приложений.

---

Azure SignalR — ээто управляемый сервис, который позволяет разработчикам быстро добавить в реальном времени функциональность в свои приложения. С помощью SignalR разработчики могут легко создавать приложения, которые поддерживают мгновенную обратную связь между клиентами и сервером.

---

Azure Event Grid   — это управляемый сервис, который обеспечивает масштабируемую и надежную доставку событий в приложения и услуги в облаке Azure. Он позволяет создавать архитектуры, реагирующие на различные события и реализующие асинхронную связь между различными компонентами системы.

---

Media Services - Облачная платформа, которая позволяет создавать решения для потоковой передачи видео широковещательного уровня. Она повышает доступность и уровень распространения, дает возможность анализировать содержимое и предоставляет многие другие функции. Службы мультимедиа позволяют создавать приложения для обработки данных мультимедиа высокого качества для крупных аудиторий на самых популярных современных мобильных устройствах и браузерах для всевозможных сфер деятельности. Их могут использовать как разработчики приложений и центры обработки вызовов, так и государственные учреждения или компании, работающие в индустрии развлечений.

---

Azure IoT Hub — Это коллекция облачных служб, пограничных компонентов и пакетов SDK, управляемых корпорацией Майкрософт, которые позволяют подключать, отслеживать ресурсы Интернета вещей и управлять ими в большом масштабе. Проще говоря, решение Интернета вещей состоит из устройств Интернета вещей, которые взаимодействуют с облачными службами.

---

Azure SQL Data Warehouse — это эластичное хранилище данных как услуга с функциями корпоративного уровня на основе архитектуры массово параллельной обработки SQL Server.

---

Azure Storage Platform - это облачное решение Microsoft для хранения данных в современных сценариях. Azure Storage предлагает высокодоступное, масштабируемое, надежное и безопасное хранилище для различных объектов данных в облаке.

![Конечные данные Azure](https://github.com/SlavaOgnev/Oblaka/blob/main/screens/%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82_Azure.png)

### Вывод
В ходе выполнения данной работы мы ознакомились с сервисами Azure, а также провели сравнение и сопоставили сервисам Azure сервисы Yandex Cloud. Аналоги были найдены не для всех сервисов. Вывод: миграция возможна, однако в том случае, когда аналоги сервисов Azure в Yandex Cloud полностью покрывают требуемые функции.
