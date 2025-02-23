import cv2
import numpy as np
import os

# Папка с оригинальными изображениями
input_folder = "./content/DIV2K"
output_folder = "./content/degraded_shift_test_2"

os.makedirs(output_folder, exist_ok=True)  # Создаем папку для сохранения

# Функция ухудшения через смещение + снижение разрешения
def degrade_image_shift(img, scale=5, shift_range=5):
	h, w = img.shape[:2]

	# 1️⃣ Фильтрация (Гауссово размытие для имитации потери деталей)
	blurred = cv2.GaussianBlur(img, (5, 5), 1.5)

	# 2️⃣ Генерация случайного сдвига
	shift_x = np.random.uniform(-shift_range, shift_range)  # Горизонтальный сдвиг
	shift_y = np.random.uniform(-shift_range, shift_range)  # Вертикальный сдвиг

	# 3️⃣ Матрица сдвига
	M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])

	# 4️⃣ Применяем сдвиг
	shifted = cv2.warpAffine(blurred, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

	# 5️⃣ Уменьшаем разрешение (имитация ухудшения)
	small = cv2.resize(shifted, (w // scale, h // scale), interpolation=cv2.INTER_LINEAR)

	# 6️⃣ Увеличиваем обратно
	degraded = cv2.resize(small, (w, h), interpolation=cv2.INTER_LINEAR)

	return degraded

# Обрабатываем изображения
image_files = [f for f in os.listdir(input_folder) if f.endswith((".png", ".jpg"))]

for img_name in image_files:
	img_path = os.path.join(input_folder, img_name)
	img = cv2.imread(img_path)

	# Генерируем ухудшенные версии
	degraded_img = degrade_image_shift(img)

	# Сохраняем ухудшенное изображение
	cv2.imwrite(f"{output_folder}/{img_name}", degraded_img)

print("✅ Ухудшенные изображения сохранены!")
