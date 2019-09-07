# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.posting import Posting  # noqa: E501
from swagger_server.models.posting_photo_gallery import PostingPhotoGallery  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPostingController(BaseTestCase):
    """PostingController integration test stubs"""

    def test_create_posting(self):
        """Test case for create_posting

        Create posting
        """
        body = Posting()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/posting',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_posting_photo(self):
        """Test case for create_posting_photo

        Create posting photo
        """
        body = PostingPhotoGallery()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/posting/gallery',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_posting(self):
        """Test case for delete_posting

        Delete posting
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/posting/{posting_id}'.format(posting_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_posting_photo(self):
        """Test case for delete_posting_photo

        Delete posting photo
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/posting/gallery/{photo_id}'.format(photo_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_posting_by_id(self):
        """Test case for get_posting_by_id

        Get posting by id
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/posting/{posting_id}'.format(posting_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_posting_photo_by_id(self):
        """Test case for get_posting_photo_by_id

        Get posting photo by id
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/posting/gallery/{photo_id}'.format(photo_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_publish_posting(self):
        """Test case for publish_posting

        Publish the posting
        """
        body = Posting()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/posting/{posting_id}/publish'.format(posting_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sell_posting(self):
        """Test case for sell_posting

        Sell posting
        """
        body = Posting()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/posting/{posting_id}/sell'.format(posting_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_posting(self):
        """Test case for update_posting

        Updates posting
        """
        body = Posting()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/posting/{posting_id}'.format(posting_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_posting_photo(self):
        """Test case for update_posting_photo

        Updates posting photo
        """
        body = PostingPhotoGallery()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/posting/gallery/{photo_id}'.format(photo_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
