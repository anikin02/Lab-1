from app import app
from flask import render_template
from structures.models import get_all_buildings, get_bulding_for_type, get_bulding_for_year, get_bulding_for_country, get_bulding_for_range_of_year


@app.route('/')

def index():
    startYear = 2000
    endYear = 2018

    [buildings_head, buildings_body] = get_all_buildings()
    [buildings_head_type, buildings_body_type] = get_bulding_for_type()
    [buildings_head_year, buildings_body_year] = get_bulding_for_year()
    [buildings_head_country, buildings_body_country] = get_bulding_for_country()
    [buildings_head_range_of_year, buildings_body_range_of_year] = get_bulding_for_range_of_year(startYear=startYear, endYear=endYear)

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body,
        buildings_head_type = buildings_head_type,
        buildings_body_type = buildings_body_type,
        buildings_head_year = buildings_head_year,
        buildings_body_year = buildings_body_year,
        buildings_head_country = buildings_head_country,
        buildings_body_country = buildings_body_country,
        buildings_head_range_of_year = buildings_head_range_of_year,
        buildings_body_range_of_year = buildings_body_range_of_year,
        startYear = startYear,
        endYear = endYear
    )

    return html