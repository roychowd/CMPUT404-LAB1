import requests 
print(requests.__version__)
response = requests.get("https://raw.githubusercontent.com/roychowd/CMPUT404-LAB1/master/test.py")
print(response.content)