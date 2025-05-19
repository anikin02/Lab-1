from config import db
from models import TypeBuilding, Country, City, Building

# item = TypeBuilding('Небоскрёб')
# db.session.add(item)
# db.session.commit()

# for type in ['Антенная мачта', 'Бетонная башня', 'Радиомачта', 'Гиперболоидная башня', 'Дымовая труба', 'Решётчатая мачта', 'Башня', 'Мост']:
#     item = TypeBuilding(type)
#     db.session.add(item)
#     db.session.commit()

# query = (TypeBuilding.query.filter((TypeBuilding.id > 3) & (TypeBuilding.type.like("%е%")))).all()
# print(query)

query = TypeBuilding.query.all()
print(query)

print("")

query = Country.query.all()
print(query)

print("")

query = City.query.all()
print(query)

print("")

query = Building.query.all()
print(query)