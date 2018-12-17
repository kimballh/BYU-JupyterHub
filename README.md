# BYU-JupyterHub

## [JupyterHub](https://jupyterhub.readthedocs.io/) server authenticated through BYU CAS.
---
### Information

This is a jupyterhub implementation that runs both single-user servers and the jupyterhub server inside docker containers on a single machine, it is based off of [this](https://github.com/defeo/jupyterhub-docker) implementation, following instructions given [here](https://opendreamkit.org/2018/10/17/jupyterhub-docker/).

The authentication method is customized to use BYU's CAS system for login, adapted from [this](https://github.com/defeo/cas2oauth2bridge) solution. The CAS system will only work on systems with a byu subdomain as described [here](https://it.byu.edu/byu/sc_help.do?sysparm_document_key=kb_knowledge,7ba90f3513160b402edf5a132244b0d1).

### Set-up

After cloning the repository, adjust the params in the .env file to match your BYU subdomain and provide a project name. In this file you can also change the default image for single-user from 'jupyter/datascience-notebook' with any of docker images in the [jupyter stack](https://jupyter-docker-stacks.readthedocs.io/en/latest/).

Adjust any of the settings in jupyterhub/jupyterhub_config.py to fit your needs (i.e. adjust user whitelist/admin priveleges); more settings can be found on jupyterhub's [docs](https://jupyterhub.readthedocs.io/). Users can also be added after starting jupyterhub from the admin console (example.byu.edu/hub/admin). More details about customizing your setup can be found [here](https://opendreamkit.org/2018/10/17/jupyterhub-docker/).

Finally, in order for jupyter hub to run over https as recommended, you need to add the ssl certs to the certs directory as key.pem and cert.pem. If you don't have certs, you can generate self-signed ssl certs with the following command:
~~~bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem --nodes
~~~
(Make sure those files are placed in the certs directory)


### Deployment
After editing .env and adding any custimization, build the project with the following command:
~~~bash
docker-compose build
~~~

Finally, start and stop the server with docker-compose:
~~~bash
# start server running in background
docker-compose up -d
# stop server
docker-compose down
~~~
