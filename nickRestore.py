###SETTINGS###
password = ''   # Contraseña usada con NickServ.
##############

import hexchat

__module_name__ = 'nickRestore'
__module_version__ = '1.0'
__module_description__ = 'Restaura tu nick principal registrado cuando aún está en uso (GHOST) tras una reconexión.'
__module_author__ = 'Wibol'
__hexchat_version__ = hexchat.get_info('version')

def restore_cb(word, word_eol, userdata):
    original = hexchat.get_prefs('irc_nick1')
    hexchat.command('TIMER 6 MSG NickServ GHOST {} {}'.format(original, password))
    hexchat.command('TIMER 16 NICK {}'.format(original))
    hexchat.command('TIMER 18 MSG ChanServ OP')
    return hexchat.EAT_PLUGIN

hexchat.hook_print('Nick Clash', restore_cb)
hexchat.hook_command('restore', restore_cb, help='Restaura el nick original registrado.')

hexchat.prnt(' * {} {} de {} cargado con éxito en Hexchat {}. {}'.format(__module_name__, __module_version__, __module_author__, __hexchat_version__, __module_description__))
