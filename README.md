pyelp
=====

Simple Python wrapper surrounding Yelp v2 API. See http://www.yelp.com/developers/documentation/v2/overview for more details on query params, responses, etc.

```python
# Initialize with your developer credentials
from pyelp.pyelp import Pyelp

pyelp = Pyelp(consumer_key='consumer_key',
              consumer_secret='consumer_secret',
              token='token',
              token_secret='token_secret')

# Search API (JSON returned as a dictionary)
results = pyelp.search(params={'term': 'sushi', 'location': 'Irvine, CA'})
print results['total'] # Prints total number of results

# Business API
business = pyelp.business('yelp-san-francisco')
print business['name'] # Prints name of business (ie. 'Yelp')
```