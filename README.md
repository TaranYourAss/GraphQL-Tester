# GraphQL-Tester
# Directive_Overload.py
This script is used to test if a web application is vulnerable to Directive Overloads by exponentially adding directives to GraphQL queries, and then plotting the data on a simple bar chart.  
  
Directive overloading occurs when an attacker leverages a large number of directives in a query to overwhelm the server's processing capabilities. Directives are used to modify the behaviour of queries.  

Queries designed to overload the GraphQL engine with excessive directives may lead to a denial-of-service of the entire GraphQL engine, as well as resource exhaustion where a significant amount of computational resources are used to parse and validate the non-existent directives, which can result in memory exhaustion or CPU spikes.  
  
If a GraphQL engine does not either:  
- limit directives
- filter on requests with excessive body-size
- utilize execution timeouts  

you should see the response time continously increase with the number of directives.  
> [!NOTE]  
> The script will end if the web app took longer than 60s to respond.  
> The script only supports POST requests and formats each query as JSON within the request body.

> {"query": "query overload {__typename @include(if:true) @include(if:true) @include(if:true)}"}


## Requirements  
cloudscraper  
plotext (optional if not plotting data into bar chart)
```
pip install cloudscraper, plotext
```

## Usage
```
python3 directive_overload.py --url https://{WEBAPP}.com/gql/v2 --cookies session=abc123 --plot-data True
```
```
Overload Count: 6 - Response Time (ms): 401.748
Overload Count: 12 - Response Time (ms): 443.837
Overload Count: 24 - Response Time (ms): 386.138
Overload Count: 48 - Response Time (ms): 417.026
Overload Count: 96 - Response Time (ms): 458.553
Overload Count: 192 - Response Time (ms): 576.506
Overload Count: 384 - Response Time (ms): 467.536
Overload Count: 768 - Response Time (ms): 559.919
Overload Count: 1536 - Response Time (ms): 610.653
Overload Count: 3072 - Response Time (ms): 839.994
Overload Count: 6144 - Response Time (ms): 1451.719
Overload Count: 12288 - Response Time (ms): 2055.501
Overload Count: 24576 - Response Time (ms): 3778.69
Overload Count: 49152 - Response Time (ms): 6874.083
Overload Count: 98304 - Response Time (ms): 14294.663
```
<img width="941" height="341" alt="Image" src="https://github.com/user-attachments/assets/063a7413-ec03-423a-b11a-b438eef6aa7e" />




> Usage for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.  
