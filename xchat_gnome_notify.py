__module_name__ = "gnome-notify"
__module_version__ = "0.1"
__module_description__ = "Notifies you when someone mentions your nick"

import xchat
import pygtk
pygtk.require('2.0')
import pynotify

irc_nick_re = r'(?<=[^a-z_\-\[\]\\^{}|`])[a-z_\-\[\]\\^{}|`][a-z0-9_\-\[\]\\^{}|`]*'

def mention_cb(word, word_eol, userdata):
    nick, line = word[:2]
    notify("XChat", "%s says: %s" % (nick, line))

def notify(title, msg):
    global notification
    if notification is None:
        notification = pynotify.Notification(title, msg)
    else:
        notification.update(title, msg)
    notification.set_timeout(pynotify.EXPIRES_DEFAULT)
    notification.show()

events = (
    "Channel Msg Hilight",
)

for event in events:
    xchat.hook_print(event, mention_cb, event)

notification = None
if not pynotify.init("XChat"):
    raise Exception("Could not initialize pynotify")


xchat.prnt("Loaded %s %s" % (__module_name__, __module_version__))
