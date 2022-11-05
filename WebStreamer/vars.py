# (c) @AvishkarPatil | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
   API_ID = int(getenv('API_ID', '9411723'))
    API_HASH = str(getenv('API_HASH', '30fa091455c0548d77dc254f0bb705b0'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5640035101:AAFTJGGblVtC6U2Uv21vReXPVhdQUcqIYFk'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'AviStreamBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001547162655'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "875770605").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
   DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://aman:aman@cluster0.chnpche.mongodb.net/?retryWrites=true&w=majority'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '500'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001296894100")).split()))
