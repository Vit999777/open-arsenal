# Каталог инструментов VITTORA

[Главная](README.md) · [План на месяц](content-plan/README.md) · [Предложить проект](CONTRIBUTING.md)

| Проект | Для чего рассматриваем | Проверка | Публикация / следующий шаг |
|---|---|---|---|
| [WhisperX](https://github.com/m-bain/whisperX) | Субтитры для озвучки | Документация и лицензия; запуск не проверен | [Пост](https://t.me/open_arsenal/3) · [Разбор и пилот](cards/m-bain--whisperx.md) |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Сохранять схемы подготовки визуалов для рилсов | Документация, лицензия, требования, релизы и выборка issues; reviewing, пилота нет | [Разбор и пилот](cards/comfy-org--comfyui.md) · [Черновик](posts/2026-10-25_comfy-org--comfyui.md) · blocked: подготовка и архив PNG; поста нет |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Локальные теги для текстов VITTORA | Документация 29.10, MIT, v0.8.0/сборка/схемы/issues; сравнение Ollama/LocalAI; reviewing, пилота нет | [Разбор](cards/ggml-org--llama.cpp.md) · [Пост](https://t.me/open_arsenal/11) · [Текст и подтверждение](posts/2026-10-29_ggml-org--llama.cpp.md) |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Проверка параметров и экспорт тизеров после монтажа | Документация, лицензия, платформы; сравнение с HandBrake/Shutter Encoder; reviewing, медиа-пилота нет | [Разбор и пилот](cards/ffmpeg--ffmpeg.md) · [Черновик](posts/2026-10-26_ffmpeg--ffmpeg.md) · blocked: подготовка и архив PNG; поста нет |
| [Audacity](https://github.com/audacity/audacity) | Три фрагмента «Воли» для тизера | Документация перепроверена 27.10; сравнение Tenacity/Ardour; reviewing, без медиа-пилота | [Разбор и пилот](cards/audacity--audacity.md) · [Пост](https://t.me/open_arsenal/6) · [Текст и подтверждение](posts/2026-10-26_audacity--audacity.md) |
| [librosa](https://github.com/librosa/librosa) | Отметки ритма «Воли» для монтажа | Документация 27.10, ISC, релиз/requirements/issues; сравнение aubio/Essentia; reviewing, без пилота | [Разбор](cards/librosa--librosa.md) · [Пост](https://t.me/open_arsenal/7) · [Текст и подтверждение](posts/2026-10-27_librosa--librosa.md) |
| [Pandoc](https://github.com/jgm/pandoc) | EPUB и HTML из общего исходника главы | Документация 28.10, GPL-2.0-or-later, релиз 3.13/INSTALL/issues; сравнение Calibre/Asciidoctor; reviewing, без пилота | [Разбор](cards/jgm--pandoc.md) · [Пост](https://t.me/open_arsenal/8) · [Текст и подтверждение](posts/2026-10-28_jgm--pandoc.md) |
| [Calibre](https://github.com/kovidgoyal/calibre) | Приёмка EPUB главы: ссылки, структура, предпросмотр и откат | Документация 28.10, GPLv3, релиз 9.17/требования ОС/Launchpad; сравнение Sigil/EPUBCheck; reviewing, без пилота | [Разбор](cards/kovidgoyal--calibre.md) · [Пост](https://t.me/open_arsenal/9) · [Текст и подтверждение](posts/2026-10-28_kovidgoyal--calibre.md) |
| [Qdrant](https://github.com/qdrant/qdrant) | Поиск фрагментов книги/инструкций с полями источника и версии | Документация 29.10, Apache-2.0, v1.20.0/требования/безопасность/issues; сравнение Chroma/pgvector; reviewing, модель не выбрана, пилота нет | [Разбор](cards/qdrant--qdrant.md) · [Пост](https://t.me/open_arsenal/10) · [Текст и подтверждение](posts/2026-10-29_qdrant--qdrant.md) |
| [Lighthouse](https://github.com/GoogleChrome/lighthouse) | Найти причины задержек страницы музыки | Документация 30.10, Apache-2.0, v13.6.0/Node>=22.19/issues; сравнение axe-core/Sitespeed.io; reviewing, пилота нет | [Разбор](cards/googlechrome--lighthouse.md) · [Пост](https://t.me/open_arsenal/12) · [Текст и подтверждение](posts/2026-10-30_googlechrome--lighthouse.md) |
| [axe-core](https://github.com/dequelabs/axe-core) | Контраст, подписи плеера/формы и структура в 3 состояниях | Документация 30.10, MPL-2.0, v4.14.0/API/issues; сравнение Pa11y/HTML_CodeSniffer; reviewing, пилота нет | [Разбор](cards/dequelabs--axe-core.md) · [Черновик](posts/2026-10-30_dequelabs--axe-core.md) · blocked: архив PNG не подтверждён, POST не выполнялся |

Дата редакционного среза: 30.10.2026. [Машиночитаемый реестр](data/candidates.json) содержит источники, пробелы и фактические подтверждения доставки. 58 ещё не исследованных активных слотов находятся в [плане исследований](content-plan/README.md).

## Как читать статусы

- **Запланирован:** тема и кандидат выбраны, редакционная проверка предстоит.
- **Исследуется:** собираются доказательства и ограничения.
- **Готов к обзору:** прошёл критерии редакции; это ещё не результат внедрения.
- **Опубликован:** есть ID сообщения и фактическая ссылка.
- **Пилот пройден:** результат подтверждён на материале VITTORA.
- **Внедрён:** использование подтверждено рабочим процессом.

Реестр кандидатов и журнал доставки сохраняют разные статусы для исследования и публикации. Не повышайте один статус по факту другого.

## Расширенное исследование

[Аналитика 100 open-source репозиториев для VITTORA](research/2026-10-25-top100/README.md) · [Данные и источники](data/research-top100-2026-10-25.json).

Срез: 25 октября 2026 года. Исследование по документации не присваивает статус редакционной готовности и не подтверждает внедрение. В отчёте есть сравнение альтернатив и ограниченные пилоты.

26.10.2026 владелец разрешил Яндекс Диск при переполнении Google Drive; интерактивная пробная загрузка в папку VITTORA подтверждена. Google Drive не объявлен восстановленным. Каждый PNG требует отдельного создания, просмотра и подтверждённого архива. [Порядок хранения](docs/STORAGE.md).
 

27.10: PNG Audacity (исходник и копия) сохранены и проверены в Яндекс Диске правильного аккаунта, путь VITTORA/open-arsenal. Обзор /6 подтверждён. План сдвинут на 27.10–25.11, прошлые слоты сохранены в [истории](content-plan/history/2026-10.json). Готовность пилота не повышена.


28.10: Pandoc опубликован /8 с новым проверенным PNG; исходник и delivery архивированы на Яндекс Диске. Горизонт 28.10–26.11, два прошедших слота сохранены в истории. Установка и пилот Pandoc не выполнены.

28.10, вечер: Calibre опубликован /9 с новым PNG; исходник и delivery архивированы на Яндекс Диске. Проверка documentation, reviewing, без установки/пилота. План 28.10–26.11: 2 published и 58 planned_research, валидаторы пройдены до отправки. Дневной лимит двух постов достигнут.

29.10: Qdrant опубликован /10 с новым PNG; исходник и delivery подтверждены в Яндекс Диске. Горизонт 29.10–27.11, слоты 28.10 сохранены в истории с фактическими подтверждениями. Publication не повышает reviewing до внедрения; локальная embedding-модель и ресурсы ещё не выбраны.

29.10, вечер: llama.cpp опубликован /11 с новым PNG; оригинал и delivery подтверждены в Яндекс Диске. Documentation/reviewing, модель и машина не выбраны, пилота нет. Горизонт 29.10–27.11 сохранён, 60 уникальных слотов. Два успешных поста за московский день; накопленные черновики не отправлялись.


| [restic](https://github.com/restic/restic) | Восстановление исходников сериала из версии архива | Документация 31.10, BSD-2-Clause, v0.19.1/requirements/issues; сравнение Borg/Kopia; reviewing, пилота нет | [Разбор](cards/restic--restic.md) · [Черновик](posts/2026-10-31_restic--restic.md) · blocked: архив PNG не подтверждён, filechooser timeout; поста нет |
