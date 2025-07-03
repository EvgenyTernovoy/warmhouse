# Project_template

Это шаблон для решения проектной работы. Структура этого файла повторяет структуру заданий. Заполняйте его по мере работы над решением.

# Задание 1. Анализ и планирование

<aside>

Чтобы составить документ с описанием текущей архитектуры приложения, можно часть информации взять из описания компании и условия задания. Это нормально.

</aside

### 1. Описание функциональности монолитного приложения

**Управление отоплением:**

- Пользователи могут удалённо включать/выключать отопление в своих домах.

**Мониторинг температуры:**

- Система получает данные о температуре с датчиков, установленных в домах. 
- Пользователи могут просматривать текущую температуру в своих домах через веб-интерфейс.

### 2. Анализ архитектуры монолитного приложения

Язык программирования: Go
База данных: PostgreSQL
Архитектура: Монолитная, все компоненты системы (обработка запросов, бизнес-логика, работа с данными) находятся в рамках одного приложения.
Взаимодействие: Синхронное, запросы обрабатываются последовательно.
Масштабируемость: Ограничена, так как монолит сложно масштабировать по частям.
Развертывание: Требует остановки всего приложения.

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

- Domain: Scenario planing
  - Subdomain: scenario design
    - Context: scenario editor
  - Subdomain: scenario execution
    - Context: automation engine
    - Context: alerting and notification

### **4. Проблемы монолитного решения**

- …
- …
- …

Если вы считаете, что текущее решение не вызывает проблем, аргументируйте свою позицию.

### 5. Визуализация контекста системы — диаграмма С4

