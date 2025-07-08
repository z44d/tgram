import tgram
from .type_ import Type_

from typing import List, Optional
from tgram.utils import message_origin_parse


class ExternalReplyInfo(Type_):
    """
    This object contains information about a message that is being replied to,
    which may come from another chat or forum topic.

    Telegram documentation: https://core.telegram.org/bots/api#externalreplyinfo

    :param origin: Origin of the message replied to by the given message
    :type origin: :class:`MessageOrigin`

    :param chat: Optional. Chat the original message belongs to. Available only if the chat is a supergroup or a channel.
    :type chat: :class:`Chat`

    :param message_id: Optional. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.
    :type message_id: :obj:`int`

    :param link_preview_options: Optional. Options used for link preview generation for the original message, if it is a text message
    :type link_preview_options: :class:`LinkPreviewOptions`

    :param animation: Optional. Message is an animation, information about the animation
    :type animation: :class:`Animation`

    :param audio: Optional. Message is an audio file, information about the file
    :type audio: :class:`Audio`

    :param document: Optional. Message is a general file, information about the file
    :type document: :class:`Document`

    :param photo: Optional. Message is a photo, available sizes of the photo
    :type photo: :obj:`list` of :class:`PhotoSize`

    :param sticker: Optional. Message is a sticker, information about the sticker
    :type sticker: :class:`Sticker`

    :param story: Optional. Message is a forwarded story
    :type story: :class:`Story`

    :param video: Optional. Message is a video, information about the video
    :type video: :class:`Video`

    :param video_note: Optional. Message is a video note, information about the video message
    :type video_note: :class:`VideoNote`

    :param voice: Optional. Message is a voice message, information about the file
    :type voice: :class:`Voice`

    :param has_media_spoiler: Optional. True, if the message media is covered by a spoiler animation
    :type has_media_spoiler: :obj:`bool`

    :param checklist: Optional. Message is a checklist
    :type checklist: :class:`tgram.types.Checklist

    :param contact: Optional. Message is a shared contact, information about the contact
    :type contact: :class:`Contact`

    :param dice: Optional. Message is a dice with random value
    :type dice: :class:`Dice`

    :param game: Optional. Message is a game, information about the game. More about games »
    :type game: :class:`Game`

    :param giveaway: Optional. Message is a scheduled giveaway, information about the giveaway
    :type giveaway: :class:`Giveaway`

    :param giveaway_winners: Optional. A giveaway with public winners was completed
    :type giveaway_winners: :class:`GiveawayWinners`

    :param invoice: Optional. Message is an invoice for a payment, information about the invoice. More about payments »
    :type invoice: :class:`Invoice`

    :param location: Optional. Message is a shared location, information about the location
    :type location: :class:`Location`

    :param poll: Optional. Message is a native poll, information about the poll
    :type poll: :class:`Poll`

    :param venue: Optional. Message is a venue, information about the venue
    :type venue: :class:`Venue`

    :return: Instance of the class
    :rtype: :class:`ExternalReplyInfo`
    """

    def __init__(
        self,
        origin: "tgram.types.MessageOrigin" = None,
        chat: "tgram.types.Chat" = None,
        message_id: "int" = None,
        link_preview_options: "tgram.types.LinkPreviewOptions" = None,
        animation: "tgram.types.Animation" = None,
        audio: "tgram.types.Audio" = None,
        document: "tgram.types.Document" = None,
        paid_media: "tgram.types.PaidMediaInfo" = None,
        photo: List["tgram.types.PhotoSize"] = None,
        sticker: "tgram.types.Sticker" = None,
        story: "tgram.types.Story" = None,
        video: "tgram.types.Video" = None,
        video_note: "tgram.types.VideoNote" = None,
        voice: "tgram.types.Voice" = None,
        has_media_spoiler: "bool" = None,
        checklist: "tgram.types.Checklist" = None,
        contact: "tgram.types.Contact" = None,
        dice: "tgram.types.Dice" = None,
        game: "tgram.types.Game" = None,
        giveaway: "tgram.types.Giveaway" = None,
        giveaway_winners: "tgram.types.GiveawayWinners" = None,
        invoice: "tgram.types.Invoice" = None,
        location: "tgram.types.Location" = None,
        poll: "tgram.types.Poll" = None,
        venue: "tgram.types.Venue" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.origin = origin
        self.chat = chat
        self.message_id = message_id
        self.link_preview_options = link_preview_options
        self.animation = animation
        self.audio = audio
        self.document = document
        self.paid_media = paid_media
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.has_media_spoiler = has_media_spoiler
        self.checklist = checklist
        self.contact = contact
        self.dice = dice
        self.game = game
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.invoice = invoice
        self.location = location
        self.poll = poll
        self.venue = venue

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ExternalReplyInfo"]:
        return (
            ExternalReplyInfo(
                me=me,
                json=d,
                origin=message_origin_parse(d.get("origin"), me),
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                message_id=d.get("message_id"),
                link_preview_options=tgram.types.LinkPreviewOptions._parse(
                    me=me, d=d.get("link_preview_options")
                ),
                animation=tgram.types.Animation._parse(me=me, d=d.get("animation")),
                audio=tgram.types.Audio._parse(me=me, d=d.get("audio")),
                document=tgram.types.Document._parse(me=me, d=d.get("document")),
                paid_media=tgram.types.PaidMediaInfo._parse(
                    me=me, d=d.get("paid_media")
                ),
                photo=[tgram.types.PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
                sticker=tgram.types.Sticker._parse(me=me, d=d.get("sticker")),
                story=tgram.types.Story._parse(me=me, d=d.get("story")),
                video=tgram.types.Video._parse(me=me, d=d.get("video")),
                video_note=tgram.types.VideoNote._parse(me=me, d=d.get("video_note")),
                voice=tgram.types.Voice._parse(me=me, d=d.get("voice")),
                has_media_spoiler=d.get("has_media_spoiler"),
                checklist=tgram.types.Checklist._parse(me=me, d=d.get("checklist")),
                contact=tgram.types.Contact._parse(me=me, d=d.get("contact")),
                dice=tgram.types.Dice._parse(me=me, d=d.get("dice")),
                game=tgram.types.Game._parse(me=me, d=d.get("game")),
                giveaway=tgram.types.Giveaway._parse(me=me, d=d.get("giveaway")),
                giveaway_winners=tgram.types.GiveawayWinners._parse(
                    me=me, d=d.get("giveaway_winners")
                ),
                invoice=tgram.types.Invoice._parse(me=me, d=d.get("invoice")),
                location=tgram.types.Location._parse(me=me, d=d.get("location")),
                poll=tgram.types.Poll._parse(me=me, d=d.get("poll")),
                venue=tgram.types.Venue._parse(me=me, d=d.get("venue")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
