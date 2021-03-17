import requests

url = 'http://ec2-13-58-4-170.us-east-2.compute.amazonaws.com:8080/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())