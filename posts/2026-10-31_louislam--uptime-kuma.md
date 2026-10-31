# Uptime Kuma — черновик выпуска 31.10.2026

Статус: blocked; Telegram не отправлялся. Проверка: documentation, не установка/пилот.

## Подпись (822 знака)

Uptime Kuma — заметить недоступный сайт
Периодически открывает страницы и сообщает о сбое. Для VITTORA рассматриваем проверку главной, музыки и журнала.

Плюсы: проверка нужного слова помогает отличить страницу от пустого ответа; история показывает моменты сбоев; настройка через экран удобна без правки конфигурационных файлов. Полезно владельцам сайтов и редакциям.

Нужен постоянно работающий компьютер/сервер: Docker либо Node.js ≥20.4 для 2.5.8. Код MIT; хостинг, электричество и обслуживание оплачиваются отдельно, сумма не рассчитана. RAM не измерена. В 2.5.8 есть открытый отчёт о пустой странице статуса; проверка доступности не проверяет плеер.

Первый шаг: на тестовой странице воспроизвести отказ и восстановление, сверить журнал.
https://github.com/louislam/uptime-kuma
31.10.2026 · документация, без запуска.

## Разбор

[cards/louislam--uptime-kuma.md](../cards/louislam--uptime-kuma.md) — сохранён в main и прочитан до предполагаемой отправки.

## Иллюстрация и блокер

PNG создан встроенным image_gen и обе версии просмотрены. Яндекс Диск доступен: VITTORA/open-arsenal, 27,6 МБ из 5 ГБ, дублей Uptime Kuma нет. Кнопка «Загрузить» не открыла поддерживаемый filechooser за 10000 мс; setFiles не вызывался, загрузка не началась, архив не подтверждён. Это таймаут выбора файла, не квота. Google Drive не объявлен восстановленным. POST не выполнялся.

```json
{
  "provider": "chat_builtin_image_gen",
  "created_at": "2026-10-31",
  "reviewed": true,
  "reviewed_at": "2026-10-31",
  "review_note": "Исходник в выводе imagegen и delivery через view_image: заголовок/подзаголовок/подвал читаемы, текст не обрезан; концептуальный ноутбук/медведь/индикатор соответствуют задаче, без измерений или обещаний.",
  "archive_status": "blocked",
  "archive_provider": null,
  "intended_archive_provider": "yandex_disk",
  "intended_archive_path": "VITTORA/open-arsenal",
  "archive_url": null,
  "blocker": "PNG создан встроенным image_gen и обе версии просмотрены. Яндекс Диск доступен: VITTORA/open-arsenal, 27,6 МБ из 5 ГБ, дублей Uptime Kuma нет. Кнопка «Загрузить» не открыла поддерживаемый filechooser за 10000 мс; setFiles не вызывался, загрузка не началась, архив не подтверждён. Это таймаут выбора файла, не квота. Google Drive не объявлен восстановленным. POST не выполнялся.",
  "files": [
    {
      "name": "2026-10-31_louislam--uptime-kuma_poster-v1.png",
      "size_bytes": 1733827,
      "sha256": "f9d38cd05419d6dcadaa5eff0e561b741809062425ce6f07f08829bffd793109",
      "width": 1254,
      "height": 1254
    },
    {
      "name": "2026-10-31_louislam--uptime-kuma_poster-v1-delivery.png",
      "size_bytes": 434768,
      "sha256": "b405b41988e92ada81414bf6feb98fc044a842fc8c90217f3710f171657762be",
      "width": 960,
      "height": 960
    }
  ]
}
```

## Доставка

```json
{
  "status": "blocked",
  "message_id": null,
  "url": null,
  "published_at": null,
  "blocker": "PNG создан встроенным image_gen и обе версии просмотрены. Яндекс Диск доступен: VITTORA/open-arsenal, 27,6 МБ из 5 ГБ, дублей Uptime Kuma нет. Кнопка «Загрузить» не открыла поддерживаемый filechooser за 10000 мс; setFiles не вызывался, загрузка не началась, архив не подтверждён. Это таймаут выбора файла, не квота. Google Drive не объявлен восстановленным. POST не выполнялся.",
  "delivery_history_checked_at": "2026-10-31",
  "delivery_history_note": "get_site owner-private: custom, только owner, внешних посетителей 0. GET status can_publish=true, channel open_arsenal. GET publish: последний Lighthouse /12 от 30.10; 0 успешных постов 31.10, Uptime Kuma нет. POST не выполнялся."
}
```
