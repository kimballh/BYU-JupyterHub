# BYU-JupyterHub

## [JupyterHub](https://jupyterhub.readthedocs.io/) server authenticated through BYU CAS.
---
### Information

This is a jupyterhub implementation that runs both single-user servers and the jupyterhub server inside docker containers on a single machine, it is based off of [this](https://github.com/defeo/jupyterhub-docker) implementation, following instructions given [here](https://opendreamkit.org/2018/10/17/jupyterhub-docker/).

The authentication method is customized to use BYU's CAS system for login, adapted from [this](https://github.com/defeo/cas2oauth2bridge) solution. The CAS system will only work on systems with a byu subdomain as described [here](https://it.byu.edu/byu/sc_help.do?sysparm_document_key=kb_knowledge,7ba90f3513160b402edf5a132244b0d1).

### Customization

After cloning the repository, adjust the params in the .env file to match your BYU subdomain and project name.

Adjust any of the settings in jupyterhub/jupyterhub_config.py to fit your needs (i.e. adjust user whitelist/admin priveleges), more settings can be found on jupyterhub's [docs](https://jupyterhub.readthedocs.io/). Users can also be added after starting jupyterhub from the admin console (example.byu.edu/hub/admin).

Changing the default image for single-user servers is as easy as replacing 'jupyter/datascience-notebook' in both places in docker-compose.yml with any of the jupyter stack docker images, more details about customizing your setup can be found [here](https://opendreamkit.org/2018/10/17/jupyterhub-docker/).

### Deployment
Finally, start and stop the server with docker-compose:
~~~bash
# start server running in background
docker-compose up -d
# stop server
docker-compose down
~~~
