### Primary Goals:
+ Run every services in docker containers
+ Add Unit Tests and Test-Coverage
+ Use huge data and perform loadtesting
+ Make use of caching with redis
+ Run scheduled tasks, manage long tasks via task management tools.
+ Implement notification and chat system.
+ Postgres full-text-search
+ Saas based authentication and authorization
+ Make use of CI/CD
+ Make use of PDF Reporting/Generation with task managers.
+ Make use of context_processors, custom middlewares, custom management command, data-scripts
+ Implement multiprocessing, batching, multithreading related things.
+ Find and ensure possible use of HTMX, Logger, DRF


### Project (Millionaires) Specs:
+ List millionaires by their rank, list newly joined millionaires (platform users actually)
+ Update newly joined millionaires tag for millionaires after ten days.
+ Allow millionaires to follow others and manage their profiles
+ Millionaire Foundation Election (?)
+ Top Millionaires of All Time
+ Top Millionaires (Current Time)
+ Top Millionaires by Year
+ Millionaires Position Tracking (up steps, down steps each time changing their rank)


# Get started with the project:
Starting up this project is very simple, If you have docker and docker-compose setup already.
+ clonse the repo and go to the project rood directory (where Dockerfile resides) from terminal.
+ run `docker-compose up --build --scale worker=4` place worker 4 to any number.
+ if you see anything like this: `docker build Error checking context: 'can't stat '...\Application Data''` 
provide permission using this command: `sudo chown -R $USER:$USER .`
+ Now you can access `http://127.0.0.1:8000/`
+ if you wish to run migration and perform other bash actions from the project location, run `dodcke-compose exec we sh`
+ EXTRA: generate data running data scripts in this order: (`generate_countries.py, company_generator.py, generate_millionaires.py`)
+ EXTRA PERFORMANCE TESTING: run `locust` and you can monitor performance metrics at `http://127.0.0.1:8089/`
