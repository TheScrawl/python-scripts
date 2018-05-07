import curses
from curses import wrapper


def main(window):
	
	
	playerY = 0
	playerX = 0
	
	#Setup Window
	window = curses.initscr()
	curses.noecho()
	curses.cbreak()
	curses.curs_set(False)	
	window.keypad(True)
	window.border(0)

	while True:
		
		keypress = window.getch()
		try:
			if keypress == ord('w'):
				window.addch(playerY, playerX, ' ')
				window.addch(playerY - 1, playerX, 'x')
				playerY = playerY - 1
			if keypress == ord('s'):
				window.addch(playerY, playerX, ' ')
				window.addch(playerY + 1, playerX, 'x')
				playerY = playerY + 1	
			if keypress == ord('a'):
				window.addch(playerY, playerX, ' ')
				window.addch(playerY, playerX - 1, 'x')
				playerX = playerX - 1			
			if keypress == ord('d'):
				window.addch(playerY, playerX, ' ')
				window.addch(playerY, playerX + 1, 'x')	
				playerX = playerX + 1		
		except(curses.error):
			pass
wrapper(main)
