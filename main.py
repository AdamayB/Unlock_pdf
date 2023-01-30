import pikepdf
path="C:\\Users\\adama\\Documents\\Thapar_Study_material\\Signals and Systems\\"
def removePass(a,b):
    removePass = pikepdf.open(a, password="2021!")
    removePass.save(b)
    print('Unlocked')
l=['09.2',10.1,10.2]
for i in l:
    path1=path+'S&S_UEC_LECT'+str(i)+'.pdf'
    path2=path+'S&S_UEC_LECT'+str(i)+'(unlocked).pdf'
    removePass(path1,path2)

'''removePass=pikepdf.open(path1,password="2021!")
removePass.save(path+'S&S_UEC_LECT01(unlocked).pdf')
print('Unlocked')'''
