# print("Entre  integer values: ")
# num_list=list(input().split())

# # sorting

# for i in range(len(num_list)):
#     for j in range(len(num_list)):
#         if(num_list[i]<num_list[j]):
#             temp=num_list[i]
#             num_list[i]=num_list[j]
#             num_list[j]=temp
# for num in num_list:
#     print(num)

import matplotlib.pyplot as plt
# # import urllib.request
# import json
# from urllib.request import urlopen
# url = 'https://raw.githubusercontent.com/oktadev/blazor-example/master/OktaBlazor/wwwroot/sample-data/weather.json'

# # store the response of URL
# response = urlopen(url)
  
# # storing the JSON response 
# # from url in data
# data_json = json.loads(response.read())
  
# print the json response
# print(data_json)


data=[
  {
    "date": "2018-05-06",
    "temperatureC": 1,
    "summary": "Freezing",
    "temperatureF": 33
  },
  {
    "date": "2018-05-07",
    "temperatureC": 14,
    "summary": "Bracing",
    "temperatureF": 57
  },
  {
    "date": "2018-05-08",
    "temperatureC": -13,
    "summary": "Freezing",
    "temperatureF": 9
  },
  {
    "date": "2018-05-09",
    "temperatureC": -16,
    "summary": "Balmy",
    "temperatureF": 4
  },
  {
    "date": "2018-05-10",
    "temperatureC": -2,
    "summary": "Chilly",
    "temperatureF": 29
  }
]

# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# y = [5, 7, 8, 1, 4, 9, 6, 3, 5, 2, 1, 8]
x=list()
y=list()
for i in range(len(data)):
    x.append(data[i]["date"])

for i in range(len(data)):
    y.append(data[i]["temperatureC"])

#plot y vs x
plt.plot(x, y)
 
#set title and x, y - axes labels
plt.title('Matplotlib Example')
plt.xlabel('x-axis Data')
plt.ylabel('y-axis temperatureC')
 
#show plot to user
plt.show()

