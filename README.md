# Incora task


**How to run the application? Follow next steps:**

*Create .env file and populate it with varibles as shown in .env.sample one*, after that type next commands in terminal:
```
git clone https://github.com/sviddo/btc_convertor.git
cd btc_convertor
python manage.py migrate
python manage.py runserver
```

To try out the service you can use any api service such as [Postman](https://www.postman.com/):
- send POST request on '/users' endpoint to create a user: [example](https://im.ge/i/O1CZ1J)
- send POST request on '/login' endpoint to log in: [example](https://im.ge/i/O1E22f). Also pay attention on cookies creation
- send GET request on '/users/<id>' endpoint to get user info by id: [example](https://im.ge/i/O1xWWS)
- send PUT request on '/users/<id>' endpoint to update user info by id: [example](https://im.ge/i/O13Omm)


Trird-party libraries used in project:
1. Django library to handle phone numbers [https://github.com/stefanfoulis/django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field)
2. [PyJWT library](https://pyjwt.readthedocs.io/en/stable/#) to work with JWTs
