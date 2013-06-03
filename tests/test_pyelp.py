import unittest
import json
import requests
import os

from mock import Mock
from pyelp.pyelp import Pyelp

class TestPyelp(unittest.TestCase):

    def setUp(self):
        self.pyelp = Pyelp(consumer_key='consumer_key',
                           consumer_secret='consumer_secret',
                           token='token',
                           token_secret='token_secret')

    def test_search(self):
        search_json = None
        with open(os.getcwd() + '/tests/search.json') as fp:
            search_json = fp.read()

        resp = Mock()
        resp.content = search_json
        requests.get = Mock(return_value=resp)

        results =  self.pyelp.search(params={'term': 'sushi', 'location': 'Irvine, CA'})
        self.assertEqual(results['total'], 185)

    def test_business(self):
        business_json = None
        with open(os.getcwd() + '/tests/business.json') as fp:
            business_json = fp.read()

        resp = Mock()
        resp.content = business_json
        requests.get = Mock(return_value=resp)

        returned_business = self.pyelp.business('yelp-san-francisco')
        self.assertEqual(returned_business['name'], 'Yelp')
        self.assertEqual(returned_business['rating'], 3)
