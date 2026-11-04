# LlamaIndex — поиск фрагментов VITTORA с источниками

Направление — агенты и поиск по базе знаний. Проверка документации от 04.11.2026, статус reviewing. Установка и пилот предстоят. [Проект](https://github.com/run-llama/llama_index)

## Польза

Редактор задаёт вопрос и получает несколько отрывков с URL и версией источника. Эти поля нужно записать при подготовке корпуса. Их наличие позволяет сверять цитаты. Компонент BM25 ранжирует по совпадениям слов и позволяет ограничить число результатов. Для этого варианта языковая модель не нужна. Сценарий подходит редакциям и владельцам внутренних баз знаний. [Код BM25](https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/retrievers/llama-index-retrievers-bm25/llama_index/retrievers/bm25/base.py)

## Сравнение

LlamaIndex Core с BM25 позволяет собрать поиск по фрагментам и хранить поля происхождения. Haystack тоже предлагает локальный BM25 в явной цепочке компонентов. LangChain удобен для более широкого сценария с агентами, но для этого пилота достаточно отдельного поиска. Базовая линия — ручной поиск по тем же файлам и сверка источника. Выигрыш по времени и точности не измерен.

| Кандидат | Что проверено | Источники |
|---|---|---|
| LlamaIndex | MIT. Core 0.14.25 и отдельный BM25, Python ≥3.10. Релиз v0.14.25 от 21.09.2026. Пакет верхнего уровня включает интеграции OpenAI, для пилота выбираются Core и BM25. | [README](https://github.com/run-llama/llama_index/blob/main/README.md), [лицензия](https://github.com/run-llama/llama_index/blob/main/LICENSE), [Core](https://github.com/run-llama/llama_index/blob/main/llama-index-core/pyproject.toml), [BM25](https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/retrievers/llama-index-retrievers-bm25/pyproject.toml), [релиз](https://github.com/run-llama/llama_index/releases/tag/v0.14.25), [#23542](https://github.com/run-llama/llama_index/issues/23542), [#22601](https://github.com/run-llama/llama_index/issues/22601) |
| Haystack | Apache-2.0, Python ≥3.11, локальный InMemoryBM25Retriever. Релиз 2.31.1 от 03.11.2026. Открытый PR #13550 касается хранения результатов инструментов, а не выбранного поиска. | [README](https://github.com/deepset-ai/haystack/blob/main/README.md), [лицензия](https://github.com/deepset-ai/haystack/blob/main/LICENSE), [зависимости](https://github.com/deepset-ai/haystack/blob/main/pyproject.toml), [BM25](https://github.com/deepset-ai/haystack/blob/main/haystack/components/retrievers/in_memory/bm25_retriever.py), [релиз](https://github.com/deepset-ai/haystack/releases/tag/v2.31.1), [PR](https://github.com/deepset-ai/haystack/pull/13550) |
| LangChain | MIT, Python ≥3.10 для пакета v1, зависимости core, LangGraph и Pydantic. В ленте релизов есть отдельный пакет langchain-typesafe 0.0.1 от 04.11.2026. Это версия подпакета. Issue #41666 касается инструкций в агенте. | [README](https://github.com/langchain-ai/langchain/blob/master/README.md), [лицензия](https://github.com/langchain-ai/langchain/blob/master/LICENSE), [зависимости](https://github.com/langchain-ai/langchain/blob/master/libs/langchain_v1/pyproject.toml), [релиз](https://github.com/langchain-ai/langchain/releases/tag/langchain-typesafe%3D%3D0.0.1), [#41666](https://github.com/langchain-ai/langchain/issues/41666) |

## Запуск и ограничения

Сложность средняя. Нужны Python, подготовка корпуса и настройка русской обработки слов. Планируется локальный Linux и Python 3.12. Core и BM25 заявляют Python ≥3.10,<4.0. BM25 требует bm25s и PyStemmer, конкретные версии и совместимость проверить перед запуском. Лицензионного платежа за MIT-код нет. В выбранном сценарии без модели, внешнего API, GPU и облака остаются CPU, RAM, диск, установка, разметка и сопровождение. Денежная сумма и ресурсы неизвестны.

MIT для Core и компонента BM25. При распространении сохранять уведомления. Условия зависимостей, корпуса и моделей при будущем подключении проверять отдельно. BM25 ранжирует по совпадениям слов, поэтому перефразировки и русские словоформы требуют проверки. Исходник компонента указывает английские настройки по умолчанию. #23542 сообщает о нерелевантных результатах с нулевой оценкой, #22601 — о проблемах установки на Python 3.14 без сети. Оба отчёта не воспроизведены. Поиск не проверяет истинность фразы. Для смысловых запросов может понадобиться отдельный этап с моделью и отдельной оценкой затрат. На пилоте показывать отрывки и их происхождение, права на исходники сверить до индексации.

## Первый пилот

На 30 разрешённых фрагментах книги и журнала добавить URL и версию источника. Подготовить 10 русских вопросов с эталонными фрагментами и 3 вопроса вне корпуса. Сравнить первые пять результатов BM25 с обычным поиском по словам на том же наборе. Цель: верный фрагмент в первых пяти для ≥8 из 10 вопросов, корректный URL у всех показанных результатов и пустая выдача для 3 контрольных запросов после отсечения нулевых оценок. Записать время ручной проверки, индексирования, медиану задержки, пиковую RAM и диск. Пилот не выполнен. Ответственные — редактор и технический специалист. Лимит — один локальный набор из 30 фрагментов и 13 запросов. Пределы RAM и времени установить после базового замера. При отклонении оставить ручной поиск, корпус и рабочие материалы сохранить без изменений.

## Выпуск

04.11.2026 Яндекс Диск в папке VITTORA/open-arsenal показывает восстановление, кнопка загрузки Disabled. Google Drive ранее вернул storageQuotaExceeded, восстановление не подтверждено. Новый PNG предстоит подготовить и проверить после восстановления маршрута архива. Отправки нет. [Черновик](../posts/2026-11-04_run-llama--llama_index.md)