[Диаграмма контекста](https://www.planttext.com?text=TLB1JiCm3BttAynEGzhM2oTEe8444g09c3WYatfhf2IE4dUmlyTffx9fub8tplFpUq-voO99EkygiU88FZ3v1-uomPA3q8_0dSLjGbzLmX64uOj5s4DZ4ncn7AhgmWRZkeQwvA0LYVcwhXD-BxPMskvBkP8fN44MXdtzQWscXbyiHNBrycg-SXXa_VnKUyn2ILkVI_QHGvc8HLgrefGvJ0lL32PhBHEjjr0Qm1kGzbWvnkXqIH4tkQpUzihgf-FrSDRnlu6XLIY7F_0OS6l35j0OxeBa6JIqiuOoO6WW6mgOB6UbF_1_tl_85ADLZlVMfcQ-qbZtSBjwBBHwIIcWAsVOS8AOU6Up2YnB1kePR4XC2qAEF4dQ3wj8FngRAchowARVHXwjA-IbGXuzZCle-4ALlf8xH7WUXcQQ-nX7U46VuOh30NlYOEcuQtgp_ymDMYTlnGtDUrrTria3_c2b5tS24Yx2RxIZx-0N)


# Задание 2. Проектирование микросервисной архитектуры

В этом задании вам нужно предоставить только диаграммы в модели C4. Мы не просим вас отдельно описывать получившиеся микросервисы и то, как вы определили взаимодействия между компонентами To-Be системы. Если вы правильно подготовите диаграммы C4, они и так это покажут.

**Диаграмма контейнеров (Containers)**

[Диаграмма контейнеров](https://www.planttext.com?text=bLR9RXin3BtFLx0vEO1JNthgASvIj6XJE76370DvXhRLQgI1n4bY5FdtKfpTI-ESnfB8n-M9JpuFf3oLkKb8aq5uK3x_wig0SEaiAMtHmvLMAw_o925N03bOE2ANGwOzfgITJP8FsgQcpB3q1jP4HVWycNZr_76bQLqk6CsdZ8QMFgOkdzpfLFdC_THOe9bSVZgR6MNf_kR795U1qFFMuwNB2sUZHn6JIv8P-k3iA6ADuUIUFoVydKBS0BS4MlUJLqLXE4hCxkGqcMyODX-rnzMQtJk7QYj2LhyWLrQjj5s1IbDNMWfZoF19fnX0sGn2YbPvxGB39ssh7Y_OD5D-SqoiK_YR9D3rUVI0YsbHn1GuBdCnKok4QQyIFlgrAJ2aNXSqXZjKAKaNZ77FGLeH8a6IEyQMQDzaFUvIbWAQiZX_W7uQNGsnoNFqqRrkETm8SiwyG7qYPG3qwuYMdM7ZchSxCUNPXjREZk4BCpwTVPF6a_DOLG6P8ZK6LN89bkho9MsFAnt8DymE0byj9FJLHHCoeYnKG0de0gqypcz_x8ibKAzRdHZzTAINTNHswYyXrEKVg0Lj5W1pfOqm8jJyfzNpcfkktSqEnE6myIBs6WvR7M-C6zjz_WSolSuqLPqjhQHvbk6IGOTNV7-uQSaw8EsujZmhWxIxCwWEOx2xesCmbmsKyDdYlibf0maiEKkzajeEKvnZ27mjRqiiO_etrH9a7K6_g-KV9OFdbGs5yyHyek5xJ7u3-CJNCy3IUL1XOrCelEDP2x7TXyc-aedigAxMnyrMPJkOhXtt0qpNTaOlCTsah2zv3wMhAVOhTrPpDvioXhnKEC9A3Vac9rbdLzFmcjIg_7ZzGYDLwDZYjVRPsOpVemqqj_E5tmEhJ5nBcsiaPnUEtn3HPyvtYPIkUpNKWNeHP1GZOFn6cfvqLZqXRGWnuG16Fo5ZX5gb-UsvGrC_FAr4ixu4UNDQisXK7sy9uCcD-iFMiOHK6H6465WUoZ7y3g9aFVSTZjyBi2C7HmDiItUhf_pMP67ou3LjoMRq6kfaqsffKUGii1X6fkJWGA0jgHNVU0SgwyE2SvnVfui3KHaK5VeAysRSz-7iJcrlY0RUmqdPxrjDox6K7gvXI_j4wc1UBgh_5xf5sCrWh-UiN1WTrZ8nvqmv_s-3Vm00).

**Диаграмма компонентов (Components)**

[Диаграмма компонентов Device Management Service](https://www.planttext.com?text=hLPDJzj04BtxLqnp0WcIIqyz0KahK4aLabGSqMOzSLQiTztTCTIg-jyxQpks4voGLZs1npFlpSURSQuy2KTvgYDIf14UXKjlRUuH9lYY9C82NVbtRDFC6ZG44oKI9z8e8fi1MLXP8fj2h1nAKjP4qGTbfCvZp9s63L7cFur6JhmE4qMRVCNWJbf3Z3MKDXtDbHGkjjyKPgX7uu-NCoqCVP_UZrBX2HsRdXhsOHPoZSOSBvH1ztHZSnCBLvmrcIyAZaelOD3MKfa6v_0h0cXYpweIfyA815C6vvYwwjOsOEEie8qr5_25yxcUtGrQFwtMA0l9ZKixA8IQ_oDNW30nfDOeiawPP73UfP-iwWGcDorWB4YiXCUIrdfA72uUxiFJWZ7GGzpwCTplJYl-kPnjM-eMrpW1rrdD3YsEh6nGD-6MozES4u_RfbnVi8F37pbwycNj7atiEInDmnEBfKg_RiGkuHmJvSc9eA6QNADhoRlleNK8YLnhRLyz16K54axJi1QFaN7yMYNN9bwG8EoZgppoceyzeNGzmYphYD29UaoXQhaH9i6jnGUGlPIcZKBw4cdV7k5U8ybDHsfRWVJJr4lTS7GewbS1_oRth2llGTj4ILXRrybb3tkvbVmTr-f3o_Ove761nkSTjcQFUaSuS_P5UKRfAGYwBzzXoJgkHxJoXc9N8CSvF18nlBzWcom3Be0dDjpZcsDcVMXmSI-AKWEj1KfJUNjuj22aR2YgGr0TkQVFF-bCP8hzbXlbuiiPt_TYkx7y4fqHvGQNYTMgj6Pb-GY7PWN9Lchgjhy3dZ8lNvE77FFGZMdr2ELpu5WwONnc7P-0zX3Y2zVdIqhX2oD3rqC1LS-ZQ8xw-1auFFF1M6ZjORNJTGPj8GykUzzyZy7rB-hRlJeDer7K_jXvwYBseqUdA5pyQfFRSlgQy9SGkoMV77nuo_y3n8wk1b_5-bd0qcPA-ZfqdwFvUkwIbVVm9CQm9eEfUEQWi0-o71hPTvjzIbpdytdO_Oe_Z_nxvWy0)

[Диаграмма компонентов Scenario Planning Service](https://www.planttext.com?text=XLEzRjim4Dxr55TD2P1OIwTEYUqMBU0MheKYOq2HPva0nHEEfmP2qNSlAScAdBheg3j-lwGUWYYMhd6PM748JugRpzG5X5AZLsm9zavvRtqD6sfQykW5jbRLh9ei4sf122eIeGQCPTHYoMVPE-krwmnsxE0aqeOFHS7gPLLRENLLv6TDNYBNIbDJ7AnMREYRnHPTiNb_dpJbnzTTqQWWo77qFAklscGtsqIyiXxvUKsTDuhxczbysKTKSmVv8iumoc_XLmOmOs_EAPDWp1WX5xbJx1BvfzMOnzs-bnFvE_WKNJtklwJHHsC5KfvxWyT8QI1C126_NKfjgrbikrxg62MgKc4Ke20rO_bzbxvA8SOm4mud8-dlHVZ_1KYpQyxFFKoTpZGf3d6YPt8EUSatxk1rcOWVdQENC3G01eEj_UntodzTOchr2l-YxtKNOiWGm55jDHpZTYuZlf-ZhJjE0I-53jXII5JzJlL3XDS93AF4lOrbWj9wfX-RpGxe_jt6zGpvHZaNeBfm6-d-fZeZtbgC3fK9nHDRYHS-tNE2lpsuU4ANcF42Hc3sWDx4d-GF)

[Диаграмма компонентов Scenario Automation Engine](https://www.planttext.com?text=hPHDRzim38Rl_XMSJodGnfUTTcgRT1zOMgJnYXu3HMOSOPPaK5GtOzX_7-KadXDWwmwx11Qjz-77o_Wwi2AEjidOS8FmhCX-z34Wb1gT8kDXsIZdZAjXvcth7Jg6kL4rAPjbx5jW3nlFx2rKXb2pyIxBtXYdcrXXf0Psp6ruLnIalarhmxku4JvfxrXOK-rjiJ9QKUKV3BRO5BEtLoadFzql2gi28qbeFMIVjgdSR2PwPHpI-jP7Lodg9aFnPISgUmdvg9q-b5_0ZmnWq4wENQQ4qgD8JlfERPT8BqPZBky--FIxYYv0Qk6gmgrGAWW7JSWlnlJvPk3FRyVeIh7QgD0pbpvmJLW-BjAfP4yO1c1_Kw0_ispVmFhkEqyiXg1gV8mOKJJt-oFqvmJvGig5rXC7O6pG8bC7-2Ap2x3r12fqJaDBNejIMfG48_eSKxitoqz2sZ_t7P5lG89zaUYg06ASLUb15g3gxuLJq8DdinLdqqQ8QdmS3tLFGwjCqxFIP1Cf-sUNKgmVPSUxbEgzB4qgzMZsON46p4sKRUthk7Er91ZpVhy3x5ycy6rCSv9XGUDhemyk7x4hR7qmObotK1rIsf0X0dqeCURY92YjnnInTONDd-iwCJh_hBPV5PHn4pIPDbqJn5_rCFRorBLNfMVk9JMuKIpabwyWpkSYOr5LA9x9iApuORF_3-7yukXlTwf9otKKPjVIatnBVW40)

[Диаграмма компонентов User Management Service](https://www.planttext.com?text=lLJFRzfG3Bxdh_0uKQc3oquxjOL9dKGh1gfwH2OnuKdlH-Rdh4FJ_lVvXG0XHHMddQ8uzlVv-spdBWgorCvcOiGIl2Axnr17WYdzCZd1ahXvJeAhWYSlC3LOCheiar2115W7aU2WC4ovcE2px9FnkQqBgjd2LgIANyTZnhTHQMHRhnMSy-15iKPvSEE5oP6By6oe8ZkUVFayj-ZbvMasTXY5M4Eh8_keIhrc4wr7uubN3w7s1V9kUEnykTCgTmk3avPzQ703VpA0O-tmHJjvGeybEONMYXI0K-GWVg2VbXAO8gJceK31My1QjfgatIVLWBu0fj94uIOmkEboJTSDs_JXm98mrXWRx7c8KZ8jVymkCIdGtopRIrXz-ot3vo1cqz9gVlVrh6FoHGHoQ6nCSqg0KS6o_sP0QtSxkk7z_7kYvc0jiIBgEvm2YUDHCQoIwFu4Ptm9AONfPqrHOcle4UsC_TuNYmvtstSYUTzaDx6hyA6EwagCO4DfSjW4ldB6XvQIUtCE6sFfr41ZQHljiXsqDeOQlmb0XP4aEh5K6EDRu0BoBVgI-k8NL8LeT2Ax6UuQCqyHQ4A9OgfZ0ippewRzAcKBihrXN6NcO89MLsbzPfD2leUxOCI7nLUDigzP9MCHnwziH6riBoN1NHh3rSNznFPgp_ExjtczWDxTxkzJ_uGRmsw_NysnVg3Y8a9lLS1tajAvPtUQfd_DVm00)


**Диаграмма кода (Code)**

[Диаграмма кода Device Management](https://www.planttext.com?text=ZL9DZnCn3BtdLvYUMA0Ta3YDLjMYhX0hRH6Y88uhRsAcblAbn5DK8VuxoRJJJYiEN2Rni_F6VdvtMJ19xwmI5alm0vFx5FfCS4yxrWHhzDYH8o-m2gR0Z5r2fvI421BWEOW41uOJQU7WbNh1NjlUK9yiR4LYRficuQz5nxBjdmjrqi5B8Lpeu9glh36Py9afacrMx-TVB7hvldvi76QXLA2dLN0n-FeYrawLjfZpsE1l1V1w8ubz1psRIUJHqIGqb7NYE3HvHctGE49hZBTvWD_0uLn29f5ooJN_o5bkDvey9WwvvCPhJUu26qXKwb_Ud693beGcG2nSXx2F1akgQF6Jk_OupMg8RbgenUhFEEgtGkD8qluU1VyryKSRK627jfzEN9-mdbPxbXeM6X9s1FLJ7E3Y1LfMIRmZyuHoxk4qz_yhNcOpF8exYFTXyCWIyE2L4_a1lsQ6IIZxUBdCAjU3kLuR-lqI8XQ75jrJ7XWUYdVB8d2_eTfHhhyzccVsRWRp-N1SQjp25lDrrTl5ujLi8aGBHwjdTGPFb4FnSR03dReZRug3_m80)

[Telemetry Flow via Message Queue (Sequence Diagram)](https://www.planttext.com?text=dPDDJiD038NtSmglKBgesBD0hTeYka02MedraBYffVa9CvwWik8Et92JuFuGcZOjY4qYZT_xx97V32BhmCaQnSG6uKa7U-jJHFXy_u0v6hJ8OGKtnhz2JHhkC4PT8ZmaJ0ZP35yIkXnXJBeCslQKqZdx06EiAKTL2ProghJZ7zhKbHYPl9jXE5Bj6cpuhS8miRTwRPkuaboxk6ttY9MF9ErN7SMHTnoy6TvFbTgUGF_wz51m1H5TqTIpGhFkgTDwWHrE8OnQ6n8dRajPiVbDYvuwqlP_cMP3Wajmdc7XaokKEZ_DEPZpmGhl3U42q0NAb_-y7xc8WHlNM21_8UrlMIXLUZOKburbKgFZ3DTVILHBBER390Y0MqvrfEWUtdXTDE5OKBctdYv2Hr-KhIHPxpnGMMA8MRVpC86xS8syjTeLcJmPaNzdOa_MM4yOr40Erw_t2m00)

# Задание 3. Разработка ER-диаграммы

[ER-диаграмма](https://www.planttext.com?text=XLJRIWCn47tVhvX75Ve3HQH2bOe8KYq-bY4xjYEvb6HQALRm7_n3lyHaDxIxszM-XEoPoPcJCvCT1K4lQwCBOT44B-ZDnAq3mS_NDznCOSouy6ZWR4mRLWGFQ751XgoS5qLSMROmSORWem2uW3MNC8JPx6uCbvUFzrTN4HqCuX8f_RmPlAs3sYaKTZO6DkZL4dq4BKR20_1Px4lD8isfKcIGTOllbNsGUM9jeXfxm1M6yEvyES6mR2d80gREcLC2bj6FUDVkLRkbPBkYlXBPwHD5V1JIPsZ7Eu2IWlAyEZ8va0ZRHOZWMt2s8U2PTEom-EqO1REElsIKbTW-8Oc1LQla1lKwYNlL3YKDXMLf9GWRYXDfLX4jKIXzfxkI8jvGEKTf1WwAdnHPzEnEcVQtsYFRbBCbTqmx5BnMLUX_Rq9MrLSlDR_JfhQqQXRZooCXl-zHIjEudGTAyXBCLfAiwbtiTeE1-wYVun2M68fgc-5gSeVWtcrHRJESfwtEpnyvj7UrFjK8xdQT8QapzWSoGNQfvYv6PClqf_a5)

# Задание 4. Создание и документирование API

### 1. Тип API

Для межсервисного взаимодействия был выбран REST API по следующим причинам:
- простота и стандартизация
- унификация взаимодействия между сервисами и SPA
- хорошо подходит для CRUD операций

Так же в проекте используется Message Queue (Kafka) для коммуникации Scenario Automation Engine и Device Management Service. Такой подход был выбран по следующим причинам:

- высокая частота передачи данных
- асинхронность, не блокируем отравителя
- удобство масштабирования потребителей
- буферизация в случаем проблем с потребителем
- надежность за счет репликации топиков

### 2. Документация API

Файлы со схемами находятся в ./schemas

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