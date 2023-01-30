import pikepdf
path="" #enter path
def removePass(a,b,password):
    removePass = pikepdf.open(a, password)
    removePass.save(b)
    print('Unlocked')
# a= the original file name
# b= the unlocked file name
#password =password of the original file
