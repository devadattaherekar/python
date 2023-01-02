import paramiko

ssh=paramiko.SSHClient() # first create ssh client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # no prompting for fingerprint
ssh.connect(username="root",password="redhat",hostname="192.168.59.132",port=22)
stdin,stdout,stderr=ssh.exec_command("uname -a")
print(stdout.read()) # print output of command
#print(stderr.read()) # print error message
sftp_client=ssh.open_sftp()
#print(dir(sftp_client))
sftp_client.get('/root/data.txt','download.txt')
sftp_client.chdir('/root')
print(sftp_client.getcwd())
sftp_client.get('/root/myzombie.c','zombie.txt') # download
sftp_client.put('use_dates.py','/root/use_dates.py') # upload
sftp_client.close() # first close sftp
ssh.close() # then close ssh