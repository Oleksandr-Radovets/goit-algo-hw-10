from pulp import LpMaximize, LpProblem, LpVariable

# Створюємо модель
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні: кількість виробленого лимонаду (L) та фруктового соку (F)
L = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
F = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Функція мети: максимізація загальної кількості вироблених продуктів
model += L + F, "Total_Production"

# Обмеження ресурсів
model += (2 * L + 1 * F <= 100), "Water_Limit"
model += (1 * L <= 50), "Sugar_Limit"
model += (1 * L <= 30), "Lemon_Juice_Limit"
model += (2 * F <= 40), "Fruit_Puree_Limit"

# Розв'язуємо задачу
model.solve()

# Виводимо результати
print(f"Оптимальна кількість Лимонаду: {int(L.varValue)}")
print(f"Оптимальна кількість Фруктового соку: {int(F.varValue)}")
