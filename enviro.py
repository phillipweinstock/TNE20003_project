from cryptography.fernet import Fernet
# Enviromental variables go here
host = "rule28.i4t.swin.edu.au"
usr_psd = ["102101219","102101219"]
# Topics 
public_data = 'public/{}/power_plant/data'
private_data = '102101219/{}/power_plant/data'
private_settings = '102101219/{}/power_plant/settings'
#Yay encryption...
symmetric_key = b'lBYUkXD2pSZjo2uTjL2Tmnru2yUSfkUnK2jIVgmRmXQ='# <-- DO NOT DO THIS Fernet.generate_key()
black_box = Fernet(symmetric_key)