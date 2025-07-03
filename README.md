# Project_template

Это шаблон для решения проектной работы. Структура этого файла повторяет структуру заданий. Заполняйте его по мере работы над решением.

# Задание 1. Анализ и планирование

<aside>

Чтобы составить документ с описанием текущей архитектуры приложения, можно часть информации взять из описания компании и условия задания. Это нормально.

</aside

### 1. Описание функциональности монолитного приложения

**Управление отоплением:**

- Пользователи могут…
- Система поддерживает…
- …

**Мониторинг температуры:**

- Пользователи могут…
- Система поддерживает…
- …

### 2. Анализ архитектуры монолитного приложения

Перечислите здесь основные особенности текущего приложения: какой язык программирования используется, какая база данных, как организовано взаимодействие между компонентами и так далее.

### 3. Определение доменов и границы контекстов

- Domain: User management
  - Subdomain: authentication and registration
    - Context: authentication
    - Context: registration
  - Subdomain: user profile management
    - Context: user profile
    - Context: password changes

- Domain: Device management
  - Subdomain: device lifecycle
    - Context: device registration
    - Context: device configuring
    - Context: device control
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

- …
- …
- …

Если вы считаете, что текущее решение не вызывает проблем, аргументируйте свою позицию.

### 5. Визуализация контекста системы — диаграмма С4

