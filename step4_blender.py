# Блок 1: Импорт библиотек и очистка сцены
# Этот блок импортирует необходимые библиотеки и подготавливает Blender
import bpy
import numpy as np
from mpmath import zeta

# Очистка сцены (удаляем все объекты перед началом)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

print("Блок 1: Импорт библиотек и очистка сцены завершены.")

# Блок 2: Определение параметров и функций
# Здесь задаются параметры и функции для вычислений
# Параметры
T = 20  # Интервал времени
dt = 1.0  # Шаг для ускорения
N = int(2 * T / dt)  # Количество точек (N = 40)
t = np.linspace(-T, T, N)  # Массив времени

# Функции из статьи
def psi(s, u, epsilon):
    denom = (s - 0.5 - 1j*u)**2 * (1 - s - 0.5 - 1j*u)**2 + epsilon**2
    return 1 / denom

def zeta_squared(t):
    return abs(complex(zeta(0.5 + 1j*t)))**2

# Значения epsilon для перебора
epsilon_values = [1e-5, 5e-5, 1e-4]

# Вычисление интегралов для всех epsilon
sigma_vals = np.linspace(0, 1, 30)
gamma = 14.1347  # Пример мнимой части (первый нетривиальный нуль)
curves_data = []

print("Блок 2: Определение параметров и функций завершено.")

# Блок 3: Вычисление интегралов и создание 3D-графика
# Этот блок вычисляет интегралы и строит график в Blender
for idx, epsilon in enumerate(epsilon_values):
    print(f"\nВычисление для ε = {epsilon}")
    
    # Вычисление интегралов
    integrals_rho = [np.trapezoid([complex(psi(sigma + 1j*gamma, u, epsilon) * zeta_squared(u)) for u in t], t) for sigma in sigma_vals]
    integrals_1_minus_rho = [np.trapezoid([complex(psi(1 - sigma + 1j*gamma, u, epsilon) * zeta_squared(u)) for u in t], t) for sigma in sigma_vals]
    
    # Отладочный вывод: значения интегралов при sigma = 0.5
    sigma_idx = np.argmin(np.abs(sigma_vals - 0.5))
    print(f"Значение интеграла для psi(rho, t) при sigma = {sigma_vals[sigma_idx]}: {integrals_rho[sigma_idx]}")
    print(f"Значение интеграла для psi(1-rho, t) при sigma = {sigma_vals[sigma_idx]}: {integrals_1_minus_rho[sigma_idx]}")
    difference = abs(integrals_rho[sigma_idx] - integrals_1_minus_rho[sigma_idx])
    print(f"Разница между интегралами: {difference}")
    
    curves_data.append((integrals_rho, integrals_1_minus_rho))

# Создание 3D-графиков в Blender
z_offset = 0  # Смещение по оси Z для каждого epsilon
for idx, (integrals_rho, integrals_1_minus_rho) in enumerate(curves_data):
    epsilon = epsilon_values[idx]
    
    # Масштабирование значений для визуализации
    sigma_scaled = (sigma_vals - 0.5) * 10  # Масштабируем sigma для оси X
    rho_scaled = np.array(integrals_rho) * 0.1  # Масштабируем значения интегралов для оси Y
    rho_minus_scaled = np.array(integrals_1_minus_rho) * 0.1
    
    # Создание кривой для integrals_rho
    curve_data_rho = bpy.data.curves.new(f'Curve_rho_epsilon_{epsilon}', type='CURVE')
    curve_data_rho.dimensions = '3D'
    spline_rho = curve_data_rho.splines.new('POLY')
    spline_rho.points.add(len(sigma_vals) - 1)
    
    for i in range(len(sigma_vals)):
        x = float(sigma_scaled[i])
        y = float(rho_scaled[i].real)  # Используем только действительную часть
        z = z_offset
        spline_rho.points[i].co = (x, y, z, 1)
    
    curve_obj_rho = bpy.data.objects.new(f'Curve_rho_epsilon_{epsilon}', curve_data_rho)
    bpy.context.collection.objects.link(curve_obj_rho)
    curve_obj_rho.data.materials.append(bpy.data.materials.new(name=f"Material_rho_{epsilon}"))
    curve_obj_rho.data.materials[0].diffuse_color = (1, 0, 0, 1)  # Красный цвет
    
    # Создание кривой для integrals_1_minus_rho
    curve_data_1_minus_rho = bpy.data.curves.new(f'Curve_1_minus_rho_epsilon_{epsilon}', type='CURVE')
    curve_data_1_minus_rho.dimensions = '3D'
    spline_1_minus_rho = curve_data_1_minus_rho.splines.new('POLY')
    spline_1_minus_rho.points.add(len(sigma_vals) - 1)
    
    for i in range(len(sigma_vals)):
        x = float(sigma_scaled[i])
        y = float(rho_minus_scaled[i].real)  # Используем только действительную часть
        z = z_offset
        spline_1_minus_rho.points[i].co = (x, y, z, 1)
    
    curve_obj_1_minus_rho = bpy.data.objects.new(f'Curve_1_minus_rho_epsilon_{epsilon}', curve_data_1_minus_rho)
    bpy.context.collection.objects.link(curve_obj_1_minus_rho)
    curve_obj_1_minus_rho.data.materials.append(bpy.data.materials.new(name=f"Material_1_minus_rho_{epsilon}"))
    curve_obj_1_minus_rho.data.materials[0].diffuse_color = (0, 0, 1, 1)  # Синий цвет
    
    # Добавляем линию для критической линии (sigma = 0.5)
    curve_data_line = bpy.data.curves.new(f'CriticalLine_epsilon_{epsilon}', type='CURVE')
    curve_data_line.dimensions = '3D'
    spline_line = curve_data_line.splines.new('POLY')
    spline_line.points.add(1)
    y_min = min(min(rho_scaled.real), min(rho_minus_scaled.real))
    y_max = max(max(rho_scaled.real), max(rho_minus_scaled.real))
    spline_line.points[0].co = (0, y_min, z_offset, 1)  # sigma = 0.5 соответствует x = 0 после масштабирования
    spline_line.points[1].co = (0, y_max, z_offset, 1)
    
    curve_obj_line = bpy.data.objects.new(f'CriticalLine_epsilon_{epsilon}', curve_data_line)
    bpy.context.collection.objects.link(curve_obj_line)
    curve_obj_line.data.materials.append(bpy.data.materials.new(name=f"Material_line_{epsilon}"))
    curve_obj_line.data.materials[0].diffuse_color = (1, 0, 1, 1)  # Пурпурный цвет
    
    # Смещение по Z для следующего epsilon
    z_offset += 2

# Настройка камеры и рендеринга
bpy.ops.object.camera_add(location=(20, -20, 10))
camera = bpy.context.object
camera.rotation_euler = (1.0, 0, 0.8)

# Настройка освещения
bpy.ops.object.light_add(type='SUN', location=(10, -10, 10))

# Рендеринг сцены
bpy.context.scene.camera = camera
bpy.context.scene.render.filepath = bpy.path.abspath("//render_step4.png")
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.ops.render.render(write_still=True)

print("Блок 3: Вычисление интегралов и создание 3D-графика завершены.")
print("Рендеринг завершён. Изображение сохранено как 'render_step4.png'.")
