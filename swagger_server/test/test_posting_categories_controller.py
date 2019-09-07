# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.posting_category import PostingCategory  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPostingCategoriesController(BaseTestCase):
    """PostingCategoriesController integration test stubs"""

    def test_create_posting_category(self):
        """Test case for create_posting_category

        Create a posting category
        """
        body = PostingCategory()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/postingCategories',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_posting_category(self):
        """Test case for delete_posting_category

        Delete category
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/postingCategories/{category_id}'.format(category_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_posting_category_by_id(self):
        """Test case for get_posting_category_by_id

        Get category by id
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/postingCategories/{category_id}'.format(category_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_posting_category(self):
        """Test case for update_posting_category

        Updates posting
        """
        body = PostingCategory()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/postingCategories/{category_id}'.format(category_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
