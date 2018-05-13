import curses
from curses import wrapper

def drawMap(array, screen):
	x = 1
	y = 1
	for c in array:
		if c == 'newline':
			y = y + 1
			x = 1 
		elif isinstance(c, str) and c != 'newline':
			screen.addstr(y, x, c)
			x = x + len(c)
		elif isinstance(c, int):
			x = x + c

def main(window):
	
	maze = [u'──────────','newline', 
			u'│', 8, u'│', 'newline',
			u'│', 8, u'│', 'newline',
			u'──────────']

	playerY = 3
	playerX = 3
	borders = [u'─', u'━', u'│', u'┃', u'┄', u'┅', u'┆', u'┇', u'┈', u'┉', u'┊', u'┋', u'┌', u'┍', u'┎', u'┏',  u'┐', u'┑', u'┒', u'┓', u'└', u'┕', u'┖', u'┗', u'┘', u'┙', u'┚', u'┛', u'├', u'┝', u'┞', u'┟', u'┠', u'┡', u'┢', u'┣', u'┤', u'┥', u'┦', u'┧', u'┨', u'┩', u'┪', u'┫', u'┬', u'┭', u'┮', u'┯', u'┰', u'┱', u'┲', u'┳', u'┴', u'┵', u'┶', u'┷', u'┸', u'┹', u'┺', u'┻', u'┼', u'┽', u'┾', u'┿', u'╀', u'╁', u'╂', u'╃', u'╄', u'╅', u'╆', u'╇', u'╈', u'╉', u'╊', u'╋', u'╌', u'╍', u'╎', u'╏', u'═', u'║', u'╒', u'╓', u'╔', u'╕', u'╖', u'╗', u'╘', u'╙', u'╚', u'╛', u'╜', u'╝', u'╞', u'╟', u'╠', u'╡', u'╢', u'╣', u'╤', u'╥', u'╦', u'╧', u'╨', u'╩', u'╪', u'╫', u'╬', u'╭', u'╮', u'╯', u'╰', u'╱', u'╲', u'╳', u'╴', u'╵', u'╶', u'╷', u'╸', u'╹', u'╺', u'╻', u'╼', u'╽', u'╾', u'╿']

	
	#Setup Window
	window = curses.initscr()
	curses.noecho()
	curses.cbreak()
	curses.curs_set(False)	
	window.keypad(True)

	drawMap(maze, window)
	while True:
		keypress = window.getch()
		try:
			if keypress == ord('w'):
				if chr(window.inch(playerY - 1, playerX)) not in borders:
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY - 1, playerX, u'o')
					playerY = playerY - 1
				else: 
					pass
			if keypress == ord('s'):
				if chr(window.inch(playerY + 1, playerX)) not in borders:
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY + 1, playerX, u'o')
					playerY = playerY + 1	
				else:
					pass
			if keypress == ord('a'):
				if chr(window.inch(playerY, playerX - 1)) not in borders:
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX - 1, u'o')
					playerX = playerX - 1			
				else:
					pass
			if keypress == ord('d'):
				if chr(window.inch(playerY, playerX + 1)) not in borders:
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX + 1, u'o')	
					playerX = playerX + 1		
				else:
					pass
		except(curses.error):
			pass
wrapper(main)
