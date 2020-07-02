# Prerequisites
* Make sure you have `Docker` and `docker-compose` installed
* Create `.env` file. You can use [.env.example](./.env.example) to see its example content
* Set up local DB. Run `docker-compose run --rm api ./manage.py migrate`. It will pull all required images and set them up so this step may take a while.
* Create a super user account: `docker-compose run --rm api ./manage.py createsuperuser`
* Import data: `docker-compose run --rm api ./manage.py runscript import-data`

You're ready to go.

# App
It's a Django app running on Python 3.8 and using PostgreSQL as a database.

Run the app: `docker-compose up api` and then out can access it at: http://localhost:8000

Admin panel accessible at http://localhost:8000/admin/

API available at http://localhost:8000/api/

# Issues
* not sure if all fields have correct type (DB)
* population and area are calculated each time being accessed. It does a DB SUM. Something to improve, maybe by denorming these fields (making them a proper table fields) and recalculating every time other models change (Django signals / celery tasks to queue etc...)
* fetching lat/lon also not very efficient. As above it makes a HTTP request to an external API which makes it slow. Could also store it in DB and for example check if coords exist, if not mayne then make a request or other strategy.
