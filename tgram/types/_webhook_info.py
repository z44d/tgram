import tgram
from .type_ import Type_

from typing import List, Optional


class WebhookInfo(Type_):
    """
    Describes the current status of a webhook.

    Telegram Documentation: https://core.telegram.org/bots/api#webhookinfo

    :param url: Webhook URL, may be empty if webhook is not set up
    :type url: :obj:`str`

    :param has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks
    :type has_custom_certificate: :obj:`bool`

    :param pending_update_count: Number of updates awaiting delivery
    :type pending_update_count: :obj:`int`

    :param ip_address: Optional. Currently used webhook IP address
    :type ip_address: :obj:`str`

    :param last_error_date: Optional. Unix time for the most recent error that happened when trying to deliver an
        update via webhook
    :type last_error_date: :obj:`int`

    :param last_error_message: Optional. Error message in human-readable format for the most recent error that
        happened when trying to deliver an update via webhook
    :type last_error_message: :obj:`str`

    :param last_synchronization_error_date: Optional. Unix time of the most recent error that happened when trying
        to synchronize available updates with Telegram datacenters
    :type last_synchronization_error_date: :obj:`int`

    :param max_connections: Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook
        for update delivery
    :type max_connections: :obj:`int`

    :param allowed_updates: Optional. A list of update types the bot is subscribed to. Defaults to all update types
        except chat_member
    :type allowed_updates: :obj:`list` of :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.WebhookInfo`
    """

    def __init__(
        self,
        url: "str" = None,
        has_custom_certificate: "bool" = None,
        pending_update_count: "int" = None,
        ip_address: "str" = None,
        last_error_date: "int" = None,
        last_error_message: "str" = None,
        last_synchronization_error_date: "int" = None,
        max_connections: "int" = None,
        allowed_updates: List["str"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.ip_address = ip_address
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.last_synchronization_error_date = last_synchronization_error_date
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.WebhookInfo"]:
        return (
            WebhookInfo(
                me=me,
                json=d,
                url=d.get("url"),
                has_custom_certificate=d.get("has_custom_certificate"),
                pending_update_count=d.get("pending_update_count"),
                ip_address=d.get("ip_address"),
                last_error_date=d.get("last_error_date"),
                last_error_message=d.get("last_error_message"),
                last_synchronization_error_date=d.get(
                    "last_synchronization_error_date"
                ),
                max_connections=d.get("max_connections"),
                allowed_updates=d.get("allowed_updates"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
