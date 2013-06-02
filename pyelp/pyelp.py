import requests
import json

from requests_oauthlib import OAuth1

class Pyelp(object):
	"""
	Simple wrapper for Yelp v2 API

	See http://www.yelp.com/developers/documentation/v2/overview for more details
	"""

	def __init__(self, url='http://api.yelp.com/v2', consumer_key=None, consumer_secret=None, token=None, token_secret=None):
		"""
		:param url: Base URL for Yelp API
		:param consumer_key: OAuth consumer key
		:param consumer_secret: OAuth consumer secret
		:param token: OAuth access token
		:param token_secret: OAuth token secret
		"""
		self.url = url
		self.oauth = OAuth1(consumer_key,
		                    client_secret=consumer_secret,
		                    resource_owner_key=token,
		                    resource_owner_secret=token_secret)

	def search(self, params={}):
		"""
		Wraps Yelp search API

		:param params: Dictionary of query params
		"""
		search_url = '{}/search'.format(self.url)
		resp = requests.get(search_url, params=params, auth=self.oauth)
		return json.loads(resp.content)

	def business(self, business_id=None, params={}):
		"""
		Wraps Yelp business API

		:param business_id: Unique ID for Yelp business
		:param params: Dictionary of query params
		"""
		business_url = '{}/business/{}'.format(self.url, business_id)
		resp = requests.get(business_url, params=params, auth=self.oauth)
		return json.loads(resp.content)
