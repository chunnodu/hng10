from fastapi import FastAPI

import json

import datetime
import time

current_date = datetime.datetime.now()
current_date_utc = datetime.datetime.now(datetime.timezone.utc)
utc_time = current_date.strftime("%Y-%m-%dT%H:%M:%SZ")

day = current_date.strftime("%A")

app = FastAPI()

@app.get("/api")

def endpoint(slackname, track):
    statuscode = 200
    data = {
        "slack_name":slackname, "track":track, "current_day":day, "current_time":utc_time,
        "github_file_url":'https://github.com/chunnodu/hng10/blob/main/stageone.py', 
        "github_repo_url":'https://github.com/chunnodu/hng10', "status_code": statuscode
        }
    return data

