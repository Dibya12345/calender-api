<h1 align="center">calender app</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/Dibya12345/covin-assignment?color=56BEB8">
  <img alt="Github language count" src="https://img.shields.io/github/languages/count/Dibya12345/covin-assignment?color=56BEB8">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/Dibya12345/covin-assignment?color=56BEB8">
  <img alt="License" src="https://img.shields.io/github/license/Dibya12345/covin-assignment?color=56BEB8">
</p>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#demo">Demo</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{github}}" target="_blank">Author</a>
</p>

<br>

## :dart: About

Implementing google calendar integration using django rest api. This app uses OAuth2 mechanism to get users calendar access. Below are detail of API endpoint and corresponding views which you need to implement.

## :sparkles: Features

/rest/v1/calendar/init/ -> GoogleCalendarInitView()
:heavy_check_mark: This view should start step 1 of the OAuth. Which will prompt user for
his/her credentials
/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()
:heavy_check_mark: This view will do two things

1. Handle redirect request sent by google with code for token. You
   need to implement mechanism to get access_token from given
   code
2. Once got the access_token get list of events in users calendar

### Demo

Here is the demo of the assignment [Demo](https://www.loom.com/share/88f5958310cd44e9bc5c97567eb1713c)
Here is the replit link [Replit](https://replit.com/@dibyadash1/covin-assignment)

## :rocket: Technologies

The following tools were used in this project:

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Google Calendar API](https://developers.google.com/calendar)

## :white_check_mark: Requirements

Before starting :checkered_flag:, you need to have [Python](https://www.python.org/) installed.
Create an virtual environment and activate it.

Create an account in google cloud console and create a project. Enable google calendar api and create credentials. Download the credentials and rename it to client_secret.json and place it in the main folder.

## :checkered_flag: Starting

```bash
# Clone this project
$ git clone https://github.com/Dibya12345/covin-assignment.git

# Install dependencies
$ pip install -r requirements.txt

# Access
$ cd main

# Run the project
$ python manage.py runserver

# The server will initialize in the <http://localhost:3000>
```

## :memo: License

This project is under license from MIT. For more details, see the [LICENSE](LICENSE) file.

Made with :heart: by <a href="https://github.com/Dibya12345" target="_blank">Dibya Debayan Dash</a>

&#xa0;

<a href="#top">Back to top</a>
