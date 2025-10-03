#🔮 ChatInviteLink

**Represents an invite link for a chat.**

##⚙️ Properties

- **`invite_link`** (**`str`** ): **The invite link. If the link was created by another chat administrator, then the second part of
the link will be replaced with “…”.**
- **`creator`** (**[User](User.md)** ): **Creator of the link**
- **`creates_join_request`** (**`bool`** ): **True, if users joining the chat via the link need to be approved by chat administrators**
- **`is_primary`** (**`bool`** ): **True, if the link is primary**
- **`is_revoked`** (**`bool`** ): **True, if the link is revoked**
- **`name`** (**`str`** ): **Optional. Invite link name**
- **`expire_date`** (**`int`** ): **Optional. Point in time (Unix timestamp) when the link will expire or has been expired**
- **`member_limit`** (**`int`** ): **Optional. The maximum number of users that can be members of the chat simultaneously after
joining the chat via this invite link; 1-99999**
- **`pending_join_request_count`** (**`int`** ): **Optional. Number of pending join requests created using this link**
