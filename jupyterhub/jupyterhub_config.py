## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

## Configure authentication (delagated to GitHub
#from oauthenticator.github import GitHubOAuthenticator
#c.JupyterHub.authenticator_class = GitHubOAuthenticator
#c.Authenticator.admin_users = { 'kimballh' }
#c.GitHubOAuthenticator.oauth_callback_url = 'https://bonsai.byu.edu/hub/oauth_callback'
#c.GitHubOAuthenticator.client_id = 'd743ba3964d1cbbe3ddb'
#c.GitHubOAuthenticator.client_secret = 'f49f2f0e2ef18f76dfa5b4ad9589a3f59add631e'

## Authenticator
PROJECT_DOMAIN = os.environ['PROJECT_DOMAIN']
from oauthenticator.oauth2 import OAuthLoginHandler
from oauthenticator.generic import GenericOAuthenticator
from tornado.auth import OAuth2Mixin

class BYUMixin(OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = 'http://{}/c2o2b/login'.format(PROJECT_DOMAIN)
    _OAUTH_ACCESS_TOKEN_URL = 'http://{}/c2o2b/token'.format(PROJECT_DOMAIN)

class BYULoginHandler(OAuthLoginHandler, BYUMixin):
    pass

class BYUAuthenticator(GenericOAuthenticator):
    login_service = 'BYU'
    login_handler = BYULoginHandler
    client_id = '0'
    client_secret = ''
    tls_verify = False
    userdata_url = 'https://{}/c2o2b/userdata'.format(PROJECT_DOMAIN)
    token_url = 'https://{}/c2o2b/token'.format(PROJECT_DOMAIN)
    oauth_callback_url = 'https://{}/hub/oauth_callback'.format(PROJECT_DOMAIN)

c.JupyterHub.authenticator_class = BYUAuthenticator
c.Authenticator.admin_users = { 'kth24', 'srp33'}
c.Authenticator.whitelist = {'kth24', 'srp33'}


## Docker spawner
import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']


# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'


## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
