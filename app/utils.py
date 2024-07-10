import os,json
import pathlib

import psycopg2

def getConfig():
    # variables por defecto(1)
    config = {
        "env": "local",
        "version": "20240709",
        "system" : {
            "admin" : {
                "show" : True,
                "path" : "admin/"
            },
            # "database" : {
            #     "ENGINE": "django.db.backends.postgresql",
            #     "NAME": "db",
            #     "USER": "postgres",
            #     "PASSWORD": "postgres",
            #     "HOST": "localhost",
            #     "PORT": "5432",
            # },
            "database" : {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "db.sqlite3",
                "USER": "",
                "PASSWORD": "",
                "HOST": "",
                "PORT": "",
            },
            "SECRET_KEY" : "django-insecure-qcn6dz0kc1_*pt-hm@bq+^7osludbmq=&d&i@gy!-i^)nr+p$e",
            "DEBUG" : True,
            "ALLOWED_HOSTS" : ["*"],
            "CSRF_TRUSTED_ORIGINS" : ["http://localhost:8000"],
            "static_url" : "static/"
        }
    }

    # Archivo json(2)
    BASE_DIR_1 = pathlib.Path(__file__).resolve().parent
    path = os.path.join(BASE_DIR_1,'config.log.json')
    if os.path.isfile(path):
        with open(path,"r") as f:
            data = json.load(f)
            updateJson(data,config,"config")
    
    # Variables de entorno(3)
    try:
        data = os.environ.get("P149_JSON", "{}")
        data = json.loads(data)
        updateJson(data,config,"env")
    except Exception as errors:
        print("Error(742.4301213112705): No se puede procesar os.environ.get()")
        print(errors)
    return config

def updateJson(source,target,base):
    for key in source:
        if key in target:
            if type(target[key]) == type({}) and type(source[key])==type({}):
                updateJson(source[key],target[key],base+'.'+key)
            elif type(target[key])==type(source[key]):
                target[key] = source[key]
            else:
                print("Error(342.38004029413327): updateJson:",base+"."+key,"target:",type(target[key]),"source",type(source[key]))
