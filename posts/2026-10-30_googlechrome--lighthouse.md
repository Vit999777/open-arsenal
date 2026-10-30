# Lighthouse — опубликовано 30.10.2026

Lighthouse — понять, что тормозит сайт.
Он проверяет загрузку страницы и объясняет найденные проблемы. Для VITTORA рассматриваем страницу музыки с трейлерами.

Плюсы: замеры загрузки помогают выбрать проблему для проверки; отчёт указывает причины задержек; HTML и JSON позволяют сохранить исходный замер и сравнить после правки. Пригодится авторам сайтов и журналов.

Первый запуск — вкладка Lighthouse в инструментах разработчика Chrome. Для командной строки: Chrome и Node ≥22.19. Код — Apache-2.0; платный API и сервер для локального запуска не нужны, остаются компьютер и время настройки. Баллы колеблются; ручную проверку и данные реальных посетителей не заменяет.

Первый шаг: 5 одинаковых прогонов одной страницы, затем одна правка и повтор. Ускорение пока не измерено.
https://github.com/GoogleChrome/lighthouse
30.10.2026 · проверена документация, пилота нет.

---
## Подтверждение доставки

{
  "status": "published",
  "message_id": 12,
  "url": "https://t.me/open_arsenal/12",
  "published_at": "2026-10-30T07:06:43.133Z",
  "delivery_history_checked_at": "2026-10-30",
  "delivery_history_note": "Owner-private Site; перед POST оба GET: can_publish=true, Lighthouse отсутствует, сегодня 0 публикаций. Один POST свежим scripts/publish_telegram.py с reviewed PNG 793070 байт; обе версии архивированы на Яндекс Диске до отправки. Коннектор вернул published /12; повторного POST нет."
}

## Иллюстрация

Создана встроенным image_gen в чате; оригинал и delivery визуально проверены: надписи читаемы, поля сохранены, соответствует диагностике сайта, вымышленных оценок нет. Оба PNG до отправки сохранены в приватной папке VITTORA/open-arsenal на Яндекс Диске. UI: «Все файлы загружены», обе миниатюры видны, занято 19,2 МБ из 5 ГБ. Размер/SHA-256 локальные; обратного скачивания/восстановления не было, это архив, не проверенный резерв.

{
  "generation_method": "chat_builtin_image_gen",
  "visually_reviewed": true,
  "status": "archived",
  "archive_provider": "yandex_disk",
  "folder_url": "https://disk.yandex.ru/client/disk/VITTORA/open-arsenal",
  "verified_at": "2026-10-30",
  "verification": "UI: Все файлы загружены, обе версии видны; SHA-256 локальный. Это архив PNG, не проверенный резерв; обратного скачивания/восстановления не было.",
  "original": {
    "name": "2026-10-30_googlechrome--lighthouse_poster-v1.png",
    "size_bytes": 1948070,
    "sha256": "1c54d83092a6b104764044bc994c7bf65ee00f45178cabe044c3e827d6bf8ab6",
    "dimensions": [
      1254,
      1254
    ],
    "path": "VITTORA/open-arsenal/2026-10-30_googlechrome--lighthouse_poster-v1.png"
  },
  "delivery": {
    "name": "2026-10-30_googlechrome--lighthouse_poster-v1-delivery.png",
    "size_bytes": 793070,
    "sha256": "4fa4f23004ca4a90a4be423dd35eecd249c6f0f99ac174b1994328f78b709094",
    "dimensions": [
      800,
      800
    ],
    "path": "VITTORA/open-arsenal/2026-10-30_googlechrome--lighthouse_poster-v1-delivery.png"
  }
}

## Приёмка

Подпись 868 знаков; разбор прочитан из main до отправки. Установки/пилота нет. Следующий пилот: пять замеров до/после одной правки тестовой страницы музыки; медианы/диапазоны LCP/CLS/TBT и проверка плееров.
