import curses
from curses import wrapper

def drawMap(y, x, screen, array):
	for i in array:
		screen.addstr(y, x, i)
		y = y + 1
		
			
def main(window):
	
	maze = [u'┌────────┐', 
			u'│        │',
			u'│        │',
			u'└────────┘']

	playerY = 3
	playerX = 3

	
	#Setup Window
	window = curses.initscr()
	curses.noecho()
	curses.cbreak()
	curses.curs_set(False)	
	window.keypad(True)

	drawMap(1, 1, window, maze)
	while True:
		keypress = window.getch()
		try:
			if keypress == ord('w'):
				if chr(window.inch(playerY - 1, playerX)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY - 1, playerX, u'o')
					playerY = playerY - 1
				else: 
					pass
			if keypress == ord('s'):
				if chr(window.inch(playerY + 1, playerX)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY + 1, playerX, u'o')
					playerY = playerY + 1	
				else:
					pass
			if keypress == ord('a'):
				if chr(window.inch(playerY, playerX - 1)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX - 1, u'o')
					playerX = playerX - 1			
				else:
					pass
			if keypress == ord('d'):
				if chr(window.inch(playerY, playerX + 1)) == ' ':
					window.addch(playerY, playerX, ' ')
					window.addstr(playerY, playerX + 1, u'o')	
					playerX = playerX + 1		
				else:
					pass
		except(curses.error):
			pass
wrapper(main)
