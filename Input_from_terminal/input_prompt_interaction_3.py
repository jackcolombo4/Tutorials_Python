##############################################################
# Interact with command line 3
##############################################################
addIp = '?'
while addIp:
    addIp = input('Would you like to add ip ? (None = no): ')
    print('\033[1A' + addIp + ' '*40)

