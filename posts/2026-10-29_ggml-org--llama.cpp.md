# llama.cpp — выпуск 29.10.2026

Статус: published. Проверка documentation, статус каталога reviewing; пилота нет.

## Текст публикации

llama.cpp — теги для текстов на своём компьютере.
Запускает языковую модель локально: она может предлагать темы и рубрики для статей VITTORA.

Рассматриваем три плюса: локальная обработка — текст можно не отправлять внешнему сервису; работа на процессоре — видеокарта не обязательна; ответ по заданной схеме — теги проще передать в каталог. Правильность тегов ещё проверим. Подойдёт редакциям и авторам.

Потребуется настройка на Windows, macOS или Linux. Код MIT, без лицензионной платы; модель и её права выбираются отдельно. Память, электричество и труд — расходы; полный бюджет пока неизвестен. Формат ответа не гарантирует смысловую точность.

Первый шаг: 10 текстов, сравнить теги с ручной разметкой.
https://github.com/ggml-org/llama.cpp
29.10.2026 · изучена документация, пилота нет.

## Приёмка

Подпись 791 знак; польза, три подтверждённые возможности, расходы/лицензия, ограничения, первый шаг и дата. Новая иллюстрация создана встроенным image_gen, оригинал и delivery просмотрены, текст читаем и не обрезан. Архив и журнал сверены до отправки; один POST подтверждён.

Разбор: [ggml-org--llama.cpp](../cards/ggml-org--llama.cpp.md).

## Подтверждение доставки

```json
{
  "status": "published",
  "message_id": 11,
  "url": "https://t.me/open_arsenal/11",
  "published_at": "2026-10-29T15:02:25.448Z",
  "delivery_history_checked_at": "2026-10-29",
  "delivery_history_note": "Owner-private Site; оба GET перед POST: can_publish=true, 1 пост сегодня, llama.cpp отсутствовал. Один POST свежим publish_telegram.py с просмотренным PNG 857128 байт, обе версии архивированы до отправки; connector returned published /11. Повторного POST нет."
}
```

## Иллюстрация и архив

```json
{
  "generation_method": "chat_builtin_image_gen",
  "visually_reviewed": true,
  "status": "archived",
  "archive_provider": "yandex_disk",
  "folder_url": "https://disk.yandex.ru/client/disk/VITTORA/open-arsenal",
  "verified_at": "2026-10-29",
  "verification": "UI: Все файлы загружены; обе миниатюры llama.cpp видны, 16.6МБ из5ГБ. SHA-256 и точные размеры локальные; обратное скачивание/восстановление не проводилось: архив PNG, не проверенный резерв.",
  "original": {
    "name": "2026-10-29_ggml-org--llama.cpp_poster-v1.png",
    "size_bytes": 2075715,
    "sha256": "8e6e44d226819f36265455093adb5ba6381af0afffa57a4d73f74930dffcd01e",
    "dimensions": [
      1254,
      1254
    ],
    "path": "VITTORA/open-arsenal/2026-10-29_ggml-org--llama.cpp_poster-v1.png",
    "url": "https://disk.yandex.ru/client/disk/VITTORA/open-arsenal"
  },
  "delivery": {
    "name": "2026-10-29_ggml-org--llama.cpp_poster-v1-delivery.png",
    "size_bytes": 857128,
    "sha256": "9b2a53e616c9e19157d3b6c70c9de41cfeafaa2813aa8d6d8be1533a45f299c4",
    "dimensions": [
      800,
      800
    ],
    "path": "VITTORA/open-arsenal/2026-10-29_ggml-org--llama.cpp_poster-v1-delivery.png",
    "url": "https://disk.yandex.ru/client/disk/VITTORA/open-arsenal"
  }
}
```

Проверки validate_catalog.py и validate_plan.py пройдены до отправки. Пилота нет. Пост с фото подтверждён защищённым маршрутом, принимающим только PNG.
