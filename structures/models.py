from config import db 
from models import Country, City, Building, TypeBuilding
from sqlalchemy import func

def get_all_buildings():
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.type.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота")
          )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
    )
    return [query.statement.columns.keys(), query.all()]

def get_bulding_for_type():
    result = (db.session.query(
    TypeBuilding.type.label("Тип"),
    func.max(Building.height).label("Максимальная высота"),
    func.min(Building.height).label("Минимальная высота"),
    func.round(func.avg(Building.height), 1).label("Средняя высота")
  )
    .select_from(Building)
    .join(TypeBuilding)
    .group_by(TypeBuilding.type)
    )
    return [result.statement.columns.keys(), result.all()]

def get_bulding_for_country():
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
    )
    return [result.statement.columns.keys(), result.all()]

def get_bulding_for_year():
    result = (db.session.query(
        Building.year.label("Год"),
        func.max(Building.height).label("Максимальная высота"),
        func.min(Building.height).label("Минимальная высота"),
        func.round(func.avg(Building.height), 1).label("Средняя высота")
    )
    .select_from(Building)
    .group_by(Building.year)
    .order_by(Building.year.asc())
    )
    return [result.statement.columns.keys(), result.all()]

def get_bulding_for_range_of_year(startYear, endYear):
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.type.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота")
          )
        .select_from(Building)
        .filter((Building.year >= startYear) & (Building.year <= endYear))
        .join(TypeBuilding)
        .join(City)
        .join(Country)
    )
    return [query.statement.columns.keys(), query.all()]