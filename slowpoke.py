import subprocess
import os
import time

def check_and_install(package):
	result = subprocess.run(['apt','-qq','list',package,'--installed'], stdout=subprocess.PIPE)
	if not result.stdout.decode('utf-8'):
		print(package+' not found...')
		time.sleep(0.5)
		print('Installing '+package)
		os.system('sudo apt-get install ' + package)

	else:
		print(package,': OK')


package_list = ['trickle','firefox','nload']

for pac in package_list:
	check_and_install(pac)

print('All requirements are satisfied')
time.sleep(2)	
data = int(input("How much data would you like to use per hour (MB): "))
data = (data * 1024)/(60*60) 
print('\n\nStarting firefox with\nUpload speed:'+str(round(data+0.1*data))+' KBps\nDownload speed: '+str(round(data))+' KBps\n\n')
print('Come back here to see total bandwidth consumption')
time.sleep(3)
subprocess.run(['trickle','-s','-u',str(data+0.1*data),'-d',str(data),'firefox'])
os.system('nload')
