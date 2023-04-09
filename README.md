# EvilLuffy Bot

EvilLuffy Bot is a Reddit bot that responds to comments containing the word "meat" in the r/MemePiece subreddit with quotes from Evil Luffy.

## How it works

The bot uses the PRAW (Python Reddit API Wrapper) library to monitor comments in the r/MemePiece subreddit. When a comment contains the word "meat", the bot randomly selects a quote from a list of Evil Luffy quotes and replies to the comment with the selected quote.

## Usage

To use the EvilLuffy Bot, simply mention the word "meat" in a comment on the r/MemePiece subreddit. If the bot is running, it will reply to your comment with a random Evil Luffy quote.

## Getting started

1. Clone the repository: `git clone https://github.com/<username>/<repository-name>.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create a Reddit app and obtain your client ID, client secret, username, and password. See [these instructions](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) for details.
4. Create a `.env` file in the root directory of the repository with the following content:

client_id=<your-client-id>
client_secret=<your-client-secret>
username=<your-username>
password=<your-password>
user_agent=<your-user-agent>


Replace `<your-client-id>`, `<your-client-secret>`, `<your-username>`, `<your-password>`, and `<your-user-agent>` with your actual values.

5. Run the bot: `python main.py`

## Contributing

Contributions are welcome! If you find a bug or have a suggestion, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


