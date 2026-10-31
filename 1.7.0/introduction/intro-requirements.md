# Технические требования

## Требования для моддеров и игроков

Чтобы полноценно пользоваться RTX Remix и модами на его основе, нужен ПК с видеокартой RTX. Для наилучших результатов
рекомендуется NVIDIA GeForce RTX 4070 или мощнее.

| Уровень           | Операционная система | Процессор                           | ОЗУ    | Видеокарта          | Видеопамять | Диск              |
|:------------------|:---------------------|:------------------------------------|:-------|:--------------------|:------------|:------------------|
| **Минимальный**   | Windows 10           | Н/Д                                 | Н/Д    | Любая видеокарта RTX | Н/Д        | Н/Д               |
| **Рекомендуемый** | Windows 11           | Intel i7 13700K / AMD Ryzen 7 7700X | 32 ГБ  | GeForce RTX 4070    | 12 ГБ       | 10 ГБ, NVMe SSD   |

## Требования для разработчиков

### RTX Remix Runtime

* Всё то же, что в разделе [Требования для моддеров и игроков](#требования-для-моддеров-и-игроков) выше.
* Visual Studio (VS 2019 или новее).
* Windows SDK и эмулятор (10.0.19041.0 или новее).
* Meson (v0.61.4 или новее, но не v1.2.0: в этой версии отсутствует библиотека). Следуйте
  [инструкции по установке](https://mesonbuild.com/SimpleStart.html#installing-meson).
* Vulkan SDK (1.3.211.0 или новее). Возможно, потребуется удалить более старые версии.
* Python (версия 3.9 или новее).

### RTX Remix Toolkit

* Всё то же, что в разделе [Требования для моддеров и игроков](#требования-для-моддеров-и-игроков) выше.
* [VS Code](https://code.visualstudio.com/), [JetBrains PyCharm](https://www.jetbrains.com/pycharm/) или любая другая
  IDE с поддержкой Python.
* Подробности см. в
  [технических требованиях Omniverse](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/common/technical-requirements.html).

***
<sub> Хотите оставить отзыв о документации RTX Remix? [Нажмите здесь](https://github.com/NVIDIAGameWorks/rtx-remix/issues/new?assignees=nvdamien&labels=documentation%2Cfeedback%2Ctriage&projects=&template=documentation_feedback.yml&title=%5BDocumentation+feedback%5D%3A+) </sub>
