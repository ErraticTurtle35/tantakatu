import connexion
import six

from swagger_server.models.currency import Currency  # noqa: E501
from swagger_server.models.currency_rate import CurrencyRate  # noqa: E501
from swagger_server import util


def create_currency(body):  # noqa: E501
    """Create currency

     # noqa: E501

    :param body: Created currency object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Currency.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_currency_rate(body, currency_id):  # noqa: E501
    """Create currency rate

     # noqa: E501

    :param body: Created a currency object
    :type body: dict | bytes
    :param currency_id: The currency_id thats needs to be updated
    :type currency_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = CurrencyRate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_currency(currency_id):  # noqa: E501
    """Delete currency

    This can only be done by the logged in user. # noqa: E501

    :param currency_id: The currency_id that needs to be deleted
    :type currency_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_currency_rate(rate_id):  # noqa: E501
    """Delete currency rate

    This can only be done by the logged in user. # noqa: E501

    :param rate_id: The rate_id that needs to be deleted
    :type rate_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_currency_by_id(currency_id):  # noqa: E501
    """Get currency by id

     # noqa: E501

    :param currency_id: The currency_id thats needs to be fetched. Use 1 for testing
    :type currency_id: int

    :rtype: Currency
    """
    return 'do some magic!'


def get_currency_rate_id(rate_id):  # noqa: E501
    """Get currency rate by id

     # noqa: E501

    :param rate_id: The rate_id thats needs to be fetched. Use 1 for testing
    :type rate_id: int

    :rtype: CurrencyRate
    """
    return 'do some magic!'


def update_currency(body, currency_id):  # noqa: E501
    """Updates currency

    This is only can be done by the logged in user # noqa: E501

    :param body: Update currency object
    :type body: dict | bytes
    :param currency_id: currency_id that needs to be updated
    :type currency_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Currency.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_currency_rate(body, rate_id):  # noqa: E501
    """Updates currency rate

    This is only can be done by the logged in user # noqa: E501

    :param body: Update currency rate object
    :type body: dict | bytes
    :param rate_id: rate_id that needs to be updated
    :type rate_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = CurrencyRate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
