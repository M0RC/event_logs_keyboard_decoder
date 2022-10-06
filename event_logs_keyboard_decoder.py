import argparse
import struct


qwerty_us = '`1234567890-=qwertyuiop[]asdfghjkl;\'\\\\zxcvbnm,./'
qwerty_uk = '`1234567890-=qwertyuiop[]asdfghjkl;\'#\zxcvbnm,./'
azerty_fr = '²&é"\'(-è_çà)=azertyuiop^$qsdfghjklmù*<wxcvbn,;:!'
azerty_be = '²&é"\'(§è!çà)-azertyuiop^$qsdfghjklmùµ<wxcvbn,;:='

code_list = []
code_dict = {
    0: '[RESERVED]',
    1: '[ESC]',
    2: '1',
    3: '2',
    4: '3',
    5: '4',
    6: '5',
    7: '6',
    8: '7',
    9: '8',
    10: '9',
    11: '0',
    12: '-',
    13: '=',
    14: '[BACKSPACE]',
    15: '[TAB]',
    16: 'q',
    17: 'w',
    18: 'e',
    19: 'r',
    20: 't',
    21: 'y',
    22: 'u',
    23: 'i',
    24: 'o',
    25: 'p',
    26: '^',
    27: '$',
    28: '[ENTER]\n',
    29: '[L_CTRL]',
    30: 'a',
    31: 's',
    32: 'd',
    33: 'f',
    34: 'g',
    35: 'h',
    36: 'j',
    37: 'k',
    38: 'l',
    39: ';',
    40: '!',
    41: '`',
    42: '[L_SHIFT]',
    43: '\\',
    44: 'z',
    45: 'x',
    46: 'c',
    47: 'v',
    48: 'b',
    49: 'n',
    50: 'm',
    51: ',',
    52: '.',
    53: '/',
    54: '[R_SHIFT]',
    55: '*',
    56: '[L_ALT]',
    57: ' ',
    58: '[CAPSLOCK]',
    59: '[F1]',
    60: '[F2]',
    61: '[F3]',
    62: '[F4]',
    63: '[F5]',
    64: '[F6]',
    65: '[F7]',
    66: '[F8]',
    67: '[F9]',
    68: '[F10]',
    69: '[NUMLOCK]',
    70: '[SCROLLLOCK]',
    71: '7',
    72: '8',
    73: '9',
    74: '-',
    75: '4',
    76: '5',
    77: '6',
    78: '+',
    79: '1',
    80: '2',
    81: '3',
    82: '0',
    83: '.',
    84: '',
    85: '[ZENKAKUHANKAKU]',
    86: '<',
    87: '[F11]',
    88: '[F12]',
    89: '[RO]',
    90: '[KATAKANA]',
    91: '[HIRAGANA]',
    92: '[HENKAN]',
    93: '[KATAKANAHIRAGANA]',
    94: '[MUHENKAN]',
    95: '[KPJPCOMMA]',
    96: '[ENTER]\n',
    97: '[R_CTRL]',
    98: '[KPSLASH]',
    99: '[SYSRQ]',
    100: '[R_ALT]',
    101: '[LINEFEED',
    102: '[HOME]',
    103: '[UP]',
    104: '[PAGEUP]',
    105: '[LEFT]',
    106: '[RIGHT]',
    107: '[END]',
    108: '[DOWN]',
    109: '[PAGEDOWN]',
    110: '[INSERT]',
    111: '[DEL]',
    112: '[MACRO]',
    113: '[MUTE]',
    114: '[VOLUMEDOWN]',
    115: '[VOLUMEUP]',
    116: '[POWER]',
    117: '[KPEQUAL]',
    118: '[KPPLUSMINUS]',
    119: '[PAUSE]',
    120: '[SCALE]',
    121: '[KPCOMMA]',
    122: '[HANGEUL]',
    123: '[HANJA]',
    124: '[YEN]',
    125: '[LEFTMETA]',
    126: '[RIGHTMETA]',
    127: '[COMPOSE]',
    128: '[STOP]',
    129: '[AGAIN]',
    130: '[PROPS]',
    131: '[UNDO]',
    132: '[FRONT]',
    133: '[COPY]',
    134: '[OPEN]',
    135: '[PASTE]',
    136: '[FIND]',
    137: '[CUT]',
    138: '[HELP]',
    139: '[MENU]',
    140: '[CALC]',
    141: '[SETUP]',
    142: '[SLEEP]',
    143: '[WAKEUP]',
    144: '[FILE]',
    145: '[SENDFILE]',
    146: '[DELETEFILE]',
    147: '[XFER]',
    148: '[PROG1]',
    149: '[PROG2]',
    150: '[WWW]',
    151: '[MSDOS]',
    152: '[SCREENLOCK]',
    153: '[ROTATE_DISPLAY]',
    154: '[CYCLEWINDOWS]',
    155: '[MAIL]',
    156: '[BOOKMARKS]',
    157: '[COMPUTER]',
    158: '[BACK]',
    159: '[FORWARD]',
    160: '[CLOSECD]',
    161: '[EJECTCD]',
    162: '[EJECTCLOSECD]',
    163: '[NEXTSONG]',
    164: '[PLAYPAUSE]',
    165: '[PREVIOUSSONG]',
    166: '[STOPCD]',
    167: '[RECORD]',
    168: '[REWIND]',
    169: '[PHONE]',
    170: '[ISO]',
    171: '[CONFIG]',
    172: '[HOMEPAGE]',
    173: '[REFRESH]',
    174: '[EXIT]',
    175: '[MOVE]',
    176: '[EDIT]',
    177: '[SCROLLUP]',
    178: '[SCROLLDOWN]',
    179: '[KPLEFTPAREN]',
    180: '[KPRIGHTPAREN]',
    181: '[NEW]',
    182: '[REDO]',
    183: '[F13]',
    184: '[F14]',
    185: '[F15]',
    186: '[F16]',
    187: '[F17]',
    188: '[F18]',
    189: '[F19]',
    190: '[F20]',
    191: '[F21]',
    192: '[F22]',
    193: '[F23]',
    194: '[F24]',
    195: '',
    196: '',
    197: '',
    198: '',
    199: '',
    200: '[PLAYCD]',
    201: '[PAUSECD]',
    202: '[PROG3]',
    203: '[PROG4]',
    204: '[ALL_APPLICATIONS]',
    205: '[SUSPEND]',
    206: '[CLOSE]',
    207: '[PLAY]',
    208: '[FASTFORWARD]',
    209: '[BASSBOOST]',
    210: '[PRINT]',
    211: '[HP]',
    212: '[CAMERA]',
    213: '[SOUND]',
    214: '[QUESTION]',
    215: '[EMAIL]',
    216: '[CHAT]',
    217: '[SEARCH]',
    218: '[CONNECT]',
    219: '[FINANCE]',
    220: '[SPORT]',
    221: '[SHOP]',
    222: '[ALTERASE]',
    223: '[CANCEL]',
    224: '[BRIGHTNESSDOWN]',
    225: '[BRIGHTNESSUP]',
    226: '[MEDIA]',
    227: '[SWITCHVIDEOMODE]',
    228: '[KBDILLUMTOGGLE]',
    229: '[KBDILLUMDOWN]',
    230: '[KBDILLUMUP]',
    231: '[SEND]',
    232: '[REPLY]',
    233: '[FORWARDMAIL]',
    234: '[SAVE]',
    235: '[DOCUMENTS]',
    236: '[BATTERY]',
    237: '[BLUETOOTH]',
    238: '[WLAN]',
    239: '[UWB]',
    240: '[UNKNOWN]',
    241: '[VIDEO_NEXT]',
    242: '[VIDEO_PREV]',
    243: '[BRIGHTNESS_CYCLE]',
    244: '[BRIGHTNESS_AUTO]',
    245: '[DISPLAY_OFF]',
    246: '[WWAN]',
    247: '[RFKILL]',
    248: '[MICMUTE]'
}

