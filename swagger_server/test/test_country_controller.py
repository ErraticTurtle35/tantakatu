# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.country import Country  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCountryController(BaseTestCase):
    """CountryController integration test stubs"""

    def test_create_country(self):
        """Test case for create_country

        Create a country
        """
        body = Country()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/countries',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_country(self):
        """Test case for delete_country

        Delete country
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/countries/{country_id}'.format(country_id='country_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_county_by_id(self):
        """Test case for get_county_by_id

        Get user by name
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/countries/{country_id}'.format(country_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_country(self):
        """Test case for update_country

        Updates country
        """
        body = Country()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/countries/{country_id}'.format(country_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
