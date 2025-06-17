import tgram

from typing import List


class EditStory:
    async def edit_story(
        self: "tgram.TgBot",
        business_connection_id: str,
        story_id: int,
        content: "tgram.types.InputStoryContent",
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List["tgram.types.MessageEntity"] = None,
        areas: List["tgram.types.StoryArea"] = None,
    ) -> "tgram.types.Story":
        """
        Edits a story previously posted by the bot on behalf of a managed business account.
        Requires the can_manage_stories business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#editstory

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :param story_id: Unique identifier of the story to edit
        :type story_id: :obj:`int`

        :param content: Content of the story
        :type content: :class:`tgram.types.InputStoryContent`

        :param caption: Caption of the story, 0-2048 characters after entities parsing
        :type caption: :obj:`str`, optional

        :param parse_mode: Mode for parsing entities in the story caption
        :type parse_mode: :obj:`str`, optional

        :param caption_entities: A JSON-serialized list of special entities that appear in the caption
        :type caption_entities: :obj:`list`, optional

        :param areas: A JSON-serialized list of clickable areas to be shown on the story
        :type areas: :obj:`list`, optional

        :return: On success, returns a Story object.
        :rtype: :class:`tgram.types.Story`
        """
        result = await self(
            "editStory",
            business_connection_id=business_connection_id,
            story_id=story_id,
            content=content,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            areas=areas,
        )
        return tgram.types.Story._parse(me=self, d=result["result"])
