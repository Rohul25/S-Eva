class script(object):

START_TXT = """𝑯𝒆𝒍𝒍𝒐 **{}**,
𝑻𝒉𝒂𝒏𝒌𝒔 𝑭𝒐𝒓 𝑼𝒔𝒊𝒏𝒈 𝑴𝒆 🤩. 𝑰 𝒂𝒎 𝒂 𝒑𝒐𝒘𝒆𝒓𝒇𝒖𝒍 𝑨𝒖𝒕𝒐-𝑭𝒊𝒍𝒕𝒆𝒓 𝒃𝒐𝒕 𝑾𝒐𝒓𝒌𝒊𝒏𝒈 24𝒙7.
𝑱𝒖𝒔𝒕 𝑪𝒍𝒊𝒄𝒌 𝑩𝒆𝒍𝒐𝒘 𝑩𝒖𝒕𝒕𝒐𝒏, 𝑨𝒅𝒅 𝑴𝒆 𝒂𝒔 𝑨𝒅𝒎𝒊𝒏. 𝑻𝒉𝒂𝒕'𝒔 𝒊𝒕 𝑰 𝒘𝒊𝒍𝒍 𝑷𝒓𝒐𝒗𝒊𝒅𝒆 𝑴𝒐𝒗𝒊𝒆𝒔 𝑰𝒏 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑.
𝑴𝒂𝒊𝒏𝒕𝒂𝒊𝒏𝒆𝒅 𝑩𝒚 - **@ViralBeatz**
"""
    HELP_TXT = """🚩 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴏᴅᴜʟᴇs"""
    ABOUT_TXT = """
**🤖 ʙᴏᴛ ɴᴀᴍᴇ: ɢʀɪғғɪɴ 

📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 

📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏʀᴏɢʀᴀᴍ

📡 ʜᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ 

📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ : @ViralBeatz**"""
    SOURCE_TXT = """Sorry It's Private Bot. 
Made By - @ViralBeatz"""
    <b>DEVS:</b>

- <a href=https://t.me/belikeberlin>Berlin ✨❣️</a>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and SM18FILTERbot will respond whenever a keyword is found the message

<b>NOTE:</b>

1. SM18FILTERBOT should have admin privillage.

2. only admins can add filters in a chat.

3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>

• /filter - <code>add a filter in chat</code>

• /filters - <code>list all the filters of a chat</code>

• /del - <code>delete a specific filter in chat</code>

• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- SM18FILTERBOT Supports both url and alert inline buttons.

<b>NOTE:</b>

1. Telegram will not allows you to send buttons without any content, so content is mandatory.

2. SM18FILTERBOT supports buttons with any telegram media type.

3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>

<code>[Button Text](buttonurl:https://t.me/SM18FILTERbot)</code>

<b>Alert buttons:</b>

<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>

1. Make me the admin of your channel if it's private.

2. make sure that your channel does not contains camrips, porn and fake files.

3. Forward the last message to me with quotes.

 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 

- it helps to avoid spamming in groups.

<b>NOTE:</b>

1. Only admins can add a connection.

2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>

• /connect  - <code>connect a particular chat to your PM</code>

• /disconnect  - <code>disconnect from a chat</code>

• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>

these are the extra features of SM18FILTERBOT 

<b>Commands and Usage:</b>

• /id - <code>get id of a specified user.</code>

• /info  - <code>get information about a user.</code>

• /imdb  - <code>get the film information from IMDb source.</code>

• /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>

This module only works for my admins

<b>Commands and Usage:</b>

• /logs - <code>to get the rescent errors</code>

• /stats - <code>to get status of files in db.</code>

• /delete - <code>to delete a specific file from db.</code>

• /users - <code>to get list of my users and ids.</code>

• /chats - <code>to get list of the my chats and ids </code>

• /leave  - <code>to leave from a chat.</code>

• /disable  -  <code>do disable a chat.</code>

• /ban  - <code>to ban a user.</code>

• /unban  - <code>to unban a user.</code>

• /channel - <code>to get list of total connected channels</code>

• /broadcast - <code>to broadcast a message to all users</code>"""

    STATUS_TXT = """📁 ᴛᴏᴛᴀʟ ꜰɪʟᴇs: <code>{}</code>

👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>

👥 ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>

⚙️ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱

🆓 ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱"""

    LOG_TEXT_G = """#NewGroup

Group = {}(<code>{}</code>)

Total Members = <code>{}</code>

Added By - {}

"""

    LOG_TEXT_P = """#NewUser

ID - <code>{}</code>

Name - {}

"""
