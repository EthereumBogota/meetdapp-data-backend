import ipfs

DATA = "/home/oscar/Desktop/picasso_nuevo.jpg"

ipfs_obj = ipfs.LightHouse()

send_data = ipfs_obj.send_data_lh(path=DATA)
