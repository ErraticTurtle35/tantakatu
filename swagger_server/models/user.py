# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, username: str=None, login: str=None, password: str=None, country_id: str=None, active: bool=True):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: int
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param login: The login of this User.  # noqa: E501
        :type login: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param country_id: The country_id of this User.  # noqa: E501
        :type country_id: str
        :param active: The active of this User.  # noqa: E501
        :type active: bool
        """
        self.swagger_types = {
            'id': int,
            'username': str,
            'login': str,
            'password': str,
            'country_id': str,
            'active': bool
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'login': 'login',
            'password': 'password',
            'country_id': 'country_id',
            'active': 'active'
        }
        self._id = id
        self._username = username
        self._login = login
        self._password = password
        self._country_id = country_id
        self._active = active

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self) -> str:
        """Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this User.


        :param username: The username of this User.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def login(self) -> str:
        """Gets the login of this User.


        :return: The login of this User.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login: str):
        """Sets the login of this User.


        :param login: The login of this User.
        :type login: str
        """
        if login is None:
            raise ValueError("Invalid value for `login`, must not be `None`")  # noqa: E501

        self._login = login

    @property
    def password(self) -> str:
        """Gets the password of this User.


        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.


        :param password: The password of this User.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def country_id(self) -> str:
        """Gets the country_id of this User.


        :return: The country_id of this User.
        :rtype: str
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id: str):
        """Sets the country_id of this User.


        :param country_id: The country_id of this User.
        :type country_id: str
        """

        self._country_id = country_id

    @property
    def active(self) -> bool:
        """Gets the active of this User.


        :return: The active of this User.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """Sets the active of this User.


        :param active: The active of this User.
        :type active: bool
        """

        self._active = active
