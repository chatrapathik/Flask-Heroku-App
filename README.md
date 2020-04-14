# Flask Heroku App

## Installation

> Prerequisites: Python:3.6
```bash
# Create seperate directory.
$ sudo mkdir `your dir`
# Move to that directory.
$ cd your dir
# Install pip3
$ sudo apt-get install python3-pip
# Install Virtualenv
$ sudo pip3 install virtualenv
# Create virtual env
$ python3 -m venv env_name
# Activate Virtual env.
$ source /env_name/bin/activate
# Clone the repo.
$ git clone https://github.com/chatrapathik/Flask-Heroku-App.git
$ cd profile 
$ pip install -r requirements.txt
```

# Setup ElasticSearch Locally
```python
$ docker pull docker.elastic.co/elasticsearch/elasticsearch:7.6.2
$ docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.6.2
```
Note:
- For reference check the below document.
- https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

# Start Application

```bash
$ python run.py
```
