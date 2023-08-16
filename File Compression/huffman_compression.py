import pickle

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def build_frequency_table(data):
    frequency_table = {}
    for char in data:
        frequency_table[char] = frequency_table.get(char, 0) + 1
    return frequency_table

def build_huffman_tree(frequency_table):
    nodes = [HuffmanNode(char, freq) for char, freq in frequency_table.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = HuffmanNode(None, left.frequency + right.frequency)
        parent.left = left
        parent.right = right
        nodes.append(parent)
    return nodes[0]

def build_encoding_table(root, current_code="", encoding_table=None):
    if encoding_table is None:
        encoding_table = {}
    if root.char:
        encoding_table[root.char] = current_code
    if root.left:
        build_encoding_table(root.left, current_code + "0", encoding_table)
    if root.right:
        build_encoding_table(root.right, current_code + "1", encoding_table)
    return encoding_table

def encode(data, encoding_table):
    encoded_data = ""
    for char in data:
        encoded_data += encoding_table[char]
    return encoded_data

def decode(encoded_data, huffman_tree):
    decoded_data = ""
    current_node = huffman_tree
    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char:
            decoded_data += current_node.char
            current_node = huffman_tree
    return decoded_data

def compress_file(input_filename, output_filename):
    with open(input_filename, "r") as file:
        data = file.read()
    
    frequency_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)
    encoded_data = encode(data, encoding_table)

    with open(output_filename, "wb") as output_file:
        import pickle
        pickle.dump((frequency_table, encoded_data), output_file)

def decompress_file(input_filename, output_filename):
    with open(input_filename, "rb") as file:
        frequency_table, encoded_data = pickle.load(file)

    huffman_tree = build_huffman_tree(frequency_table)
    decoded_data = decode(encoded_data, huffman_tree)

    with open(output_filename, "w") as output_file:
        output_file.write(decoded_data)

if __name__ == "__main__":
    input_filename = "input.txt"
    compressed_filename = "compressed.bin"
    decompressed_filename = "decompressed.txt"

    compress_file(input_filename, compressed_filename)
    decompress_file(compressed_filename, decompressed_filename)

import pickle

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def build_frequency_table(data):
    frequency_table = {}
    for char in data:
        frequency_table[char] = frequency_table.get(char, 0) + 1
    return frequency_table

def build_huffman_tree(frequency_table):
    nodes = [HuffmanNode(char, freq) for char, freq in frequency_table.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = HuffmanNode(None, left.frequency + right.frequency)
        parent.left = left
        parent.right = right
        nodes.append(parent)
    return nodes[0]

def build_encoding_table(root, current_code="", encoding_table=None):
    if encoding_table is None:
        encoding_table = {}
    if root.char:
        encoding_table[root.char] = current_code
    if root.left:
        build_encoding_table(root.left, current_code + "0", encoding_table)
    if root.right:
        build_encoding_table(root.right, current_code + "1", encoding_table)
    return encoding_table

def encode(data, encoding_table):
    encoded_data = ""
    for char in data:
        encoded_data += encoding_table[char]
    return encoded_data

def decode(encoded_data, huffman_tree):
    decoded_data = ""
    current_node = huffman_tree
    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char:
            decoded_data += current_node.char
            current_node = huffman_tree
    return decoded_data

def compress_file(input_filename, output_filename):
    with open(input_filename, "r") as file:
        data = file.read()
    
    frequency_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)
    encoded_data = encode(data, encoding_table)

    with open(output_filename, "wb") as output_file:
        import pickle
        pickle.dump((frequency_table, encoded_data), output_file)

def decompress_file(input_filename, output_filename):
    with open(input_filename, "rb") as file:
        frequency_table, encoded_data = pickle.load(file)

    huffman_tree = build_huffman_tree(frequency_table)
    decoded_data = decode(encoded_data, huffman_tree)

    with open(output_filename, "w") as output_file:
        output_file.write(decoded_data)

if __name__ == "__main__":
    input_filename = "input.txt"
    compressed_filename = "compressed.bin"
    decompressed_filename = "decompressed.txt"

    compress_file(input_filename, compressed_filename)
    decompress_file(compressed_filename, decompressed_filename)