from utils.io import read_input

def detect_message_index(msg: str, distinct_char: int) -> int:

    return (
        [
            len(set(msg[i:i+distinct_char]))
            for i in range(len(msg) - distinct_char + 1)
        ]
    ).index(distinct_char) + distinct_char

data = read_input(day=6)[0]

start_of_packet = detect_message_index(msg=data, distinct_char=4)
print(f"Characters processed before first start-of-packet: {start_of_packet}")

start_of_msg = detect_message_index(msg=data, distinct_char=14)
print(f"Characters processed before first start-of-message: {start_of_msg}")