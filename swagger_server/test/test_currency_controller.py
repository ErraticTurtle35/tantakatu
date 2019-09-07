# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.currency import Currency  # noqa: E501
from swagger_server.models.currency_rate import CurrencyRate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCurrencyController(BaseTestCase):
    """CurrencyController integration test stubs"""

    def test_create_currency(self):
        """Test case for create_currency

        Create currency
        """
        body = Currency()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/currencies',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_currency_rate(self):
        """Test case for create_currency_rate

        Create currency rate
        """
        body = CurrencyRate()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/currencies/{currency_id}/rate'.format(currency_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_currency(self):
        """Test case for delete_currency

        Delete currency
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/currencies/{currency_id}'.format(currency_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_currency_rate(self):
        """Test case for delete_currency_rate

        Delete currency rate
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/currencies/rate/{rate_id}'.format(rate_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_currency_by_id(self):
        """Test case for get_currency_by_id

        Get currency by id
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/currencies/{currency_id}'.format(currency_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_currency_rate_id(self):
        """Test case for get_currency_rate_id

        Get currency rate by id
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/currencies/rate/{rate_id}'.format(rate_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_currency(self):
        """Test case for update_currency

        Updates currency
        """
        body = Currency()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/currencies/{currency_id}'.format(currency_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_currency_rate(self):
        """Test case for update_currency_rate

        Updates currency rate
        """
        body = CurrencyRate()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/currencies/rate/{rate_id}'.format(rate_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
