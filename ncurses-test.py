import curses
from curses import wrapper



def main(window):
	
	
	playerY = 1
	playerX = 1
	borders = [u'─', u'│', u'┌', u'┐', u'└', u'┘', u'├', u'├']
	
	#Setup Window
	window = curses.initscr()
	curses.noecho()
	curses.cbreak()
	curses.curs_set(False)	
	window.keypad(True)

	while True:
		window.addch(10, 10, '1')
		keypress = window.getch()
		try:
			if keypress == ord('w'):
				if chr(window.inch(playerY - 1, playerX)) != '1':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY - 1, playerX, u'😀')
					playerY = playerY - 1
			if keypress == ord('s'):
				if chr(window.inch(playerY + 1, playerX)) != '1':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY + 1, playerX, u'😀')
					playerY = playerY + 1	
			if keypress == ord('a'):
				if chr(window.inch(playerY, playerX - 1)) != '1':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX - 1, u'😀')
					playerX = playerX - 1			
			if keypress == ord('d'):
				if chr(window.inch(playerY, playerX + 1)) != '1':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX + 1, u'😀')	
					playerX = playerX + 1		
		except(curses.error):
			pass
wrapper(main)
