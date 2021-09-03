# WIP meminisse
## An experimental password generator

<!-- TOC -->

- [Deescription](#description)
- [Requirements](#requirements)
- [Upcoming-features](#to-be-added)
- [Contribution](#contributionguide)

### Description

An experimental password generator, make password from set of words
this can be a complete sensible sentence or vene jumled sentence with no real meaning, but this set of words must be tailored to each individual to act as an unique set of password after conversion. For the current release this must be entered each time user need a new password, an account system is currently in the work that aims to saves each user preferences for an easy centralized generation, but of course this is an issuee of itself as this feature will likely compromise user password, so on the way to find an acceptable alternative.


### Requirements

- cachelib==0.3.0
- certifi==2021.5.30
- charset-normalizer==2.0.4
- click==8.0.1
- Flask==2.0.1
- Flask-Session==0.4.0
- gunicorn==20.1.0
- idna==3.2
- itsdangerous==2.0.1
- Jinja2==3.0.1
- MarkupSafe==2.0.1
- requests==2.26.0
- urllib3==1.26.6
- Werkzeug==2.0.1

### Release v0.0.4 Neira

Deployed to Heroku https://reminisse.herokuapp.com/,
fixed grammar and typo.

### To be added

1. Error catching
2. Algorithm improvement
3. UI revamp
4. Account system
5. Database for storing user saved passwords
6. Custom user profiles for entered password
7. Random password generator

### Quick start

Download or Fork-Clone the repo, install the requirements located in requirements.txt with:

```
$ pip install -r requirements.txt
```
Then run with

```
$ flask run
```

### Contribution guide

Fork the repo add your changes, and submit a pull request