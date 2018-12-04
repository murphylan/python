# 导入socket
import socket                                         

# 创建一个socket对象
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# 得到主机名
host = socket.gethostname()                           
host = '127.0.0.1' # 仅用于测试本地
port = 9999                                           

# 绑定主机和端口
serversocket.bind((host, port))                                  

# 最多排队5个请求
serversocket.listen(5)                                           

while True:
   # 建立连接
   clientsocket,addr = serversocket.accept()      

   print("从这里开始建立连接 %s" % str(addr))
    
   msg = 'Thank you for connecting'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()




