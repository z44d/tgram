# Security Policy

## Security Responsibility

The security of your bots and their implementations using Tgram is **your responsibility**. While we ensure that the Tgram library is free of vulnerabilities and provide updates for the latest version, how you configure, deploy, and secure your bots is beyond our scope.

## Guidelines for Securing Your Bots

To help maintain the security of your bots, consider the following recommendations:

1. **Keep Tgram Updated**  
   Always use the latest version of Tgram to benefit from the latest security patches and features.

2. **Secure API Tokens**  
   - Never hardcode your API tokens in public repositories.
   - Use environment variables or secure vaults to manage sensitive data.

3. **Restrict Access**  
   - Limit the permissions of your bot to only what is necessary.
   - Avoid granting unnecessary administrative privileges.

4. **Validate User Input**  
   - Sanitize and validate all user inputs to prevent injection attacks.
   - Avoid executing user-provided commands without strict validation.

5. **Monitor Logs and Usage**  
   - Regularly review logs to detect suspicious activities.
   - Use rate limiting to prevent abuse.

6. **Enable HTTPS**  
   If your bot interacts with external servers, ensure all communication is secured with HTTPS.

7. **Follow Telegram’s Best Practices**  
   Refer to Telegram's [faq](https://core.telegram.org/bots/faq) for additional tips.

## Reporting Issues

If you encounter a bug or suspect a vulnerability in Tgram itself, please report it responsibly by texting [Bot Support](https://telegram.me/botsupport). For vulnerabilities in your bot, refer to your bot's security policy or maintainers.

Thank you for taking the necessary steps to secure your bots and keeping the ecosystem safe!

