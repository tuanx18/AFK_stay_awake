
import time
import random
import pyautogui
import keyboard

def keep_awake(duration_hours=8, move_interval=30, key_interval=120):
    """
    Prevent system sleep by random mouse moves and key presses.
    duration_hours: total hours to run
    move_interval: seconds between mouse moves
    key_interval: seconds between key presses
    """
    end_time = time.time() + duration_hours * 3600
    print(f"Keep-awake started for {duration_hours} hours...")
    
    last_key_time = time.time()
    
    while time.time() < end_time:
        # Random small mouse movement
        x_move = random.randint(-10, 10)
        y_move = random.randint(-10, 10)
        pyautogui.moveRel(x_move, y_move, duration=0.2)  # smooth move
        print(f"Mouse moved by ({x_move}, {y_move})")
        
        # Every key_interval seconds, press a harmless key
        if time.time() - last_key_time >= key_interval:
            keyboard.press_and_release('shift')  # harmless key
            print("Pressed Shift key")
            last_key_time = time.time()
        
        # Optional: random scroll
        if random.random() < 0.1:  # 10% chance
            scroll_amount = random.choice([-1, 1])
            pyautogui.scroll(scroll_amount)
            print(f"Scrolled {scroll_amount}")
        
        time.sleep(move_interval)
    
    print("Keep-awake finished.")

if __name__ == "__main__":
    keep_awake(duration_hours=9, move_interval=30, key_interval=120)
