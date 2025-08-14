from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton(" ᴄʜᴀᴛ-ɢᴘᴛ ", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton(" ɢʀᴏᴜᴘs ", callback_data="mplus HELP_Group"),InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("ᴛᴀɢ-ᴀʟʟ ", callback_data="mplus HELP_TagAll")],
    [InlineKeyboardButton(" ᴀᴄᴛɪᴏɴ ", callback_data="mplus HELP_Action")],    
    [InlineKeyboardButton(" ғᴏɴᴛ ", callback_data="mplus HELP_Font"),
    InlineKeyboardButton(" ᴛ-ɢʀᴀᴘʜ ", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton(" ɪᴍᴘᴏsᴛᴇʀ ", callback_data="mplus HELP_Imposter")],          
    [InlineKeyboardButton("<🔘", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton("🔘>", callback_data=f"managebot123 settings_back_helper"),
    ]]
    
