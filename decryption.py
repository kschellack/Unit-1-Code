#this program will demonstrate letter replacement decryption

# this is the dictionary that defines the decryption
# key =    'mwgp bdzxrylacsokjfhtnueivq'
# values = 'abcdefghijklmnopqrstuvwxyz '

# variable decoder is the dictionary
decoder = {'m': 'a', 'w': 'b', 'g': 'c', 'p': 'd', ' ': 'e', 'b': 'f', 'd': 'g',
           'z': 'h', 'x': 'i', 'r': 'j', 'y': 'k', 'l': 'l', 'a': 'm', 'c': 'n',
           's': 'o', 'o': 'p', 'k': 'q', 'j': 'r', 'f': 's', 'h': 't', 't': 'u',
           'n': 'v', 'u': 'w', 'e': 'x', 'i': 'y', 'v': 'z', 'q': ' '}

# text to be decoded is ciphertext = 'hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh'
# which has manually been decrypted as  "the sun was shining on the sea shining with all his might"

output=''   #the initial string is ''. Decoded letters from for loop will be concatenated to output

# the text to decrypt is ciphertext
ciphertext = 'hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh'

for i in range(len(ciphertext)):             # for loop provides index of string ciphertext, it is used as key
   output=output + decoder[ciphertext[i]]    # to determine value from dictionary (decoder)

print(output)                                # string (output) is printed


