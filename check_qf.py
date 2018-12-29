import os
import random
import time

base1='/home/zzl/alaska/material_qf/98/stego/train1_stego'
base2='/home/zzl/alaska/material_qf/98/stego/train2_stego'
base3='/home/zzl/alaska/material_qf/98/stego/train3_stego'
base4='/home/zzl/alaska/material_qf/98/stego/train4_stego'
base5='/home/zzl/alaska/material_qf/98/stego/train5_stego'

path = [base1,base2,base3,base4,base5]

result = []

def all_path(dirname):

    for i in path:
	for maindir, subdir, file_name_list in os.walk(i):
            for filename in file_name_list[0:100]: # choice 98 items in each dir 
		apath = os.path.join(maindir, filename)
		result.append(apath)
    return result

def write_result():
    for path in result:
        cmd='find '+path+' -print | xargs -i identify -format "%Q," {} >> /home/zzl/alaska/material_qf/98/stego/train_temp_qf.txt'
	os.system(cmd)

if __name__=='__main__':
	all_path(path)
	write_result()

