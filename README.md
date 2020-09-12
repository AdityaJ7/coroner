## Coroner

A simple tool used to determine when your favorite twitch streamers go live.


---
#### Setup

1. `python3 -m venv ./venv`
2. `source setup.sh`
3. pip install -r requirements.txt
4. Create a file: `config/secret.json` and put the following into it

```javascript

{
    "client_id": <YOUR_TWITCH_CLIENT_ID>
}
```


---
#### Testing

1. Simply run `pytest` in the root project directory


---
#### Requirements:

- python3-devel
- openssl-devel
- libcurl-devel
