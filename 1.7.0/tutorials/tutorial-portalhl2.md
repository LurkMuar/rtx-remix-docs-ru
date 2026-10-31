# Настройка Portal для совместимости с RTX Remix

```{important}
Для этого руководства нужна игра [Portal with RTX](https://store.steampowered.com/app/2012840/Portal_with_RTX).

Убедитесь, что Portal и Portal with RTX установлены и полностью обновлены.
```

Многим играм для корректной работы с RTX Remix Runtime нужны определённые изменения. В случае Portal совместимость с
RTX Remix улучшают изменения, сделанные в
[Portal with RTX](https://store.steampowered.com/app/2012840/Portal_with_RTX). Другим играм на
[Source Engine](https://developer.valvesoftware.com/wiki/Source) (например,
[Half-Life 2](https://developer.valvesoftware.com/wiki/Half-Life_2)) для совместимости с RTX Remix также понадобятся
похожие шаги настройки.

```{warning}
Эти шаги относятся именно к обеспечению совместимости Portal.
```

## Копирование необходимых файлов

1. **Резервная копия папки CFG:** перейдите в папку `cfg` игры **Portal** (`common\Portal\portal\cfg`) и переименуйте
   её (например, в `original-cfg`), чтобы сохранить исходные данные.
2. **Копирование содержимого CFG:** скопируйте все файлы из папки `cfg` игры **Portal with RTX**
   (`common\Portal with RTX\portal_rtx\cfg`) и вставьте их в папку `cfg` игры **Portal** (`common\Portal\portal\cfg`).
3. **Резервная копия папки BIN:** аналогично перейдите в папку `bin` игры **Portal** (`common\Portal\bin`) и
   переименуйте её (например, в `original-bin`), чтобы сохранить исходные данные.
4. **Копирование содержимого BIN:** скопируйте все файлы из папки `bin` игры **Portal with RTX**
   (`common\Portal with RTX\bin`) и вставьте их в папку `bin` игры **Portal** (`common\Portal\bin`).
5. **Копирование файлов конфигурации:** скопируйте файлы `rtx.conf` и `dxvk.conf` из папки **Portal with RTX**
   (`common\Portal with RTX`) и вставьте их в папку **Portal** (`common\Portal`).
6. **Копирование файлов RTX Remix Runtime:** скопируйте файлы
   [последней версии RTX Remix Runtime](../installation/install-runtime.md#загрузка-с-github) в `common\Portal\bin`,
   при запросе перезаписав существующие файлы.

## Изменение игровых переменных

После запуска игры из библиотеки Steam может понадобиться задать некоторые переменные. Это можно сделать через
консоль разработчика в игре или через параметры запуска Steam.

1. Установите `dxlevel` равным `70`.
2. Установите `r_3dsky` равным `0`.
3. Установите `viewmodel_fov` равным `90`.
4. Установите `cl_first_person_uses_world_model` равным `0`.

### Параметры запуска Steam

1. Откройте Steam.
2. Перейдите в «Библиотеку».
3. Щёлкните правой кнопкой по игре, которую нужно перенастроить.
4. Выберите в меню «Свойства...».
5. Перейдите в раздел «Параметры запуска».
6. Удалите все параметры запуска, указанные в поле ввода.
7. Задайте параметры запуска, как описано выше. Параметры запуска Steam должны выглядеть так:
   ```text
   -dxlevel 70 -r_3dsky 0 -viewmodel_fov 90 -cl_first_person_uses_world_model 0
   ```

```{tip}
Запуск игры с разными уровнями DirectX может решить некоторые проблемы, но в других играх может вызвать новые.

Чтобы изменить уровень DirectX в параметрах запуска, используйте следующие значения:

1. `-dxlevel 90` (DirectX v9.0)
2. `-dxlevel 81` (DirectX v8.1)
3. `-dxlevel 80` (DirectX v8.0)
4. `-dxlevel 70` (DirectX v7.0)
```

## Запуск игры

Теперь в Portal можно играть с RTX Remix.

Запускайте игру как обычно из библиотеки Steam.

Если нужна помощь с настройкой RTX Remix для других игр, заходите в
[сообщество RTX Remix Showcase в Discord](https://discord.gg/c7J6gUhXMk) и загляните в канал
[remix-projects](https://discord.com/channels/1028444667789967381/1055020377430048848).

***
<sub> Хотите оставить отзыв о документации RTX Remix? [Нажмите здесь](https://github.com/NVIDIAGameWorks/rtx-remix/issues/new?assignees=nvdamien&labels=documentation%2Cfeedback%2Ctriage&projects=&template=documentation_feedback.yml&title=%5BDocumentation+feedback%5D%3A+) </sub>
