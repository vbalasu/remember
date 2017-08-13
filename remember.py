#USAGE: python remember.py "Python from command line"
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('inputText', help='Text string that you want to remember')
args = parser.parse_args()
if args.inputText:
  import requests
  import queue
  #from multiprocessing import Queue      #This statement is need to avoid a pyinstaller error
  import json
  payload = '{"text":"'+args.inputText+'"}'
  r = requests.post('https://cloudmaticafunctions.azurewebsites.net/api/remember?code=VavYQv2lFrkUaB82HjsQ9lZDkeaW8kyx6Srznr7pEQGH1gDK82F2uA==',data=payload)
  print(json.loads(r.text))
  