# Apod-py
A simple easy to use python wrapper for the "Astronomy Picture Of the Day" api.

# Installation

```py
pip install apod.py
```

# Usage 

```py
import apod 
client = apod.Client("api_key") #replace "api key" with your api key
data = client.fetch() #this will return a json file
print(data) #will print the json file
```
