# Jenkins API Consumer


### Project specifications
- Operating System platform: Windows
- Python version: 3.5.2
- Pip version: 8.1.1


### Project setup steps:
----------
- Create project directory

- Initialize git repository

- Create virtual environment
```terminal
virtual env
```

- Add "env" directory to .gitignore file

- Install Library dependencies
```
env\Scripts\pip install jenkinsapi
env\Scripts\pip install sqlalchemy
```

- Generate requirements file for repeatable installations:
```terminal
env\Scripts\pip freeze > requirements.txt
```
For later installations, use:
```
env\Scripts\pip install -r requirements.txt
```


### Libraries used
---------
- Jenkins Python Library
  Source: https://pypi.python.org/pypi/jenkinsapi

- SQLAlchemy
  Source: http://www.sqlalchemy.org/


### How to run
```terminal
virtual env
env\Scripts\pip install -r requirements.txt
env\Scripts\python Challenge1.py
```

### References
- https://pypi.python.org/pypi/jenkinsapi
- https://fatalfailure.wordpress.com/2012/06/26/the-python-jenkins-api/
- http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
