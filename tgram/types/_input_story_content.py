import tgram
from .type_ import Type_
from typing import Optional


class InputStoryContentPhoto(Type_):
    """
    Describes a photo to post as a story.

    :param type: Type of the content, always "photo"
    :type type: :obj:`str`
    :param photo: The photo to post as a story. The photo must be of the size 1080x1920 and must not exceed 10 MB.
    :type photo: :obj:`str`
    """

    def __init__(
        self,
        photo: str = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "photo"
        self.photo = photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["InputStoryContentPhoto"]:
        return (
            InputStoryContentPhoto(
                photo=d.get("photo"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class InputStoryContentVideo(Type_):
    """
    Describes a video to post as a story.

    :param type: Type of the content, always "video"
    :type type: :obj:`str`
    :param video: The video to post as a story. The video must be of the size 720x1280, streamable, encoded with H.265 codec, with key frames added each second in the MPEG4 format, and must not exceed 30 MB.
    :type video: :obj:`str`
    :param duration: Optional. Precise duration of the video in seconds; 0-60
    :type duration: :obj:`float`
    :param cover_frame_timestamp: Optional. Timestamp in seconds of the frame that will be used as the static cover for the story. Defaults to 0.0.
    :type cover_frame_timestamp: :obj:`float`
    :param is_animation: Optional. Pass True if the video has no sound
    :type is_animation: :obj:`bool`
    """

    def __init__(
        self,
        video: str = None,
        duration: float = None,
        cover_frame_timestamp: float = None,
        is_animation: bool = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "video"
        self.video = video
        self.duration = duration
        self.cover_frame_timestamp = cover_frame_timestamp
        self.is_animation = is_animation

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["InputStoryContentVideo"]:
        return (
            InputStoryContentVideo(
                video=d.get("video"),
                duration=d.get("duration"),
                cover_frame_timestamp=d.get("cover_frame_timestamp"),
                is_animation=d.get("is_animation"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
