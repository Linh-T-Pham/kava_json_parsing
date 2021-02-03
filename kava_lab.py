import json 
import requests
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

request = requests.get("https://kava-3-snapshots.s3.amazonaws.com/kava-4-export-20210122.json")
request_text = request.text 

data = json.loads(request_text)
print(data)

# Create myfile.json 

# out_file = open("myfile.json", "w")
# json.dump(data, out_file, indent = 6)
# out_file.close()
# print(out_file)

delegations_data = data['app_state']['staking']['delegations']
# print(delegations_data)
shares_list = []
for each_delegartion in delegations_data:
    shares_list.append(each_delegartion['shares'])
    shares_list_length = len(shares_list) # 6545

# Question1:  Find the median 
shares_list.sort()
index_of_median = len(shares_list) // 2
median = shares_list[index_of_median]
# print(median) # 25000000.000000000000000000

# Question 2: Mean numbers of shares

total_values_of_shares = 0 
for each_share in shares_list:
    total_values_of_shares += float(each_share)

mean = total_values_of_shares / shares_list_length 
# print(mean) # 11164855160.519333

# Question 3: Find the address which has the most number of delegations 
delegator_address_arr = (sorted(delegations_data, key = lambda i: (i['shares'], i['delegator_address'])))
address = delegator_address_arr[-1]["delegator_address"]
# print(address) #kava1cdsplflzkwcyx8kz26v07m6q3ucrttfps3qp8v


#Question 4: create range of x-values from float(shares_list[0]) to float(shares_list[-1]) in increments of .001
x = np.arange(int(float(shares_list[0])), int(float(shares_list[-1])), 0.001)

#create range of y-values that correspond to normal pdf with mean=0 and sd=1 
y = norm.pdf(x,0,1)

#define plot 
fig, ax = plt.subplots(figsize=(9,6))
ax.plot(x,y)

#choose plot style and display the bell curve 
plt.style.use('fivethirtyeight')
print(plt.show())