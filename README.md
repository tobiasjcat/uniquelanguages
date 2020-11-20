# Unique languages homework

## Design
The purpose of this assignment is to create an API that returns a list of  
unique official languages out of five regions: Africa, Americans, Asia, Europe   
and Oceania. 
After gathering the data from `https://restcountries.eu/` I compiled the data   
into a single JSON file with the five regions and their respective languages.   
The API just loads this data into RAM and returns the languages when requested. 

### Pros
- All of the possible responses are less than 2Kb and can be stored in RAM easily; no need for a database. This allows for very fast responses.  
- Regions and official languages don't change very often.
- This API does not create more unnecessary requests to `restcountries.eu`.

### Cons
- Inflexible: When regions or languages change, the compliled data file will need to be updated. 

### Frameworks
- **Flask** allows for a very stripped down API with no database or HTML templates  
It also allows for advanced configuration and modular design. Switching from http  
to https is simple as is turning threading on or off.  
- **Python Unittest** is a standard testing suite for python. Something more complicted
like Selenium would be overkill. 
## To Run

```
$ pip install -r requirements.txt
$ flask run
```
or with docker
```
$ docker build -t homework:languages .
$ docker run -d -p 5000:5000 homework:languages
```

## To Test
```
$ python3 test_app.py
```
expected test response:
```
$ python3 test_app.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.028s

OK
```