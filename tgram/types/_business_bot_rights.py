import tgram
from .type_ import Type_

from typing import Optional


class BusinessBotRights(Type_):
    """

    Represents the rights of a business bot.

    Telegram Documentation: https://core.telegram.org/bots/api#businessbotrights

    :param can_reply: Optional. True, if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours.
    :type can_reply: bool, optional
    :param can_read_messages: Optional. True, if the bot can mark incoming private messages as read.
    :type can_read_messages: bool, optional
    :param can_delete_sent_messages: Optional. True, if the bot can delete messages sent by the bot.
    :type can_delete_sent_messages: bool, optional
    :param can_delete_all_messages: Optional. True, if the bot can delete all private messages in managed chats.
    :type can_delete_all_messages: bool, optional
    :param can_edit_name: Optional. True, if the bot can edit the first and last name of the business account.
    :type can_edit_name: bool, optional
    :param can_edit_bio: Optional. True, if the bot can edit the bio of the business account.
    :type can_edit_bio: bool, optional
    :param can_edit_profile_photo: Optional. True, if the bot can edit the profile photo of the business account.
    :type can_edit_profile_photo: bool, optional
    :param can_edit_username: Optional. True, if the bot can edit the username of the business account.
    :type can_edit_username: bool, optional
    :param can_change_gift_settings: Optional. True, if the bot can change the privacy settings pertaining to gifts for the business account.
    :type can_change_gift_settings: bool, optional
    :param can_view_gifts_and_stars: Optional. True, if the bot can view gifts and the amount of Telegram Stars owned by the business account.
    :type can_view_gifts_and_stars: bool, optional
    :param can_convert_gifts_to_stars: Optional. True, if the bot can convert regular gifts owned by the business account to Telegram Stars.
    :type can_convert_gifts_to_stars: bool, optional
    :param can_transfer_and_upgrade_gifts: Optional. True, if the bot can transfer and upgrade gifts owned by the business account.
    :type can_transfer_and_upgrade_gifts: bool, optional
    :param can_transfer_stars: Optional. True, if the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts.
    :type can_transfer_stars: bool, optional
    :param can_manage_stories: Optional. True, if the bot can post, edit and delete stories on behalf of the business account.
    :type can_manage_stories: bool, optional

    :return: Instance of the class
    :rtype: :class:`tgram.types.BusinessBotRights`
    """

    def __init__(
        self,
        can_reply: "bool" = None,
        can_read_messages: "bool" = None,
        can_delete_sent_messages: "bool" = None,
        can_delete_all_messages: "bool" = None,
        can_edit_name: "bool" = None,
        can_edit_bio: "bool" = None,
        can_edit_profile_photo: "bool" = None,
        can_edit_username: "bool" = None,
        can_change_gift_settings: "bool" = None,
        can_view_gifts_and_stars: "bool" = None,
        can_convert_gifts_to_stars: "bool" = None,
        can_transfer_and_upgrade_gifts: "bool" = None,
        can_transfer_stars: "bool" = None,
        can_manage_stories: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.can_reply = can_reply
        self.can_read_messages = can_read_messages
        self.can_delete_sent_messages = can_delete_sent_messages
        self.can_delete_all_messages = can_delete_all_messages
        self.can_edit_name = can_edit_name
        self.can_edit_bio = can_edit_bio
        self.can_edit_profile_photo = can_edit_profile_photo
        self.can_edit_username = can_edit_username
        self.can_change_gift_settings = can_change_gift_settings
        self.can_view_gifts_and_stars = can_view_gifts_and_stars
        self.can_convert_gifts_to_stars = can_convert_gifts_to_stars
        self.can_transfer_and_upgrade_gifts = can_transfer_and_upgrade_gifts
        self.can_transfer_stars = can_transfer_stars
        self.can_manage_stories = can_manage_stories

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BusinessBotRights"]:
        return (
            BusinessBotRights(
                me=me,
                json=d,
                can_reply=d.get("can_reply"),
                can_read_messages=d.get("can_read_messages"),
                can_delete_sent_messages=d.get("can_delete_sent_messages"),
                can_delete_all_messages=d.get("can_delete_all_messages"),
                can_edit_name=d.get("can_edit_name"),
                can_edit_bio=d.get("can_edit_bio"),
                can_edit_profile_photo=d.get("can_edit_profile_photo"),
                can_edit_username=d.get("can_edit_username"),
                can_change_gift_settings=d.get("can_change_gift_settings"),
                can_view_gifts_and_stars=d.get("can_view_gifts_and_stars"),
                can_convert_gifts_to_stars=d.get("can_convert_gifts_to_stars"),
                can_transfer_and_upgrade_gifts=d.get("can_transfer_and_upgrade_gifts"),
                can_transfer_stars=d.get("can_transfer_stars"),
                can_manage_stories=d.get("can_manage_stories"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
