import connexion
import six

from swagger_server.models.permission import Permission  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server.models.role_permission import RolePermission  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_role import UserRole  # noqa: E501
from swagger_server import util


def create_permission(body):  # noqa: E501
    """Create permission

     # noqa: E501

    :param body: Created permission object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = RolePermission.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_role(body):  # noqa: E501
    """Create roles

     # noqa: E501

    :param body: Created role object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Role.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_user(body):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_user_role(body, user_id):  # noqa: E501
    """Create a role for the user

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes
    :param user_id: The user_id thats needs a new role. Use 1 for testing
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserRole.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_permission(permission_id):  # noqa: E501
    """Delete permission

    This can only be done by the logged in user. # noqa: E501

    :param permission_id: The permission id that needs to be deleted
    :type permission_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_role(role_id):  # noqa: E501
    """Delete role

    This can only be done by the logged in user. # noqa: E501

    :param role_id: The role id that needs to be deleted
    :type role_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def delete_user_role(role_id):  # noqa: E501
    """Delete role

    This can only be done by the logged in user. # noqa: E501

    :param role_id: The role id that needs to be deleted
    :type role_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_permission_by_id(permission_id):  # noqa: E501
    """Get permission by id

     # noqa: E501

    :param permission_id: The id thats needs to be fetched. Use 1 for testing
    :type permission_id: int

    :rtype: Permission
    """
    return 'do some magic!'


def get_role_by_id(role_id):  # noqa: E501
    """Get role by id

     # noqa: E501

    :param role_id: The id thats needs to be fetched. Use 1 for testing
    :type role_id: int

    :rtype: Role
    """
    return 'do some magic!'


def get_user_by_name(username):  # noqa: E501
    """Get user by name

     # noqa: E501

    :param username: The name thats needs to be fetched. Use user1 for testing
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def get_user_role_by_id(role_id):  # noqa: E501
    """Get role by name

     # noqa: E501

    :param role_id: The id thats needs to be fetched. Use 1 for testing
    :type role_id: int

    :rtype: UserRole
    """
    return 'do some magic!'


def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: the user name for the login
    :type username: str
    :param password: The password for the current user
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Log  out current logged user

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def update_permission(body, permission_id):  # noqa: E501
    """Updates permission

    This is only can be done by the logged in user # noqa: E501

    :param body: Update role object
    :type body: dict | bytes
    :param permission_id: id that needs to be updated
    :type permission_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Permission.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_role(body, role_id):  # noqa: E501
    """Updates role

    This is only can be done by the logged in user # noqa: E501

    :param body: Update role object
    :type body: dict | bytes
    :param role_id: id that needs to be updated
    :type role_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Role.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_user(body, username):  # noqa: E501
    """Updates users

    This is only can be done by the logged in user # noqa: E501

    :param body: Update user object
    :type body: dict | bytes
    :param username: name that needs to be updated
    :type username: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_user_role(body, role_id):  # noqa: E501
    """Updates role

    This is only can be done by the logged in user # noqa: E501

    :param body: Update role object
    :type body: dict | bytes
    :param role_id: id that needs to be updated
    :type role_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserRole.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
