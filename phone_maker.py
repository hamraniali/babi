import random
print('in process...')
begines = ['0913', '0938', '0917',
           '0916', '0914' , '0933' ,
           '0910' , '0935' , '0912' ,
           '0920' , '0930' , '0936' ,
           '0990' , '0921' , '0922',
           '0919' , '0998' , '0939']

phones = ""
for i in range(183):
    phones += begines[random.randint(0 , 17)] + str(random.randint(1000000 , 9999999)) + '\n'

f = open('phones.txt', 'w')
f.write(phones)
f.close()
print('All Done!')
