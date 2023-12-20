import os

#run thumbor server
print("Thumbor started on http://localhost:8888")

os.system("thumbor -c ./thumbor.conf")
