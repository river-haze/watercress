print("Starting")

import board
print(dir(board))

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.combos import Chord, Combos, Sequence
from kmk.modules.string_substitution import StringSubstitution
from kmk.handlers.sequences import simple_key_sequence

from kb import split

keyboard = KMKKeyboard()
keyboard.col_pins = [
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
]
keyboard.row_pins = [
    board.D9,
    board.D10,
    board.D8,
]
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.coord_mapping = [
    0,  1,  2,  3,  4,    19, 18, 17, 16, 15, 
    5,  6,  7,  8,  9,    24, 23, 22, 21, 20,
       11, 12, 13, 14,    29, 28, 27, 26
]

my_dictionary = {
    'qh': 'qu',
    'Qh': 'Qu',
    'jn': 'ju',
    'Jn': 'Ju'
}

keyboard.modules.append(split)
keyboard.modules.append(Layers())
combos = Combos()
combos.timeout = 3
keyboard.modules.append(combos)
string_substitution = StringSubstitution(dictionary=my_dictionary)
keyboard.modules.append(string_substitution)

ACTION = KC.MO(2)
QWERTY = KC.TG(1)
FUNKEY = KC.TG(3)
DIW = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.LEFT,
        KC.RIGHT,
        KC.BSPC,
        KC.LCTL(no_press=True),
    )
)

combos.combos = [
    #MODS
    #shift
    Chord((7, 11), KC.LSFT, match_coord=True),
    Chord((22, 26), KC.LSFT, match_coord=True),
    #control
    Chord((6, 12), KC.LCTL, match_coord=True),
    Chord((21, 27), KC.LCTL, match_coord=True),
    #super
    Chord((8, 13), KC.LGUI, match_coord=True),
    Chord((23, 28), KC.LGUI, match_coord=True),
    #alt
    Chord((4, 9), KC.LALT, match_coord=True),
    Chord((19, 24), KC.LALT, match_coord=True),
    #END MODS
    
    #EDITTING
    #backspace
    Chord((27, 26), KC.BSPC, match_coord=True),
    #delete
    Chord((28, 27), KC.DEL, match_coord=True),
    #tab
    Chord((17, 22), KC.TAB, match_coord=True),
    #escape
    Chord((28, 27, 26), KC.ESC, match_coord=True),
    #enter
    Chord((11, 7, 8), KC.ENT, match_coord=True),
    Chord((23, 22, 26), KC.ENT, match_coord=True),
    #delete previous word
    Chord((7, 8, 23, 22), KC.LCTL(KC.BSPC), match_coord=True),
    Chord((7, 8, 22, 21), DIW, match_coord=True),
    #END EDITTING
    
    #NAV
    #arrows
    Chord((18, 23), KC.LEFT, match_coord=True),
    Chord((16, 21), KC.RGHT, match_coord=True),
    Chord((16, 17, 18), KC.UP, match_coord=True),
    Chord((21, 22, 23), KC.DOWN, match_coord=True),
    #home end
    Chord((18, 17, 21), KC.HOME, match_coord=True),
    Chord((17, 16, 23), KC.END, match_coord=True),
    #END NAV
    
    #SYM
    Chord((KC.LPRN, KC.DOT), KC.LCBR),
    Chord((KC.RPRN, KC.SCLN), KC.RCBR),
    Chord((KC.LPRN, KC.RPRN), KC.LBRC),
    Chord((KC.DOT, KC.SCLN), KC.RBRC),
    Chord((KC.LPRN, KC.SCLN), KC.LABK),
    Chord((KC.RPRN, KC.DOT), KC.RABK),
    #END SYM
    
    #NUM
    Chord((1, 6), KC.N1, match_coord=True),
    Chord((2, 7), KC.N2, match_coord=True),
    Chord((3, 8), KC.N3, match_coord=True),
    Chord((1, 2, 3), KC.N4, match_coord=True),
    Chord((6, 7, 8), KC.N5, match_coord=True),
    Chord((1, 2, 8), KC.N6, match_coord=True),
    Chord((6, 2, 3), KC.N7, match_coord=True),
    Chord((1, 2, 6, 7), KC.N8, match_coord=True),
    Chord((2, 3, 7, 8), KC.N9, match_coord=True),
    Chord((6, 7, 3), KC.N0, match_coord=True),
    #END NUM
    
    #LAYOUT
    Chord((5, 8, 23, 20), QWERTY, match_coord=True),
    #END LAYOUT
    
    #CAPSWORD
    Chord((6, 2, 8), KC.CAPS, match_coord=True),
    #END CAPSWORD
    
    #FUNCTION KEY LAYER CHORD
    Chord((21, 23, 17), FUNKEY, match_coord=True),
    #END FUNCTION KEY LAYER CHORD
    
]

keyboard.keymap = [
	[
		KC.W,   KC.L,   KC.F,   KC.M,   KC.K,          KC.Z,   KC.B,   KC.U,   KC.O,   KC.Y,   
		KC.C,   KC.R,   KC.S,   KC.T,   KC.G,          KC.P,   KC.N,   KC.E,   KC.A,   KC.I,   
		        KC.X,   KC.V,   KC.D,   ACTION,        KC.SPC, KC.H,   KC.J,   KC.Q,
	],
    [
		KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,          KC.Y,   KC.U,   KC.I,   KC.O,   KC.J,   
		KC.A,   KC.S,   KC.D,   KC.F,   KC.G,          KC.H,   KC.N,   KC.K,   KC.L,   KC.P,  
		        KC.X,   KC.C,   KC.V,   ACTION,        KC.SPC, KC.M,   KC.B,   KC.Z,
	],
    [
		KC.AMPR,KC.PIPE,KC.LPRN,KC.RPRN,KC.CIRC,       KC.ASTR,KC.MINS,KC.UNDS,KC.EQL, KC.PLUS,   
		KC.QUOT,KC.QUES,KC.DOT, KC.SCLN,KC.BSLS,       KC.SLSH,KC.COLN,KC.COMM,KC.EXLM,KC.DQUO,   
		        KC.AT,  KC.DLR, KC.PERC,KC.TRNS,       KC.TRNS,KC.HASH,KC.GRV, KC.TILD,
	],
    [
		KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,         KC.F11, KC.F7,  KC.F8,  KC.F9, KC.NO,   
		KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,         KC.F10, KC.F4,  KC.F5,  KC.F6, KC.F12,   
		        KC.NO,  KC.NO,  KC.NO,  KC.NO,         FUNKEY,KC.F1,  KC.F2,  KC.F3,
	],
]



if __name__  == '__main__':
	keyboard.go()
