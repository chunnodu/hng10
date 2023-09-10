from typing import Union

from fastapi import FastAPI

import requests

import json

import datetime
import time

app = FastAPI()

BASE_URL = 'http://chunnodu.pythonanywhere.com'

@app.get("/")

dict = {
    "Slackname" : "chunnodu", 
    "track" : "backend"
    "Current_day": current_day
    "current_time": current_time
    "github_file_url": 
    "github_repo_url":
    "status_code"
    
    
    }

datetime.date
current_time = time.time
print(current_time)

'''
def read_data(slack_name, track):
    
    return (slack_name, track)

'''