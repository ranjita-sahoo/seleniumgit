f = open('Pancard.jpg','rb')
f1 = open('Pan.jpg','wb')
for i in f:
    f1.write(i)