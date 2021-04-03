# -*- coding: utf-8 -*-


import os

path = "*.*"
pathnew = "*.*"
#
os.chdir(path)


#path, directory, files
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        #txt file
        if os.path.splitext(name)[1] == '.txt':  
            #print(root)
            print(os.path.join(root, name))
            
            L = []          # null
            #open file
            f1 = open(os.path.join(root, name),'r')
            f1_data = f1.readlines()
            for k in range(len(f1_data)):
                #processing
                fline = f1_data[k].replace('docid = ','');
                #
                fline = fline.replace('inc = ','');
                #
                fline = fline.replace('prob = ','');
                #
                fs = fline.split()
                L.append([fs[0],fs[1],fs[2],fs[5],fs[6],fs[7]])
            
            #write the file
            filenamenew=os.path.join(pathnew,os.path.join(root, os.path.splitext(name)[0]+'_new'+os.path.splitext(name)[1]).replace('.\\',''))
            if not os.path.exists(os.path.dirname(filenamenew)):
                try:
                    os.makedirs(os.path.dirname(filenamenew))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            
            fw = open(filenamenew,'w')
            
            
            for j in range(len(L)):
                fw.write(L[j][0]+' '+L[j][1]+' '+L[j][2]+' ' + str(L[j][3])+' '+ L[j][4] +' '+ L[j][5]+'\n')
            fw.close()
            f1.close()

