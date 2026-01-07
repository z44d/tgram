import tgram
from tgram.types import Story


class RepostStory:
    async def repost_story(
        self: "tgram.TgBot",
        business_connection_id: str,
        story_sender_chat_id: int,
        story_id: int,
    ) -> Story:
        """
        Use this method to repost a story from one business account to another.
        Requires the can_post_stories business bot right in both chats.
        Returns the reposted Story on success.

        Telegram documentation: https://core.telegram.org/bots/api#repoststory

        :param business_connection_id: Unique identifier of the business connection on behalf
            of which the story will be reposted
        :type business_connection_id: :obj:`str`
        :param story_sender_chat_id: Unique identifier of the chat that originally posted the story
        :type story_sender_chat_id: :obj:`int`
        :param story_id: Unique identifier of the story to repost
        :type story_id: :obj:`int`

        :return: Returns the reposted Story on success.
        :rtype: :class:`tgram.types.Story`
        """
        result = await self(
            "repostStory",
            business_connection_id=business_connection_id,
            story_sender_chat_id=story_sender_chat_id,
            story_id=story_id,
        )
        return Story._parse(me=self, d=result["result"])