def translate_key(translate, code):
    """Translate a key from QWERTY US keyboard to specified keyboard"""

    if code_dict[code] not in qwerty_us:
        return code_dict[code]
    else:
        if code in range(0, 55) or code in range(56, 71) or code in range(84, 249): 
            return code_dict[code].translate(translate)
        else:
            return code_dict[code]

def check_args(parser, args):
    """Check if arguments from parser is valid"""

    try:
        with open(args.file) as f:
            pass
    except PermissionError:
        parser.error("File permission error")
    except FileNotFoundError:
        parser.error("File not found")

def get_args(parser):
    """Create arguments for the program and return parser"""

    parser_group = parser.add_mutually_exclusive_group(required=True)
    parser_group.add_argument('--be', action='store_true', help="For AZERTY Belgium keyboard")
    parser_group.add_argument('--fr', action='store_true', help="For AZERTY French keyboard")
    parser_group.add_argument('--uk', action='store_true', help="For QWERTY UK keyboard")
    parser_group.add_argument('--us', action='store_true', help="For QWERTY US keyboard")
    parser_group.add_argument('--all', '-a', action='store_true', help="Use all keyboards options")
    parser.add_argument('--file', '-f', required=True, type=str, help="Path of file")
    args = parser.parse_args()
	
    return args

def main():
    parser = argparse.ArgumentParser()
    args = get_args(parser)
    check_args(parser, args)

    stopped = False
    with open(args.file, "rb") as f:
        while not stopped:
            try:
                data = f.read(24)
                data = struct.unpack('4IHHI', data)

                if data[4] == 1 and data[6] == 1:
                    code_list.append(data[5])
            except struct.error:
                stopped = True

    if args.be or args.all:
        print("AZERTY BELGIUM Keyboard")
        print("========================")
        translation = str.maketrans(qwerty_us, azerty_be)
        [print(translate_key(translation, code), end='') for code in code_list]
        print("\n\n")
    if args.fr or args.all:
        print("AZERTY FRENCH Keyboard")
        print("========================")
        translation = str.maketrans(qwerty_us, azerty_fr)
        [print(translate_key(translation, code), end='') for code in code_list]
        print("\n\n")
    if args.uk or args.all:
        print("QWERTY UK Keyboard")
        print("========================")
        translation = str.maketrans(qwerty_us, qwerty_uk)
        [print(translate_key(translation, code), end='') for code in code_list]
        print("\n\n")
    if args.us or args.all:
        print("QWERTY US Keyboard")
        print("========================")
        [print(code_dict[code], end='') for code in code_list]
        print("")


if __name__ == '__main__':
    main()
