# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.permission import Permission  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server.models.role_permission import RolePermission  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_role import UserRole  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_create_permission(self):
        """Test case for create_permission

        Create permission
        """
        body = RolePermission()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/roles/permissions/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_role(self):
        """Test case for create_role

        Create roles
        """
        body = Role()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/roles',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user(self):
        """Test case for create_user

        Create user
        """
        body = User()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user_role(self):
        """Test case for create_user_role

        Create a role for the user
        """
        body = UserRole()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/users/{user_id}/roles'.format(user_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_permission(self):
        """Test case for delete_permission

        Delete permission
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/roles/permissions/{permission_id}'.format(permission_id='permission_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_role(self):
        """Test case for delete_role

        Delete role
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/roles/{role_id}'.format(role_id='role_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Delete user
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/users/{username}'.format(username='username_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user_role(self):
        """Test case for delete_user_role

        Delete role
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/users/roles/{role_id}'.format(role_id='role_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_permission_by_id(self):
        """Test case for get_permission_by_id

        Get permission by id
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/roles/permissions/{permission_id}'.format(permission_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_role_by_id(self):
        """Test case for get_role_by_id

        Get role by id
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/roles/{role_id}'.format(role_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_by_name(self):
        """Test case for get_user_by_name

        Get user by name
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/users/{username}'.format(username='username_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_role_by_id(self):
        """Test case for get_user_role_by_id

        Get role by name
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/users/roles/{role_id}'.format(role_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_user(self):
        """Test case for login_user

        Logs user into the system
        """
        query_string = [('username', 'username_example'),
                        ('password', 'password_example')]
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/users/login',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_user(self):
        """Test case for logout_user

        Log  out current logged user
        """
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/users/logout',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_permission(self):
        """Test case for update_permission

        Updates permission
        """
        body = Permission()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/roles/permissions/{permission_id}'.format(permission_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_role(self):
        """Test case for update_role

        Updates role
        """
        body = Role()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/roles/{role_id}'.format(role_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        Updates users
        """
        body = User()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/users/{username}'.format(username='username_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user_role(self):
        """Test case for update_user_role

        Updates role
        """
        body = UserRole()
        response = self.client.open(
            '/Erraticturtle35/Tantakatu/1.0.0/users/roles/{role_id}'.format(role_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
