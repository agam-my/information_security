#source to learn from https://koding.alza.web.id/
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = int(input('Please input cipher key using number: '))

def encode(word,key):
  word = word.lower()
  enc = ''
  for char in word:
    if char in alphabet:
      old = alphabet.index(char)
      new = (old + key) % len(alphabet)
      alphabet_new = alphabet[new]
      enc = enc + alphabet_new 
    else:
       enc = enc + ' ' 
  return enc

word = input('Please input the word that would like to encrypt :')
# ENCRYPTION
word_res = encode(word,key)
print('Word entered is:',word)
print('Word encryption result using Caesar Cipher with key:',key, 'is', word_res)
# DECRYPTION (re-encryption using minus key)
word_begin = encode(word_res,-key)
print('If the result is re-encrypted using the negative value of the previous cipher key, the result word is:',-key, 'is', word_begin)
