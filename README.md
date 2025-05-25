### Структура Репозитория
- [degrade_image.ipynb](https://github.com/Hprimer/Increasing-Image-Resolution/blob/main/degrade_image.ipynb): Этот ноутбук содержит все методы, используемые для обработки изображений.

- [DataSets](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/DataSets): Каталог, c датасетами из открытого доступа (Urban100, Set5, Set14).

- [content](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content): Каталог, в котором хранятся все изображения моего датасета.

  - [Nail'sDataSet](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content/DIV2K): Исходные изображения.

  - [filtered_shifted_scaled](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content/filtered_shifted_scaled): Каталог, внутри которого находятся папки К2, К4, К8 (коэффициенты уменшьшения изображений) с изображениями после усредняющего размытия, смещения и уменьшения разрешения в k раз.

  - [filtered_shifted_rotated_scaled](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content/filtered_shifted_rotated_scaled): Каталог, внутри которого находятся папки К2, К4, К8 (коэффициенты уменшьшения изображений) с изображениями после усредняющего размытия, смещения, поворота и уменьшения разрешения в k раз.

  - [filtered_shifted_rotated_randomScaled](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content/filtered_shifted_rotated_randomScaled): Каталог, внутри которого находятся папки К2, К4, К8 (коэффициенты уменшьшения изображений) с изображениями после усредняющего размытия, смещения, поворота и изменения масштаба в (alpha/k) раз (alpha = случайное число из [0.9;1.1]).

  - [filtered_shifted_randomScaled](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content/filtered_shifted_randomScaled): Каталог, внутри которого находятся папки К2, К4, К8 (коэффициенты уменшьшения изображений) с изображениями после усредняющего размытия, смещения и изменения масштаба в (alpha/k) раз (alpha = случайное число из [0.9;1.1]).

**метаданные к изображениям находятся в каждой папке с алгоритмом (filtered_shifted_scaled, filtered_shifted_rotated_scaled, filtered_shifted_rotated_randomScaled, filtered_shifted_randomScaled) в файле meta_info.json**

#### Также в репозитории находятся некоторые БД:
