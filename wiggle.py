# wiggle.py
import mouse
import time

if __name__ == "__main__":
    while True:
        time.sleep(60)
        mouse.move(5, 5, absolute=False, duration = 0.005)
        mouse.move(-5, -5, absolute=False, duration = 0.005)