import requests

token = "YOUR TOKEN"
guild_id = "CTF_SERVER_ID"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Authorization': token,
    'Content-Type': 'application/json'
}

response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers = headers)
print(response.text)
