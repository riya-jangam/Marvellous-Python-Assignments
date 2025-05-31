import threading

# Thread for counting lowercase characters
def count_small(s):
    count = sum(1 for ch in s if ch.islower())
    print(f"[{threading.current_thread().name}] ID: {threading.get_ident()} - Small letters: {count}")

# Thread for counting uppercase characters
def count_capital(s):
    count = sum(1 for ch in s if ch.isupper())
    print(f"[{threading.current_thread().name}] ID: {threading.get_ident()} - Capital letters: {count}")

# Thread for counting digits
def count_digits(s):
    count = sum(1 for ch in s if ch.isdigit())
    print(f"[{threading.current_thread().name}] ID: {threading.get_ident()} - Digits: {count}")

# Main execution
if __name__ == "__main__":
    # Take input from user
    input_str = input("Enter a string: ")

    # Create threads with names
    t1 = threading.Thread(target=count_small, args=(input_str,), name="SmallThread")
    t2 = threading.Thread(target=count_capital, args=(input_str,), name="CapitalThread")
    t3 = threading.Thread(target=count_digits, args=(input_str,), name="DigitThread")

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for threads to complete
    t1.join()
    t2.join()
    t3.join()
