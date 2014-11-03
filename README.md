# Whiskerboard Docker Image

This is a Dockerized version of Whiskerboard. It runs a development ready instance of the webapp inside a docker container with default settings making it suitable to run with the default trusted Redis and PostgreSQL images. No third-party services are required. 

## What is Whiskerboard

Whiskerboard is a status board for websites, services and APIs, like Amazon's [AWS status page](http://status.aws.amazon.com/).

It is heavily based on [Stashboard](http://www.stashboard.org/). Unlike Stashboard, it uses vanilla Django, so you aren't stuck using Google App Engine.


### Running this image

It's dead quick to get a status board up and running using Docker. The easiest way is to use the included Fig file to orchestrate Redis, PostgreSQL, and the Whiskerboard containers:

	$ fig up
	
You can also manually spin up the depedencies as needed.

	$ docker run -d -t --name some-redis \ 
				  -v `pwd`/redis:/data \ 
				  redis:2.8 \ 
				  redis-server --appendonly yes
				  
	$ docker run -d -t --name some-postgres \ 
				 -v `pwd`/pgdata/data:/data \ 
				 -v `pwd`/pgdata/log:/var/log/postgresql \
				 postgres:9.3
				 
	$ docker run -d -t --name whiskerboard \ 
				 -v `pwd`/whiskerboard/logs:/whiskerboard/logs \ 
				 --link some-redis:redis \ 
				 --link some-postgres:postgres \ 
				 -p 8000:8000 \
				 -p 10022:22 \
				 -h docker.example.com \
				 agaveapi/whiskerboard

The webapp will be running in a python dev server by default. In the future we will front the app with a http server.

At this point you can visit the app. Now head over to http://docker.example.com:8000/admin/ and login with admin:changeit. You'll want to set the name of your board by clicking on "sites". Edit the single entry called "example.com" and enter a name for your board.

Back on the admin home page, click on "services" and add the things you want to report the status of (website, API etc). To change the status of a service add an event for it.

