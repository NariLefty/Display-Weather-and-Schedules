# -*- coding: utf-8 -*-
import datetime, os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_schedules():
    """Get schedules method.
    Get schedules from Google Calendar.
    Ref : https://developers.google.com/calendar/api/quickstart/python
    """

    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    creds = None
    if os.path.exists("./token.json"):
        creds = Credentials.from_authorized_user_file("./token.json", SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "./credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("./token.json", "w") as token:
            token.write(creds.to_json())
    try:
        service = build("calendar", "v3", credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + "Z"
        events_results = service.events().list(
            calendarId="primary", timeMin=now,
            maxResults=3, singleEvents=True,
            orderBy="startTime"
        ).execute()
        
        events = events_results.get("items", [])

        responses = []
        for event in events:
            start = datetime.datetime.strptime(
                event['start']['dateTime'], '%Y-%m-%dT%H:%M:%S+09:00'
            )
            end = datetime.datetime.strptime(
                event['end']['dateTime'], '%Y-%m-%dT%H:%M:%S+09:00'
            )
            time = f"{start:%Y-%m-%d %H:%M}~{end:%H:%M}"
            responses.append(f"{time}\n{event['summary']}")
        
    except HttpError as error:
        print("An error occurred: %s" % error)
    
    return responses