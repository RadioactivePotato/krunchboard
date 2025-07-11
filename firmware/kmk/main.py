import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.mcp23017 import MCP23017

i2c = busio.I2C(scl=board.GP1, sda=board.GP0)

mcp = MCP23017(i2c, address=0x20)

keyboard = KMKKeyboard()

display = Display(
    display=SSD1306(sda=board.GP0, scl=board.GP1),
    entries=[TextEntry(text='Hello World')],
    height=32,
)
keyboard.extensions.append(display)

keyboard.col_pins = (
    board.GP21, # C0
    board.GP22,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP16,
    board.GP17,
    board.GP18, # C18
)

keyboard.row_pins = (
    mcp.P0, # R0
    mcp.P1,
    mcp.P2,
    mcp.P3,
    mcp.P4,
    mcp.P5, # R5
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.NO, KC.NO, KC.PSCR, KC.SCRLK, KC.PAUSE, KC.MUTE],
    [KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.NO, KC.BSPACE, KC.INSERT, KC.HOME, KC.PGUP, KC.NO],
    [KC.TAB, KC.NO, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.NO, KC.DEL, KC.END, KC.PGDN, KC.NO], 
    [KC.KCAP, KC.NO, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOTE, KC.HASH, KC.ENTER, KC.NO, KC.NO, KC.NO, KC.NO],
    [KC.LSHIFT, KC.BSLASH, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.NO, KC.RSHIFT, KC.NO, KC.NO, KC.UP, KC.NO, KC.NO],
    [KC.LCTRL, KC.NO, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.NO, KC.RALT, KC.RGUI, KC.NO, KC.APP, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO]
]

if __name__ == '__main__':
    keyboard.go()
