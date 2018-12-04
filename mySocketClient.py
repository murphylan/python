# 导入socket
import socket                                         

# 创建一个socket对象
clientsocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# 得到主机名
host = socket.gethostname()                           
host = '127.0.0.1' # 仅用于测试本地
port = 9999                                           

# 连接服务器端.
clientsocket.connect((host, port))                               

# 接收不超过1024个字节
msg = clientsocket.recv(1024)                                     

clientsocket.close()
print (msg.decode('ascii'))


