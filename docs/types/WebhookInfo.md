#🔮 WebhookInfo

**Describes the current status of a webhook.**

##⚙️ Properties

- **`url`** (**`str`** ): **Webhook URL, may be empty if webhook is not set up**
- **`has_custom_certificate`** (**`bool`** ): **True, if a custom certificate was provided for webhook certificate checks**
- **`pending_update_count`** (**`int`** ): **Number of updates awaiting delivery**
- **`ip_address`** (**`str`** ): **Optional. Currently used webhook IP address**
- **`last_error_date`** (**`int`** ): **Optional. Unix time for the most recent error that happened when trying to deliver an
update via webhook**
- **`last_error_message`** (**`str`** ): **Optional. Error message in human-readable format for the most recent error that
happened when trying to deliver an update via webhook**
- **`last_synchronization_error_date`** (**`int`** ): **Optional. Unix time of the most recent error that happened when trying
to synchronize available updates with Telegram datacenters**
- **`max_connections`** (**`int`** ): **Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook
for update delivery**
- **`allowed_updates`** (**List of `str`** ): **Optional. A list of update types the bot is subscribed to. Defaults to all update types
except chat_member**
