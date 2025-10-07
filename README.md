
<!-- <img width="270" height="320" align="left" alt="Image" src="https://github.com/user-attachments/assets/9e780001-edeb-448f-8e83-813270309f59" />  -->
<img width="700" height="420" align="left" alt="Image" src="https://github.com/user-attachments/assets/ad4d3cc8-6580-4a11-93b5-b426db15266a" />


### gqlmap  
### [![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](https://raw.githubusercontent.com/TaranYourAss/gqlmap/master/LICENSE)

<br clear="right"/>  
<br clear="left"/>  
<br>  
gqlmap is is an open source penetration testing tool that maps GraphQL engines and automates the process of detecting and exploiting GraphQL vulnerabilities.  

#### Current Detections
- Directive Overloading
- Alias Overloading
- Array-based Query Batching
- Field Duplication


## Usage
```
python3 gqlmap.py --url=https://{WEBAPP}.com/gql/v2 --cookies='session=abc123; extra=123abc' --max_overload_response=30

```
## Requirements  
cloudscraper  
plotext  
requests  
```
pip install cloudscraper, plotext, requests
```

## Overloading Info
gqlmap by default will attempt multiple types of overloads to map what the GraphQL enginge is vulnerable to.  
<br>
This is done by coninuously doubling the fields, directives, aliases, etc within each GraphQL query until a maximum set timeout or overload count is reached:  
> query alias_test {alias1: __typename alias2: __typename}  
> query alias_test {alias1: __typename alias2: __typename alias2: __typename alias3: __typename alias4: __typename}  
<br>
gqlmap takes a maximalist approach to overload testing to fully ensure denial-of-service is possible, without fully causing a denial-of-service of the application.  Applications may allow large amount of aliases, directives, fields, etc before rejecting/filtering or timing-out queries.  
  
If the GraphQL endpoint does not either:  
- limit directives, aliases, fields, etc
- filter on requests with excessive body-size
- utilize execution timeouts  

you should see the response time continously increase with the number of overload attmempts.  

> [!WARNING]
> Queries designed to overload the GraphQL engine may lead to a denial-of-service of the entire GraphQL engine, as well as resource exhaustion where a significant amount of computational resources are used to parse and validate the non-existent directives, which can result in memory exhaustion or CPU spikes.
> Always utilize either of the --max_overload_count or --max_overload_response arguments to safely test the application.  

> [!NOTE]  
> By default, gqlmap will end if the app took longer than 60s to respond or if the overload count exceeds 100,000.  
> The script only supports POST requests and formats each query as JSON within the request body.

> {"query": "query overload {__typename @include(if:true) @include(if:true) @include(if:true)}"}




> [!CAUTION]
> Attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

<sub><em>Made in Canada 🇨🇦</em></sub>
