PACKET = 4
MESSAGE = 14

def is_all_different_chars(buffer :str) -> bool:
    return len(buffer) == len(set(buffer))

'''
Finds index of marker
A packet-marker is identified by 4 consecutive different chars
A message-marker is identified by 14 consecutive different chars
The index returned is the starting index of the message to be passed after the marker
@input buffer: buffer-string
@input msg: type of message
@return first marker after numer of chars
'''
def find_marker_idx(buffer :str, msg) -> int:
    
    for i in range(len(buffer)):
        if is_all_different_chars(buffer[i:i+msg]):
            return i+msg
    else: 
        return None

def test_successful():

    p1 = "bvwbjplbgvbhsrlpgdmjqwftvncz" # first marker after character 5
    p2 = "nppdvjthqldpwncqszvftbrmjlhg" # first marker after character 6
    p3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # first marker after character 10
    p4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" # first marker after character 11

    m1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # first marker after character 19
    m2 = "bvwbjplbgvbhsrlpgdmjqwftvncz" # first marker after character 23
    m3 = "nppdvjthqldpwncqszvftbrmjlhg" # first marker after character 23
    m4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # first marker after character 29
    m5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" # first marker after character 26

    return find_marker_idx(p1, PACKET) == 5 and \
            find_marker_idx(p2, PACKET) == 6 and \
            find_marker_idx(p3, PACKET) == 10 and \
            find_marker_idx(p4, PACKET) == 11 and \
            find_marker_idx(m1, MESSAGE) == 19 and \
            find_marker_idx(m2, MESSAGE) ==23 and \
            find_marker_idx(m3, MESSAGE) == 23 and \
            find_marker_idx(m4, MESSAGE) == 29 and \
            find_marker_idx(m5, MESSAGE) == 26 

def main():
    
    if test_successful():
        with open('input.txt') as input:
            buffer = input.read()
            print("First packet-marker", find_marker_idx(buffer, PACKET))
            print("First message-marker", find_marker_idx(buffer, MESSAGE))
        input.close()
    else:
        print("test failed")


if __name__ == '__main__':
    main()