import tgram

from typing import List, Union


class PostStory:
    async def post_story(
        self: "tgram.TgBot",
        business_connection_id: str,
        content: Union[
            "tgram.types.InputStoryContentPhoto", "tgram.types.InputStoryContentVideo"
        ],
        active_period: int,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        areas: List["tgram.types.StoryArea"] = None,
        post_to_chat_page: bool = None,
        protect_content: bool = None,
    ) -> "tgram.types.Story":
        """
        Posts a story on behalf of a managed business account.
        Requires the can_manage_stories business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#poststory

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :param content: Content of the story
        :type content: :class:`tgram.types.InputStoryContent`

        :param active_period: Period after which the story is moved to the archive, in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400
        :type active_period: :obj:`int`

        :param caption: Caption of the story, 0-2048 characters after entities parsing
        :type caption: :obj:`str`, optional

        :param parse_mode: Mode for parsing entities in the story caption
        :type parse_mode: :obj:`str`, optional

        :param caption_entities: A JSON-serialized list of special entities that appear in the caption
        :type caption_entities: :obj:`list`, optional

        :param areas: A JSON-serialized list of clickable areas to be shown on the story
        :type areas: :obj:`list`, optional

        :param post_to_chat_page: Pass True to keep the story accessible after it expires
        :type post_to_chat_page: :obj:`bool`, optional

        :param protect_content: Pass True if the content of the story must be protected from forwarding and screenshotting
        :type protect_content: :obj:`bool`, optional

        :return: On success, returns a Story object.
        :rtype: :class:`tgram.types.Story`
        """
        result = await self(
            "postStory",
            business_connection_id=business_connection_id,
            content=content,
            active_period=active_period,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            areas=areas,
            post_to_chat_page=post_to_chat_page,
            protect_content=protect_content,
        )
        return tgram.types.Story._parse(me=self, d=result.get("result", {}))
