import board
from kmk.modules.split import Split, SplitType, SplitSide

split = Split(
    split_flip=True,
	data_pin=board.RX, 
	data_pin2=board.TX,
	use_pio=True,
	uart_flip=False
	)