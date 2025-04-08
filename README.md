### Структура Репозитория
- [degrade_image.ipynb](https://github.com/Hprimer/Increasing-Image-Resolution/blob/main/degrade_image.ipynb): Этот ноутбук содержит все методы, используемые для обработки изображений.

- [content](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content): Каталог, в котором хранятся все изображения.

  - [DIV2K](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content/DIV2K): Исходные изображения.

  - [filtered_shifted](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content/filtered_shifted): Каталог, внутри которого находятся папки К2, К4, К8 (коэффициенты уменшьшения изображений) с изображениями после усредняющего размытия, смещения и уменьшения разрешения в k раз.

  - [filtered_shifted_rotated](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content/filtered_shifted_rotated): Каталог, внутри которого находятся папки К2, К4, К8 (коэффициенты уменшьшения изображений) с изображениями после усредняющего размытия, смещения, поворота и уменьшения разрешения в k раз.

  - [filtered_shifted_rotated_scaled](https://github.com/Hprimer/Increasing-Image-Resolution/tree/main/content/filtered_shifted_rotated_scaled): Каталог, внутри которого находятся папки К2, К4, К8 (коэффициенты уменшьшения изображений) с изображениями после усредняющего размытия, смещения, поворота, уменьшения масштаба, а затем окончательного уменьшения разрешения в k раз.

**метаданные к изображениям находятся в каждой папке с алгоритмом (filtered_shifted, filtered_shifted_rotated, filtered_shifted_rotated_scaled) в файле meta_info.json**
