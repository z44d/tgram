import tgram


class DeleteStory:
    async def delete_story(
        self: "tgram.TgBot",
        business_connection_id: str,
        story_id: int,
    ) -> bool:
        """
        Deletes a story previously posted by the bot on behalf of a managed business account.
        Requires the can_manage_stories business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#deletestory

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :param story_id: Unique identifier of the story to delete
        :type story_id: :obj:`int`

        :return: True on success.
        :rtype: :obj:`bool`
        """
        result = await self(
            "deleteStory",
            business_connection_id=business_connection_id,
            story_id=story_id,
        )
        return result.get("result", {})
