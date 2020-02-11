# 10x Federal Grant Reporting Distiller Project

## Project description

### The 10x Federal Grant Reporting project is enabling simpler, faster, easier, better resolution of single audit findings by agencies and grantees alike.

To that end, we're building prospective shared solutions for the single audit finding resolution process.

### Distiller

Distiller, provides easier access to data, reducing a multi-day process to less than five minutes. This stands to help auditors, grant managers, and agency CFOs as well as grantees.

This codebase was extracted from exploritory work available [here](https://github.com/18F/federal-grant-reporting/).


## How can you help?

### Federal granting agency

If you're someone who works with single audits at a federal agency, we're interested in speaking with you.

Email the team at federal-grant-reporting@gsa.gov or [File an issue](https://github.com/18F/federal-grant-reporting/issues/new).

### Independent auditors

If you're someone who's created single audits, we're interested in talking with you and better understanding your current process and any pain points around creating audits and adding them to the Federal Audit Clearinghouse.

Email the team at federal-grant-reporting@gsa.gov or [File an issue](https://github.com/18F/federal-grant-reporting/issues/new).

### Grantees

If you've developed corrective action plans or been involved in single audit finding resolution, we'd love to talk.

Email the team at federal-grant-reporting@gsa.gov or [File an issue](https://github.com/18F/federal-grant-reporting/issues/new).


## Local development

To develop against a Docker-based Postgres DB and a local virtual environment, follow these steps.

### Dependencies

1. Install [Docker][https://www.docker.com/]. If you're on OS X, install Docker for Mac. If you're on Windows, install Docker for Windows.

2. Install Python dependencies into a Pipenv-managed virtual environment

```shell
pipenv install --dev
```

NOTE: Python 3.7 is required.

### Local settings

Optionally, create a local settings file in `distiller/settings/local.py`:

```python
from .development import *

CHROME_DRIVER_LOCATION = os.path.join(BASE_DIR, 'chromedriver')
```

### Database server

To start a database server, run one of these commands:

```shell
# Run in the foreground
docker-compose up db
# Run in the background
docker-compose up -d db
```

#### Initialize database

Create database tables:

```shell
docker-compose run app python manage.py migrate
```

Create a Django admin user to access the admin interface:

```shell
docker-compose run app python manage.py createsuperuser
```

#### Start a development webserver

```shell
pipenv run manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) directly to access the site.

You can access the admin panel at [http://localhost:8000/admin](http://localhost:8000/admin)
 by logging in with the super user credentials you created in the step above.

## Running ETLs

This application relies on external data sources. To populate the database with required data, run these ETL jobs.

### Download source tables

To load, first download the source table dumps. By default, these tables will be placed in timestamped directories under `/imports`. In production, these files will be placed in an S3 bucket.

To may download specific tables, or all tables at once.

```shell
pipenv run python manage.py download_table --all
pipenv run python manage.py download_table --audit
pipenv run python manage.py download_table --cfda
pipenv run python manage.py download_table --finding
pipenv run python manage.py download_table --findingtext
```

### Load tables

```shell
pipenv run python manage.py load_table --all
pipenv run python manage.py load_table --audit
pipenv run python manage.py load_table --cfda
pipenv run python manage.py load_table --finding
pipenv run python manage.py load_table --findingtext
```

### Cloud.gov table loads

In the deployed environment, `django-apscheduler` is used to refresh all tables daily at 12:00 AM EST.

### cf-service-connect

For local debugging, install [the cf service-connect plugin](https://github.com/18F/cf-service-connect "cf service connect plugin") and run `./bin/tunnel_cf_db` to access the postgres database
on cloud.gov.

## Scrapying FAC documents

Scrapy is used to download documents from the Federal Audit Clearinghouse website.

Here are some example crawls:

```shell
# Crawl all documents from prior year with CFDA `11.*`
pipenv run scrapy crawl fac -a cfda=11

# Crawl all documents from prior year with CFDA `11.2*`
pipenv run scrapy crawl fac -a cfda=11.2

# Crawl all documents from prior year with CFDA `11.123`
pipenv run scrapy crawl fac -a cfda=11.123

# Crawl all documents from prior year with CFDA `11*`
# Also, for debugging, open a copy of each search results page in a browser.
pipenv run scrapy crawl fac -a cfda=11.123 -a open_pages=1
```

In production usage, metadata on these documents should be output to file, so it may be loaded into the Distiller database. Use the `-t` and `-o` Scrapy options to specify a format and target file name:

```shell
pipenv run scrapy crawl fac -a cfda=11.123 -t json -o test.json
```

There is a script checked into the repository that will assist in refreshing a subset of CFDA prefices on a cloud.gov deployment. To run as a one-off task:

```
cf run-task fac-distiller "/home/vcap/app/bin/crawl"
```

## Running tests

To run the test suite with `pytest`:

```shell
pipenv run pytest
```

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.


## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.

[Docker]: https://www.docker.com/
[http://localhost:8000/]: http://localhost:8000/
