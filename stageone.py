from fastapi import FastAPI
from datetime import datetime, timezone

import json
import time

app = FastAPI()

@app.get("/api")

def endpoint(slack_name, track):
    statuscode = 200
    current_date = datetime.now()
    current_date_utc = datetime.now(timezone.utc)
    utc_time =  f'{current_date_utc.strftime("%Y-%m-%dT%H:%M:%SZ")}'
    day = current_date.strftime("%A")

    return {
        "slack_name":slack_name, 
        "track":track, 
        "current_day":day, 
        "utc_time": utc_time,
        "github_file_url":'https://github.com/chunnodu/hng10/blob/main/stageone.py', 
        "github_repo_url":'https://github.com/chunnodu/hng10', 
        "status_code": statuscode
        }
    


    
  

