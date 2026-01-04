"""
 1. "Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
 2. "Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
 3. Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
 4. Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
 5. Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".
 Використовуючи PuLP, створіть модель, яка визначає, скільки "Лимонаду" та "Фруктового соку" потрібно виробити 
 для максимізації загальної кількості продуктів, дотримуючись обмежень на ресурси. Напишіть програму, код якої 
 максимізує загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік", враховуючи обмеження на кількість ресурсів.
"""
import pulp

model = pulp.LpProblem("Lemonade_and_Juice_Production", pulp.LpMaximize)
# Lemonade entities
l = pulp.LpVariable('lemonade_entities', lowBound=0, cat="Integer")  
# Juice entities
j = pulp.LpVariable('juice_entities', lowBound=0, cat="Integer")
model += l + j, "Products"

# model += x + 2 * y <= 8, "Constraint1"
# model += y >= 2, "Constraint2"

model += 2 * l + j <= 100, "Water"
model += l <= 50, "Sugar"
model += l <= 30, "Lemon juice"
model += 2 * j <= 40, "Fruits"

model.solve()

if pulp.LpStatus[model.status] == "Optimal":
    for variable in model.variables():
        print(f"{variable.name} = {variable.varValue}")
    print(f"Total cost = {pulp.value(model.objective)}")

