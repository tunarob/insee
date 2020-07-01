import csv
import os

from tqdm import tqdm

from ..models import City, County, Region

FILENAME = "correspondance-code-insee-code-postal.csv"


def run():
    current_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_path, FILENAME)) as f:
        rows = csv.DictReader(f, delimiter=";")
        for row in tqdm(rows):
            region = get_or_create_region(row)
            county = get_or_create_county(row, region)
            get_or_create_city(row, county)


def get_or_create_region(row) -> Region:
    region, _ = Region.objects.get_or_create(
        code=row["Code Région"], defaults={"name": row["Région"]}
    )
    return region


def get_or_create_county(row, region: Region) -> County:
    county, _ = County.objects.get_or_create(
        code=row["Code Département"],
        defaults={"name": row["Département"], "region": region},
    )
    return county


def get_or_create_city(row, county: County) -> City:
    city, _ = City.objects.get_or_create(
        code_insee=row["Code INSEE"],
        defaults={
            "code_postal": row["Code Postal"],
            "name": row["Commune"],
            "population": row["Population"],
            "area": row["Superficie"],
            "county": county,
        },
    )
    return city
