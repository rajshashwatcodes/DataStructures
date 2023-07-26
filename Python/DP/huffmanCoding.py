import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(data):
    frequency = Counter(data)
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)

        internal_node = HuffmanNode(None, left_child.frequency + right_child.frequency)
        internal_node.left = left_child
        internal_node.right = right_child

        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]

def build_huffman_codes(node, code="", huffman_codes={}):
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = code

    build_huffman_codes(node.left, code + "0", huffman_codes)
    build_huffman_codes(node.right, code + "1", huffman_codes)

    return huffman_codes

def huffman_encode(data, huffman_codes):
    encoded_data = ""
    for char in data:
        encoded_data += huffman_codes[char]
    return encoded_data

def huffman_decode(encoded_data, huffman_codes):
    decoded_data = ""
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        if current_code in huffman_codes.values():
            decoded_char = next(key for key, value in huffman_codes.items() if value == current_code)
            decoded_data += decoded_char
            current_code = ""
    return decoded_data

if __name__ == "__main__":
    data = "this is an example for huffman encoding"
    root_node = build_huffman_tree(data)
    huffman_codes = build_huffman_codes(root_node)

    encoded_data = huffman_encode(data, huffman_codes)
    print("Encoded data:", encoded_data)

    decoded_data = huffman_decode(encoded_data, huffman_codes)
    print("Decoded data:", decoded_data)
