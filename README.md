### Work in Progress/TODO:
- [x] Full text search (stemming, ranking)
- [x] Authentication system (email, username) (millionaire, business, user, admins)
- [ ] Following system (follow millionaires)
- [ ] CRUD millionaire
- [ ] Profile acquiring process (user can acquire a millionaire profile)
- [ ] Genrate random votes for a group of millionaires (weekly/monthly/daily polls)
using task schedular
- [ ] User-search-history


### Primary Goals:
+ Run every services in docker containers `docker, docker-compose, k8s`
+ Add Unit Tests and Test-Coverage `coverage, unittest, django-test, pre-commit, CI/CD`
+ Use huge data security and perform loadtesting `locust.io, OWASP Security issues`
+ Make use of caching with redis `cache template, urls, use NoSQL/In-Memory DB for some cases`
+ Run scheduled tasks, manage long tasks via task management tools. `celery, django-q`
+ Implement notification and chat system. `django-channels`
+ Postgres full-text-search. `postgresql, elasticsearch`
+ Saas based authentication and authorization. `django-multitenant?`
+ Make use of CI/CD `github actions/cirlcle ci`
+ Make use of PDF Reporting/Generation with task managers. `waeasy print, xhtml2pdf`
+ Make use of context_processors, custom middlewares, custom management command, data-scripts
+ Implement multiprocessing, batching, multithreading related things.
+ Find and ensure possible use of HTMX, Logger, DRF


### Project (Millionaires) Specs:
+ List millionaires by their rank, list newly joined millionaires (platform users actually)
+ Full-text search with stemming, ranking
+ Update newly joined millionaires tag for millionaires after ten days.
+ Allow millionaires to follow others and manage their profiles
+ Millionaire Foundation Election (?)
+ Top Millionaires of All Time
+ Top Millionaires (Current Time)
+ Top Millionaires by Year
+ Millionaires Position Tracking (up steps, down steps each time changing their rank)


# Get started with the project:
Starting up this project is very simple, If you have docker and docker-compose setup already.
+ clone the repo and go to the project root directory (where the Dockerfile resides) from the terminal.
+ run `docker-compose up --build --scale worker=4` place worker 4 to any number. <br> You may avoid providing `--scale worker=4` part as well.
+ if you see any error like this: `docker build Error checking context: 'can't stat '...\Application Data''`  <br>
provide folder permission using this command: `sudo chown -R $USER:$USER .` <br> Then run `docker-compose up --build --scale worker=4` again.
+ Now you can access `http://127.0.0.1:8000/`
+ if you want to run migration and perform other bash actions from the project terminal, run `dodcke-compose exec we sh`. <br> It will take you to the project root bash of the docker host. Try perfoming some linux commands ;)
+ <b>EXTRA:</b> generate data running data scripts in this order: (`generate_countries.py, company_generator.py, generate_millionaires.py`)
+ <b>EXTRA PERFORMANCE TESTING:</b> run `locust` and you can monitor performance metrics at `http://127.0.0.1:8089/`

## Full-text-search Setup:
This project uses postgres as database very strictly because it uses features specific to only postgres.
Like full-text-search feature. Here's what you'll need to setup for stemming search queries:
+ access bash/shell of postgres container: `docker exec -it <CONTAINER ID> bash`
+ acess psql db: `psql -U <db_name>`
+ install the `pg_trgm` extension: `CREATE EXTENSION pg_trgm;`


## Project scripts (RunScript by django-extensions):
+ use self explanatory run scripts by running the command bellow (chose either option from <>).
+ Available scripts: <br> `company_generator` <br>`generate_countries` <br>
`generate_millionaires` <br> `upload_billionaire_images`
+ command: `python manage.py runscript upload_billionaire_images`


## Coverage Report and Testing:
Run unit-tests and see coverage reports by following the commands.
+ `coverage erase`  `# Remove any coverage data from previous runs`
+ `coverage run manage.py test`  `# Run the full test suite`

Browse coverage report as HTML Page(s)
+ `coverage html` and browse `htmlcov/index.html` file.
