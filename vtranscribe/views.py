from django.shortcuts import render
import pyrebase
from google.oauth2 import service_account
from google.cloud import speech
from pydub import AudioSegment
from PyDictionary import PyDictionary

dictionary=PyDictionary()

config = {
    "apiKey": "AIzaSyBNFiTW8_2AeQNQSxlEqBu1qrRKC5S-PKU",
    "authDomain": "dict-131c6.firebaseapp.com",
    "databaseURL": "https://dict-131c6-default-rtdb.firebaseio.com/",
    "projectId": "dict-131c6",
    "storageBucket": "dict-131c6.appspot.com",
    "messagingSenderId": "263354360121",
    "appId": "1:263354360121:web:f71760956a3f3c8f2888e8"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
storage = firebase.storage()
credentials = service_account.Credentials.from_service_account_file(
    'api-key.json')


def transcribe(request):
    gcs_uri = "gs://dict-131c6.appspot.com/audio/Parts of a cell-short.wav"

    id = gcs_uri.replace('gs://dict-131c6.appspot.com/audio/', '')

    client = speech.SpeechClient(credentials=credentials)

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        audio_channel_count=1,
        enable_separate_recognition_per_channel=False,
        language_code="en-US",
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=1000)

    keywords = open('bio.txt', 'r')
    keyword_list = keywords.readlines()
    keywords.close()

    transcript = ''
    for result in response.results:
        alternative = result.alternatives[0]
        transcript += (alternative.transcript)
    definition_list = []
    for keyword in keyword_list:
        newkey = keyword.replace('\n', '')
        if newkey in transcript:
            definition_list.append(newkey)
    DiC = {}
    for defi_word in definition_list:
        DiC[defi_word] = dictionary.meaning(defi_word, True)["Noun"]
    return render(request, 'DiC/result.html',
                  {"DiC": DiC, "id": id})


def home(request):
    #  storage.child("image/pinksnail.png").download('../images', "downloaded.png")
    #  storage.child("audio/Fly-like-a-raven.mp3").download('',
    #                                                 "downloaded.mp3")

    #   storage.child('image/redsnail.png').put('C:/Users/jwang/Pictures/snail/redsnail.png')

    # Imports the Google Cloud client library

    name = database.child('Data').child('Name').get().val()
    id = database.child('Data').child('ID').get().val()
    project = database.child('Data').child('Project').get().val()
    return render(request, "DiC/index.html",
                  {"name": name, "id": id, "project": project})
