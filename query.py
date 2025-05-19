from config import db
from models import Country, City, Building, TypeBuilding
from sqlalchemy import func

# result = db.session.query(
#     City.name, 
#     City.country_id
# ).all()

# print(result)

# result = db.session.query(
#     City.name.label("Город"), 
#     City.country_id.label("Страна")
# ).all()

# print(result)

# result = (db.session.query(
#     Country.name.label("Страна"),
#     City.name.label("Город"),
#   )
#   .join(City)
#   .all()
# )
# print(result)

# Задание 1
# Вывести информацию о каждом здании: название, тип, страна, город, год, высота.
# Информацию отсортировать по убыванию высоты.

result = (db.session.query(
    Building.title.label("Название"),
    TypeBuilding.type.label("Тип"),
    Country.name.label("Страна"),
    City.name.label("Город"),
    Building.year.label("Год"),
    Building.height.label("Высота"),
  )
  .select_from(Building)
  .join(City)
  .join(TypeBuilding)
  .join(Country)
  .order_by(Building.height.desc())
  .all()
)
print(result)

# Задание 2
# Посчитать максимальную, минимальную и среднюю высоту зданий в каждой стране,
# информацию отсортировать по названию страны.

result = (db.session.query(
    Country.name.label("Страна"),
    func.max(Building.height).label("Максимальная высота"),
    func.min(Building.height).label("Минимальная высота"),
    func.round(func.avg(Building.height), 1).label("Средняя высота")
  )
  .select_from(Building)
  .join(City)
  .join(Country)
  .group_by(Country.name)
  .order_by(Country.name.asc())
  .all()
)
print(result)

# Задание 3
# Посчитать максимальную, минимальную и среднюю высоту зданий по каждому году,
# информацию отсортировать по возрастанию года.

result = (db.session.query(
    Building.year.label("Год"),
    func.max(Building.height).label("Максимальная высота"),
    func.min(Building.height).label("Минимальная высота"),
    func.round(func.avg(Building.height), 1).label("Средняя высота")
  )
  .select_from(Building)
  .group_by(Building.year)
  .order_by(Building.year.asc())
  .all()
)
print(result)


# Задание 4
# Посчитать максимальную, минимальную и среднюю высоту зданий только для тех типов зданий,
# название которых содержит слово «мачта». Информацию отсортировать по убыванию средней высоты.

result = (db.session.query(
    TypeBuilding.type.label("Тип"),
    func.max(Building.height).label("Максимальная высота"),
    func.min(Building.height).label("Минимальная высота"),
    func.round(func.avg(Building.height), 1).label("Средняя высота")
  )
  .select_from(Building)
  .filter(Building.title.like("%мачта%"))
  .join(TypeBuilding)
  .group_by(TypeBuilding.type)
  .order_by(Building.year.asc())
  .all()
)
print(result)

# Задание 5
# Посчитать максимальную, минимальную и среднюю высоту зданий для тех стран,
# в которых построено больше одного здания
# (самостоятельно найти соответствующий метод - эквивалент HAVING в SQL).

result = (db.session.query(
    Country.name.label("Страна"),
    func.max(Building.height).label("Максимальная высота"),
    func.min(Building.height).label("Минимальная высота"),
    func.round(func.avg(Building.height), 1).label("Средняя высота")
)
.select_from(Building)
.join(City)
.join(Country)
.group_by(Country.name)
.having(func.count(Building.id) > 1)
.all()
)

print(result)