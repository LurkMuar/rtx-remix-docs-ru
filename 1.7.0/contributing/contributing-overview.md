# Как внести вклад в RTX Remix

Мы очень ценим вклад сообщества — неважно, художник вы, технический художник, разработчик или обладаете другими
полезными навыками.

## Сообщения о проблемах

Чтобы сообщить об ошибке или предложить новую функцию, следуйте инструкциям из раздела
[Как оставить NVIDIA отзыв о работе с RTX Remix?](../remix-faq.md#как-оставить-nvidia-отзыв-о-работе-с-rtx-remix)

## Участие в разработке кода

Основной репозиторий RTX Remix на GitHub —
[NVIDIAGameWorks/rtx-remix](https://github.com/NVIDIAGameWorks/rtx-remix). Он состоит из подмодулей, соответствующих
различным компонентам проекта RTX Remix:

* **[dxvk-remix](https://github.com/NVIDIAGameWorks/dxvk-remix):** содержит рендерер RTX Remix, отвечающий за
  изображение с трассировкой лучей. Здесь же находятся перехватчик (Interceptor) и конвертер (Converter) RTX Remix,
  которые преобразуют игровые данные для использования рендерером.
* **[toolkit-remix](https://github.com/NVIDIAGameWorks/toolkit-remix):** содержит RTX Remix Toolkit — интерфейс и
  набор инструментов для создания модов RTX Remix.

В каждом подмодуле есть файл `README.md` с инструкциями по сборке и запуску соответствующего проекта. Эти файлы —
важная отправная точка для разработчиков, желающих внести свой код.

Кроме того, в репозитории Toolkit есть подробная [документация для разработчиков](https://github.com/NVIDIAGameWorks/toolkit-remix/blob/main/docs_dev/index.md): стек
технологий, настройка сборки и тестирования, стандарты кодирования и типовые шаблоны реализации. Прежде чем отправлять
PR, начните с раздела Quick Start в [документации для разработчиков](https://github.com/NVIDIAGameWorks/toolkit-remix/blob/main/docs_dev/index.md) и
[контрольного списка для ревью](https://github.com/NVIDIAGameWorks/toolkit-remix/blob/main/docs_dev/getting-started/review-checklist.md).

## Участие в проектах модов

Для тех, кто хочет присоединиться к существующим проектам модов или поделиться своими работами, в
[сообществе RTX Remix Showcase в Discord](https://discord.gg/c7J6gUhXMk) есть специальный канал
[team-project-requests](https://discord.com/channels/1028444667789967381/1219748702487318591). Он помогает моддерам
общаться и координировать работу. Полезным источником информации для моддеров также служит канал
[remix-projects](https://discord.com/channels/1028444667789967381/1055020377430048848).

***

<sub>Хотите оставить отзыв о документации RTX Remix? [Нажмите здесь](https://github.com/NVIDIAGameWorks/rtx-remix/issues/new?assignees=nvdamien&labels=documentation%2Cfeedback%2Ctriage&projects=&template=documentation_feedback.yml&title=%5BDocumentation+feedback%5D%3A+)</sub>
