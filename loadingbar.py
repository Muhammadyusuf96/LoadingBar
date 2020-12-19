"""Draw loadingbar.

Attributes:
    bars (TYPE): List of bars you can use.
    Loading (TYPE): Description
    thrd (TYPE): Description

Deleted Attributes:
    L (TYPE): Description
    t (TYPE): Description
"""
import sys
import time
# Create and launch a thread
from threading import Thread


bars = [
    '01234567890123456789',
    '.                   ',
    'Loading...          ',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒',
    '▒▓█▓▒░░░░░░░░░░░░░',
    '█▓▒░░▒▓████████████████',
    '░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░ ',
    '░▒▓█▓▒                  ',
    '█▓▒░ ░▒▓████████████████']


class LoadingBar:
    """A Loading bar class."""

    def __init__(self):
        """Class initialization."""
        self._running = True
        self._to_right = True
        self._speed = 24

    def stop(self):
        """Stop the drawing."""
        self._running = False

    def change_direction(self):
        """Change the direction."""
        self._to_right = not self._to_right

    def change_speed(self, speed: int):
        """Change the speed.

        Args:
            speed (int): Update FPS
        """
        self._speed = speed

    def start(self, load_bar: str):
        """Start the drawing.

        Args:
            load_bar (str): Bar
        """
        while self._running and len(load_bar) > 0:
            for i in range(len(load_bar)):
                if self._to_right:
                    sys.stdout.write('\r' + load_bar[-i:] + load_bar[:-i])
                else:
                    sys.stdout.write('\r' + load_bar[i:] + load_bar[:i])
                sys.stdout.flush()
                time.sleep(1 / self._speed)


Loading = LoadingBar()

thrd = Thread(target=Loading.start, args=(bars[5], ))
thrd.start()

time.sleep(5)

# Change direction
Loading.change_direction()

time.sleep(5)

# Change direction
Loading.change_direction()

# Change the speed
Loading.change_speed(50)
time.sleep(5)

# Signal termination
Loading.stop()

# Wait for actual termination (if needed)
thrd.join()
