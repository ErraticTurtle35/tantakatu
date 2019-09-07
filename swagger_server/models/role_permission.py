# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RolePermission(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, role_id: int=None, permission_id: int=None, active: bool=True):  # noqa: E501
        """RolePermission - a model defined in Swagger

        :param id: The id of this RolePermission.  # noqa: E501
        :type id: int
        :param role_id: The role_id of this RolePermission.  # noqa: E501
        :type role_id: int
        :param permission_id: The permission_id of this RolePermission.  # noqa: E501
        :type permission_id: int
        :param active: The active of this RolePermission.  # noqa: E501
        :type active: bool
        """
        self.swagger_types = {
            'id': int,
            'role_id': int,
            'permission_id': int,
            'active': bool
        }

        self.attribute_map = {
            'id': 'id',
            'role_id': 'role_id',
            'permission_id': 'permission_id',
            'active': 'active'
        }
        self._id = id
        self._role_id = role_id
        self._permission_id = permission_id
        self._active = active

    @classmethod
    def from_dict(cls, dikt) -> 'RolePermission':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RolePermission of this RolePermission.  # noqa: E501
        :rtype: RolePermission
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this RolePermission.


        :return: The id of this RolePermission.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this RolePermission.


        :param id: The id of this RolePermission.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def role_id(self) -> int:
        """Gets the role_id of this RolePermission.


        :return: The role_id of this RolePermission.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id: int):
        """Sets the role_id of this RolePermission.


        :param role_id: The role_id of this RolePermission.
        :type role_id: int
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def permission_id(self) -> int:
        """Gets the permission_id of this RolePermission.


        :return: The permission_id of this RolePermission.
        :rtype: int
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id: int):
        """Sets the permission_id of this RolePermission.


        :param permission_id: The permission_id of this RolePermission.
        :type permission_id: int
        """
        if permission_id is None:
            raise ValueError("Invalid value for `permission_id`, must not be `None`")  # noqa: E501

        self._permission_id = permission_id

    @property
    def active(self) -> bool:
        """Gets the active of this RolePermission.


        :return: The active of this RolePermission.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """Sets the active of this RolePermission.


        :param active: The active of this RolePermission.
        :type active: bool
        """

        self._active = active