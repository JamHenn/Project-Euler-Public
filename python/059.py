"""
This took some experimentation.
There are 26^3 = 17576 possible results, so several filters are applied:

(1) Each character decrypted is checked for weird ASCII characters (<32).
    All decrypted characters pass this test.

(2) The letter count of the decrypted message.
    If the minimum proportion of letters is set to 70%:
    17404 out of 17576 results are excluded.
    Note: 75% excluded everything.

(3) The message should contain at least one of these strings:
    "The ", "the " or "and ".
    This leaves just 1 result, which is clearly the right answer.
    The password is "exp".
"""

def generate_possible_passwords():
    """Password consists of 3 lowercase letters"""
    lc_alphabet = [chr(ascii) for ascii in range(ord('a'), ord('z')+1)]
    possible_passwords = []
    for c1 in lc_alphabet:
        for c2 in lc_alphabet:
            for c3 in lc_alphabet:
                possible_passwords.append(c1+c2+c3)

    return possible_passwords


def convert_char_to_ascii(char):
    return ord(char)


def convert_ascii_to_char(ascii_value):
    return chr(ascii_value)


def xor(int1, int2):
    return int1 ^ int2


def has_common_words(string):
    common_words = ["The ", "the ", "and "]
    for word in common_words:
        if word in string:
            return True
    return False


def is_text(ascii):
    """Filter most of the non-text ASCII characters (10=\n)"""
    return (ascii > 31 or ascii == 10)


def is_letter(ascii):
    return (64 < ascii and ascii < 91) or (96 < ascii and ascii < 123)


def xor_decrypt(encrypted_text, encryption_key):
    key_ascii = [convert_char_to_ascii(character) for character in encryption_key]
    key_length = len(encryption_key)
    key_index = 0

    letter_count = 0
    original_text = ""
    for character in encrypted_text:
        character_ascii = convert_char_to_ascii(character)
        decrypted_ascii = xor(character_ascii, key_ascii[key_index])
        if not(is_text(decrypted_ascii)): return

        letter_count += is_letter(decrypted_ascii)
        original_text += convert_ascii_to_char(decrypted_ascii)

        key_index += 1
        key_index %= key_length

    letter_proportion = letter_count/len(original_text)
    if letter_proportion < 0.7: return
    if has_common_words(original_text): return original_text


encryption = ""
with open("data/p059_cipher.txt", 'r') as f:
    decimals = f.read().split(',')
    characters = [convert_ascii_to_char(int(decimal)) for decimal in decimals]
    encryption = "".join(characters)


skipped = 0
possible_passwords = generate_possible_passwords()
for password in possible_passwords:
    decryption = xor_decrypt(encryption, password)
    if decryption is not None:
        print(f"Password: {password}")
        print(f"{decryption}\n")
    else:
        skipped += 1

print(f"Excluded {skipped} out of {len(possible_passwords)} results due to low letter count or lack of common words.")

original_text = xor_decrypt(encryption, "exp")
sum_ascii = sum([ord(character) for character in original_text])
print("Result: Password = exp")
print(f"Sum of ASCII values in original text: {sum_ascii}")
