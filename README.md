# Project_template

# Задание 1. Анализ и планирование

### 1. Описание функциональности монолитного приложения

**Управление отоплением:**

- Пользователи могут управлять отоплением
- Система поддерживает подключение датчиков к системе с помощью специалистов
- Пользователь не может подключить датчик к системе самостоятельно

**Мониторинг температуры:**

- Пользователи могут проверять температуру в доме

### 2. Анализ архитектуры монолитного приложения

Архитектура приложения представляет из себя монолит на GO с СУБД Postgres. Все запросы обрабатываются синхронно.
Все запросы идут от сервера к датчику, например что бы получить данные о температуре сервер делает запрос к датчику.

### 3. Определение доменов и границы контекстов

- Domain: User management
  - Subdomain: authentication and authorization
    - Context: authentication
    - Context: authorization
  - Subdomain: user profile management
    - Context: user profile

- Domain: Device management
  - Subdomain: device lifecycle
    - Context: device provisioning
    - Context: device registration
    - Context: device configuring
  - Subdomain: monitoring and telemetry
    - Context: telemetry ingestion
	- Context: realtime monitoring 
    - Context: alerting and notification

- Domain: Scenario planing
  - Subdomain: scenario design
    - Context: scenario editor
  - Subdomain: scenario execution
    - Context: automation engine	

### **4. Проблемы монолитного решения**

- длительный цикл разработки и внедрения новой функциональности
- текущее решение плохо масштабируется
- разработка текущего решение имеет повышенный риск возникновения ошибок в следствии чего будут повышаться косты на тестирование
- для подключение нового датчика требуются специалисты
- разработка монолитного приложение будет со временем увеличивать время выхода на рынок новых версий

### 5. Визуализация контекста системы — диаграмма С4

Добавьте сюда диаграмму контекста в модели C4.

Чтобы добавить ссылку в файл Readme.md, нужно использовать синтаксис Markdown. Это делают так:

```markdown
[Диаграмма контекста](https://www.planttext.com?text=TP51JyCm38Nl_HLcfo6nzSA9qz100WdGn9WuJYRrjaX972NkOFyUfwtA4EAKndxlvRExo899MkygiU88tZ7v1supmPA3q9V0dSLzGbzLmX64uOD5s4DZ4ncn7AhgmWRZseRQvE0W4lDDNIVydE-j7DeFpKgcP0MP6_RrgpMO6dwn5CdLo-lPoc6GpVDJxJ4B9Irjb-mZX-A81QrQKSeSfYNg2YORFIPwta8f0Ez03kVa6AFJHmhSvB9QdpJLJyTsVrVxZw4lbSZ-2pm6tDkm1pI6so3v2XewMaCPC3IG3GLCbhF63_dR-o-POhIQyNQmgPcjTAqdk5qzbbXjKWheoXrsd20cFjgiWEMH8NfaxRB8etN5Max88-4OHUSDvNWbDopexwYwiTmjQPGNzHzTuU-rl_YMZjkc6-KVNyywMPFkXcOTLvlLEUY7KJguNoBX0hxGYlxbRm00)
```

# Задание 2. Проектирование микросервисной архитектуры

В этом задании вам нужно предоставить только диаграммы в модели C4. Мы не просим вас отдельно описывать получившиеся микросервисы и то, как вы определили взаимодействия между компонентами To-Be системы. Если вы правильно подготовите диаграммы C4, они и так это покажут.

**Диаграмма контейнеров (Containers)**

Добавьте диаграмму.

**Диаграмма компонентов (Components)**

Добавьте диаграмму для каждого из выделенных микросервисов.

**Диаграмма кода (Code)**

Добавьте одну диаграмму или несколько.

# Задание 3. Разработка ER-диаграммы

Добавьте сюда ER-диаграмму. Она должна отражать ключевые сущности системы, их атрибуты и тип связей между ними.

# Задание 4. Создание и документирование API

### 1. Тип API

Укажите, какой тип API вы будете использовать для взаимодействия микросервисов. Объясните своё решение.

### 2. Документация API

Здесь приложите ссылки на документацию API для микросервисов, которые вы спроектировали в первой части проектной работы. Для документирования используйте Swagger/OpenAPI или AsyncAPI.

# Задание 5. Работа с docker и docker-compose

Перейдите в apps.

Там находится приложение-монолит для работы с датчиками температуры. В README.md описано как запустить решение.

Вам нужно:

1) сделать простое приложение temperature-api на любом удобном для вас языке программирования, которое при запросе /temperature?location= будет отдавать рандомное значение температуры.

Locations - название комнаты, sensorId - идентификатор названия комнаты

```
	// If no location is provided, use a default based on sensor ID
	if location == "" {
		switch sensorID {
		case "1":
			location = "Living Room"
		case "2":
			location = "Bedroom"
		case "3":
			location = "Kitchen"
		default:
			location = "Unknown"
		}
	}

	// If no sensor ID is provided, generate one based on location
	if sensorID == "" {
		switch location {
		case "Living Room":
			sensorID = "1"
		case "Bedroom":
			sensorID = "2"
		case "Kitchen":
			sensorID = "3"
		default:
			sensorID = "0"
		}
	}
```

2) Приложение следует упаковать в Docker и добавить в docker-compose. Порт по умолчанию должен быть 8081

3) Кроме того для smart_home приложения требуется база данных - добавьте в docker-compose файл настройки для запуска postgres с указанием скрипта инициализации ./smart_home/init.sql

Для проверки можно использовать Postman коллекцию smarthome-api.postman_collection.json и вызвать:

- Create Sensor
- Get All Sensors

Должно при каждом вызове отображаться разное значение температуры

Ревьюер будет проверять точно так же.


# **Задание 6. Разработка MVP**

Необходимо создать новые микросервисы и обеспечить их интеграции с существующим монолитом для плавного перехода к микросервисной архитектуре. 

### **Что нужно сделать**

1. Создайте новые микросервисы для управления телеметрией и устройствами (с простейшей логикой), которые будут интегрированы с существующим монолитным приложением. Каждый микросервис на своем ООП языке.
2. Обеспечьте взаимодействие между микросервисами и монолитом (при желании с помощью брокера сообщений), чтобы постепенно перенести функциональность из монолита в микросервисы. 

В результате у вас должны быть созданы Dockerfiles и docker-compose для запуска микросервисов. 