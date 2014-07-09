# Combining ExtJS 5 with Django 1.6
Django is a wonderful framework on the Serverside and ExtJS ist a clear win for Client-Application-Developers. Would be nice if we could bring them together. This is a Proof of Concept of how this could be done. Far more then delivering code it is meant as Documentation and Reference. The Code is tested to run with python 3.3

To understand the explanations below, you should go through at least Part 1 & 2 of the [Django 1.6 Tutorial](https://docs.djangoproject.com/en/1.6/intro/tutorial01/). Instead of adding HTML-Templates in Part 3, we'll add a REST-Api and on top of that a nice ExtJS Application.

## Installing the dependencies
To install all dependencies Globally on your System, run

	sudo pip3 install -r requirements.txt

This will install

 - django 1.6 (stable at the time of writing)
 - djangorestframework (automatically expose django models as REST-Api-Calls)
 - django-filter (sorting and -optionally- filtering for the on the REST-Api)
 - django-rest-auth (login. logout and profile functions for the REST-Api)
 - django-registration (requirement of django-rest-auth)

## Setting up the REST-Api
The first thing we'll do is configuring the browsable REST-Api. For the existing Model [Polls](polls/models.py#L5) this will automatically generate views and routes to handle HTTP-Requests like this:

 - GET /api/polls (get a list of all polls)
 - POST /api/polls (add a new poll)
 - OPTIONS /api/polls (get meta-information of the Polls-Model)
 - GET /api/polls/5 (get Details of Poll Number 5)
 - PUT/PATCH /api/polls/5 (modify Poll Number 5)
 - DELETE /api/polls/5 (remove Number 5)

and some more. This feature is provided by the [Django REST framework](http://www.django-rest-framework.org/).
To enable this functionality, add the two apps 'rest_framework' and 'rest_framework.authtoken' to the [djangotest/settings.py#L32](INSTALLED_APPS config). 'rest_framework.authtoken' provides an Token-Based authorization (your Desktop-Client-Program saves a token instead of the original username/password) which we don't need here but the 'rest_auth'-package does not work without.

Further down in the settings.py-File the [REST_FRAMEWORK configuration](djangotest/settings.py#L58) follows:

 - DEFAULT_MODEL_SERIALIZER_CLASS names the class that converts model-information to json. [rest_framework.serializers.HyperlinkedModelSerializer](http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis) is the default class, that returns json based on the model definition but with hyperlinks to the clickable REST-Api
 - DEFAULT_AUTHENTICATION_CLASSES names the class that controlls how the current user is determined. [rest_framework.authentication.SessionAuthentication](http://www.django-rest-framework.org/api-guide/authentication#sessionauthentication) uses a session-cookie to identify the current user
 - DEFAULT_PERMISSION_CLASSES names  the class that controlls which user can access which information. [rest_framework.permissions.DjangoModelPermissions](http://www.django-rest-framework.org/api-guide/permissions#djangomodelpermissions) uses the permissions that can be controlled in the django admin-gui. Depending on your requirements there are [other defaults](http://www.django-rest-framework.org/api-guide/permissions) you should check out.
   ![django permission GUI](http://i.stack.imgur.com/icrtr.png)
 - PAGINATE_BY_PARAM configures the name of the parameter, that the django REST-Api expects from ExtJS to specify the number of results that should be returned. "limit" is what ExtJS assumes by default.
 - ORDERING_PARAM does the same for sorting. ExtJS defaults to "sort"
 - PAGINATE_BY is the default number of items to display per page. ExtJS has its own setting, so this setting does not really matter much
 - MAX_PAGINATE_BY limits the number of items that can be returned per page.
 - DEFAULT_FILTER_BACKENDS enables sorting and filtering by default. The classes named in this array are ties between the datasource an the REST-Api-Output and that can modify the queries sent to the database. The order of items in this array matters - first filter, then sort. This would be the place to add other filter backends, see "Filtering" below.

And finally a global setting - LOGIN_REDIRECT_URL - sets the url where a non-ajax user gets redirected after the login. This only matters when a user loggs in to the browsable api, because normal users will always use the Ajax-Gui. Setting this value to '/api/' is just a cosmetic thing.

## Filtering

## Running with Python 3.2

## A word on Production systems