f1 = open('/home/hp/Documents/College/Coding/ACT - Technical/download.jpeg', 'rb')
f2 = open('download_duplicate.jpeg', 'wb')
data = f1.read()
f2.write(data)