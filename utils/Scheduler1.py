import datefinder
from datetime import date, datetime, timedelta
import pickle
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import dateutil.parser
scopes = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file(
"./utils/client_secret.json", scopes=scopes)


# flow = InstalledAppFlow.from_client_secrets_file(
    # "client_secret.json", scopes=scopes)

# credentials = flow.run_console()
# print(credentials)

# pickle.dump(credentials, open("token.pkl", "wb"))
credentials = pickle.load(open("./utils/token.pkl", "rb"))
# credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
# result = service.calendarList().list().execute()
# print(result['items'][0])

# calendar_id = result['items'][0]['id']
# result = service.events().list(calendarId=calendar_id,
#                                timeZone="Asia/Kolkata").execute()
# result['items'][0]
# start_time = datetime(2019, 5, 12, 19, 30, 0)
# end_time = start_time + timedelta(hours=4)
# timezone = 'Asia/Kolkata'

# event = {
#     'summary': 'IPL Final 2019',
#     'location': 'Hyderabad',
#     'description': 'MI vs TBD',
#     'start': {
#         'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
#         'timeZone': timezone,
#     },
#     'end': {
#         'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
#         'timeZone': timezone,
#     },
#     'reminders': {
#         'useDefault': False,
#         'overrides': [
#             {'method': 'email', 'minutes': 24 * 60},
#             {'method': 'popup', 'minutes': 10},
#         ],
#     },
# }

# service.events().insert(calendarId=calendar_id, body=event).execute()

# matches = datefinder.find_dates("5 may 9 PM")
# list(matches)


def create_event(start_time_str, summary, duration=1, description=None, location=None):

    matches = list(datefinder.find_dates(start_time_str))
    print("matches ", matches[0])
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)

    # return
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    return service.events().insert(calendarId='primary', body=event).execute()


# create_event("25 Sep 7 PM", "Meeting again")
# print("Meeting Scheduled")


def create_event_for_meeting(dateTimeInput, summary, duration=1, description=None, location=None):
    # dateTimeInput = dateutil.parser.isoparse(dateTimeInput)
    dateTimeInput = dateutil.parser.parse(dateTimeInput)
    # print("dateTimeInput ", dateTimeInput)
    # return
    # matches = list(datefinder.find_dates(dateTimeInput))
    # if len(matches):
    #     start_time = matches[0]
    #     end_time = start_time + timedelta(hours=duration)

    start_time = dateTimeInput

    end_time = start_time + timedelta(hours=duration)

    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    return service.events().insert(calendarId='primary', body=event).execute()


# create_event("25 Sep 7 PM", "Meeting again")

# create_event_for_meeting('2021-10-02T19:53', summary='Meeting from yb')