[Диаграмма контекста](https://www.planttext.com?text=TP51JyCm38Nl_HLcfo6nzSA9qz100WdGn9WuJYRrjaX972NkOFyUfwtA4EAKndxlvRExo899MkygiU88tZ7v1supmPA3q9V0dSLzGbzLmX64uOD5s4DZ4ncn7AhgmWRZseRQvE0W4lDDNIVydE-j7DeFpKgcP0MP6_RrgpMO6dwn5CdLo-lPoc6GpVDJxJ4B9Irjb-mZX-A81QrQKSeSfYNg2YORFIPwta8f0Ez03kVa6AFJHmhSvB9QdpJLJyTsVrVxZw4lbSZ-2pm6tDkm1pI6so3v2XewMaCPC3IG3GLCbhF63_dR-o-POhIQyNQmgPcjTAqdk5qzbbXjKWheoXrsd20cFjgiWEMH8NfaxRB8etN5Max88-4OHUSDvNWbDopexwYwiTmjQPGNzHzTuU-rl_YMZjkc6-KVNyywMPFkXcOTLvlLEUY7KJguNoBX0hxGYlxbRm00)


# Задание 2. Проектирование микросервисной архитектуры

В этом задании вам нужно предоставить только диаграммы в модели C4. Мы не просим вас отдельно описывать получившиеся микросервисы и то, как вы определили взаимодействия между компонентами To-Be системы. Если вы правильно подготовите диаграммы C4, они и так это покажут.

**Диаграмма контейнеров (Containers)**

[Диаграмма контейнеров](https://www.planttext.com?text=bLPBJnin4BxlhvXo2b8WbvvwuX6gLWKKI157v7WdYSkklR9dWQZYltSy-qv8WTF6zZo_R_mv9u6KfpBF4ZAK8Tmhd_zmPK0uTvQKiUXXQjJAgpn9o1L03XQEoEMG6e-QZBD9yiLOdPKfbZw3DL4HlaqcNZqVhmojomL7yvgZeQLZxVB9hT7Af-xQO87PvFphqInJbkwkBYUv2eIUjnxENLuu6psAM5oIpD07PqSnrXWExlXpmDzJY1lWba3hVl6gA3BE4gixE4pc6mwRZzhZQitkdKEr5KDMlo1NLgsCNO7IsfMMmXXIV38Q0oYRGj1ebJSkSFYaXUhXZ4rJvJSVoNK8VvC4Efn7zxWuBOfO0kTbBcPgXN3QwuIFVcyA3DgRWiPmYqgJe91bxZa8524I9BLZXCJufkfnLx8qqBJ5zGFqo-XwY23FqKVt6dAuaiWvymBrYRG1qEyZMdQ6ZMlUxiIIPnjQEpk6xypuwUod04_EOzK5f8hK65J9BLYgsvUoFQvC8DymEqWyNKZgwLcJCaPPg82Iq0LQUPpVNBwLIqAzRY4nkdPabdLsTkel8TJjx-a5RHe0SsKoOKIe-G_KyvgR3kvc1-Bbi74GUu335kADSMFxbl-UIYzIGnMofPKoZr9SSj3XY6_Zt4GNhDjKx-BTX0IMWwLPITxzyESO0e_CJObbHEIgMeAiOz1VQlcev59uPKFXF37McF6CaTy0Fl7e15Ww3ofih8R2Exu78KAnduYft9QEXchziRclR0UJl-E-XuNQBZDBr1lDTp_lHUbwYdZbpXf6isbZo4iLHrYfGxxBIThPrJIy9hLYFboyq4WL9aAyDZuzcl5RiO5cSbvOgwtAubfWhYCvkt2ixwATNEyIIQzxFTI9UXdaciI0yHjfUZ9f9Uzj2Z7X19bvGeuHQWNbT-4Mi_fHQEMJxtwGzw0rYqRryPOu7LofHxQEBMYLoMMDYUKH6yEV82hJSz_X-BC1TgxgXmDiosghTVmEf65oxmrjILhq6cfO0xL053aBB5IHAJdOasXB1iKtpa1blQizdxKVYCcWcT1Nbjf_zvRrXdxWFPpijtshwVue1RkrRscKI1BCoqNrHflMSpVpcvxy3yjecUiJ9eR_-Vm3).

**Диаграмма компонентов (Components)**

[Диаграмма компонентов Device Management Service](https://www.planttext.com?text=hLPBSzem4BxxLsnzIcO8N7hgAGcqaqn3Xm2T71aX2wE97gwqJkhfzBztPHlR40TefoVGQlVxzYrVUsGESwqYbAW4F36dxspk1Kp4Y-G25iALlsEhCsk4GPX8bZgcemXj1cXXRH6jXaGwmL5Q4qKVfE4gJqJk56mHC_zfD7BiTPXAtEPh0dVS6YIi8RTwD9USkSH-ao8JQZJ-U3LJpE3twSD8Cu_2aMZLi0-pu6iq9dicZN2hMvkRXBdYel5yKP2L7a3SnbA9ualu5G4qjXTLY5DcM2eqWPDD7NKhYqauAt1hpG2-a3yti_kurLDo8tZ1AN6wWu92qJzq1J2JWBP6edNIfF5bbtwohXsOtBQ02KEsPbwKjDPZwiJYyI6S5eGXF2Ij7i7zxgJYdyFPfQLESOqJS9rLfD3Yy4e6THBkA3n5Fb6vhQRuWXoS-94BZxwCtGkJU3BJEfoeMIhtwqJi4yv5AZqw5dge9bV2jUJTUsWLWYCtIjbN3w6p0WcvQQWNZv6H_KQcVJJLJNwIX-_fzL9Dcyht4RMtHrWs0lcsqqAxmlVJrCFQS7Gewgk0VvjxwXVlGTbKSjXOr_7b07kvQ-Lxar9LATH33cXKeD4vmTRCHszfPiw-I4yeFG51z_84IzPHFT83RoZs6-0uXnU81Ey79EEbmG2eOiC3lhd8h0y9BXvOKVP0Au5ILEuKAYqmpXkAQi2hvRNw_1ClM2P9RxcLBhcQqTukTfD8by8PLavcwLYz9gnPMrgk8LbX0AjkwgQ_0ww9bxR4Ooxoa8rfTOJo73YMZXcVMKUZtIuuyKBn-PAI-SBmaFKGG9NpA9eBTNoytwzvF6PAULZlPPr0MyWtGznNrsCm_GFwTfxEmsWwwR3SL6sM-D6JanWsU3N1RHXzmVybn7x8Pnk_Fzt_0MAld-AlRFFCO6apoNrjUiZHl8RxPEKUF8inZ4SyPSza5EQ0bqL3UpBPvzXrdiFtrQ_fkQFlapy0)

[Диаграмма компонентов Scenario Planning Service](https://www.planttext.com?text=ZLJ1Jjj04BtxAwO-1Gd8fQUUW8IgLG51t8eZcjWJPzNrhZKxXbfL_xspjkCuDBGz9HxlUpDltbjV146MfhA96B44ZyZL9zy4WYKzcvmW8-v-5xwglICdi3HOCbP98hu6yR3s8hw2mZ3bOhnBadV6vROfg64BMv4wV9ZF6L_EIoFRPgtad7idodMU-sg-CZbouUyCrMJdY_TdznQTVBkzcLSOX5XBJsFtyphEcYmKZyOHFrtvnXN8xMoSF6iLLPr2kjVIbz8J-9a0ZDXPbfD3DZusDAvKoAu2GsadFzLtzwrilJk5ZphLvVtdMBekZ02w0hXn47MT5RHHwWB2G1JIasdBvNfikhoQzYjGS8sXR-I3b4pPmqryoiGpXP6mEwcalvAaL_Lq_KDc5OM09Jqqr91YRlj7w9uZoLT65shF4a38KaN2BT2pBZJ0nZDWQ5qEDVjSaQfR6qpO-oYePcKQOX4LiRSmB28ZLmHGDokCVpGLHNSk71BTUJ4RjJl6H57Jn-ccUpQgqDYEAsusCYL_isuOx1QTAgzKsJ7FTWaOqZJIH2Cz3w8iyTIQ_XtiNqRYIslzI-WcKwd1b6vqQ73yU8j1vH7-YVwhHZrG8y3wqkITGQFzUdCsfcouDsdQwBBHQzZjyjgLYezJZYMWhXRPL__AwevmHRKFSRRs1jjk9_iATAL8jzGy0kRvE6yVpcH5zktr7bzAka2hZgyFv2jTfFf3tK7aqo-u-OwGDUkGiwdZiRTmC4tpOMxVXBpARKI1czH2UdfoHF1Er-j5wXwn2FD7Dg8tUxZGHpl_D_BrmSbNvX3J9xO79XSgHB-dlm40)

[Диаграмма компонентов User Management Service](https://www.planttext.com?text=lLJFRzfG3Bxdh_0uKQc3oquxjOL9dKGh1gfwH2OnuKdlH-Rdh4FJ_lVvXG0XHHMddQ8uzlVv-spdBWgorCvcOiGIl2Axnr17WYdzCZd1ahXvJeAhWYSlC3LOCheiar2115W7aU2WC4ovcE2px9FnkQqBgjd2LgIANyTZnhTHQMHRhnMSy-15iKPvSEE5oP6By6oe8ZkUVFayj-ZbvMasTXY5M4Eh8_keIhrc4wr7uubN3w7s1V9kUEnykTCgTmk3avPzQ703VpA0O-tmHJjvGeybEONMYXI0K-GWVg2VbXAO8gJceK31My1QjfgatIVLWBu0fj94uIOmkEboJTSDs_JXm98mrXWRx7c8KZ8jVymkCIdGtopRIrXz-ot3vo1cqz9gVlVrh6FoHGHoQ6nCSqg0KS6o_sP0QtSxkk7z_7kYvc0jiIBgEvm2YUDHCQoIwFu4Ptm9AONfPqrHOcle4UsC_TuNYmvtstSYUTzaDx6hyA6EwagCO4DfSjW4ldB6XvQIUtCE6sFfr41ZQHljiXsqDeOQlmb0XP4aEh5K6EDRu0BoBVgI-k8NL8LeT2Ax6UuQCqyHQ4A9OgfZ0ippewRzAcKBihrXN6NcO89MLsbzPfD2leUxOCI7nLUDigzP9MCHnwziH6riBoN1NHh3rSNznFPgp_ExjtczWDxTxkzJ_uGRmsw_NysnVg3Y8a9lLS1tajAvPtUQfd_DVm00)


**Диаграмма кода (Code)**

[Диаграмма кода Device Management](https://www.planttext.com?text=ZL9DZnCn3BtdLvYUMA0Ta3YDLjMYhX0hRH6Y88uhRsAcblAbn5DK8VuxoRJJJYiEN2Rni_F6VdvtMJ19xwmI5alm0vFx5FfCS4yxrWHhzDYH8o-m2gR0Z5r2fvI421BWEOW41uOJQU7WbNh1NjlUK9yiR4LYRficuQz5nxBjdmjrqi5B8Lpeu9glh36Py9afacrMx-TVB7hvldvi76QXLA2dLN0n-FeYrawLjfZpsE1l1V1w8ubz1psRIUJHqIGqb7NYE3HvHctGE49hZBTvWD_0uLn29f5ooJN_o5bkDvey9WwvvCPhJUu26qXKwb_Ud693beGcG2nSXx2F1akgQF6Jk_OupMg8RbgenUhFEEgtGkD8qluU1VyryKSRK627jfzEN9-mdbPxbXeM6X9s1FLJ7E3Y1LfMIRmZyuHoxk4qz_yhNcOpF8exYFTXyCWIyE2L4_a1lsQ6IIZxUBdCAjU3kLuR-lqI8XQ75jrJ7XWUYdVB8d2_eTfHhhyzccVsRWRp-N1SQjp25lDrrTl5ujLi8aGBHwjdTGPFb4FnSR03dReZRug3_m80)

[Telemetry Flow via Message Queue (Sequence Diagram)](https://www.planttext.com?text=dPDDJiD038NtSmglKBgesBD0hTeYka02MedraBYffVa9CvwWik8Et92JuFuGcZOjY4qYZT_xx97V32BhmCaQnSG6uKa7U-jJHFXy_u0v6hJ8OGKtnhz2JHhkC4PT8ZmaJ0ZP35yIkXnXJBeCslQKqZdx06EiAKTL2ProghJZ7zhKbHYPl9jXE5Bj6cpuhS8miRTwRPkuaboxk6ttY9MF9ErN7SMHTnoy6TvFbTgUGF_wz51m1H5TqTIpGhFkgTDwWHrE8OnQ6n8dRajPiVbDYvuwqlP_cMP3Wajmdc7XaokKEZ_DEPZpmGhl3U42q0NAb_-y7xc8WHlNM21_8UrlMIXLUZOKburbKgFZ3DTVILHBBER390Y0MqvrfEWUtdXTDE5OKBctdYv2Hr-KhIHPxpnGMMA8MRVpC86xS8syjTeLcJmPaNzdOa_MM4yOr40Erw_t2m00)

# Задание 3. Разработка ER-диаграммы

[ER-диаграмма](https://www.planttext.com?text=XLJRIWCn47tVhvX75Ve3HQH2bOe8KYq-bY4xjYEvb6HQALRm7_n3lyHaDxIxszM-XEoPoPcJCvCT1K4lQwCBOT44B-ZDnAq3mS_NDznCOSouy6ZWR4mRLWGFQ751XgoS5qLSMROmSORWem2uW3MNC8JPx6uCbvUFzrTN4HqCuX8f_RmPlAs3sYaKTZO6DkZL4dq4BKR20_1Px4lD8isfKcIGTOllbNsGUM9jeXfxm1M6yEvyES6mR2d80gREcLC2bj6FUDVkLRkbPBkYlXBPwHD5V1JIPsZ7Eu2IWlAyEZ8va0ZRHOZWMt2s8U2PTEom-EqO1REElsIKbTW-8Oc1LQla1lKwYNlL3YKDXMLf9GWRYXDfLX4jKIXzfxkI8jvGEKTf1WwAdnHPzEnEcVQtsYFRbBCbTqmx5BnMLUX_Rq9MrLSlDR_JfhQqQXRZooCXl-zHIjEudGTAyXBCLfAiwbtiTeE1-wYVun2M68fgc-5gSeVWtcrHRJESfwtEpnyvj7UrFjK8xdQT8QapzWSoGNQfvYv6PClqf_a5)

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