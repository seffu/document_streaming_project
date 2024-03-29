import linecache
import json
import time

# Make sure that requests is installed in your WSL
import requests 

# We could just read the entire file, but if it's really big you could go line by line
# If you want make this an excercise and replace the process below by reading the whole file at once and going line by line

#set starting id and ending id
start = 1
end = 50
# headers = {"charset": "utf-8", "Content-Type": "application/json"}
# Loop over the JSON file
i=start

while i <= end:     
    # read a specific line
    line = linecache.getline('./output.txt', i)
    #print(line)
    # write the line to the API
    myjson = json.loads(line)
    
    print(myjson)
    
    response = requests.post('http://127.0.0.1:8080/invoiceitem', json=myjson)

    # Use this for dedbugging
    #print("Status code: ", response.status_code)
    #print("Printing Entire Post Request")
    print(response.json())

    # increase i
    i+=1
    time.sleep(1)
