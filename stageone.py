from fastapi import FastAPI

import datetime
import time

current_date = datetime.datetime.now()
current_date_utc = datetime.datetime.now(datetime.timezone.utc)
utc_time =  f'{current_date_utc.strftime("%Y-%m-%dT%H:%M:%SZ")}'
day = current_date.strftime("%A")

app = FastAPI()

@app.get("/api")

def endpoint(slack_name, track):
    statuscode = 200
    data = {"slack_name":slack_name, "track":track, "current_day":day, "utc_time": utc_time,"github_file_url":'https://github.com/chunnodu/hng10/blob/main/stageone.py', "github_repo_url":'https://github.com/chunnodu/hng10', "status_code": statuscode}
    return data

