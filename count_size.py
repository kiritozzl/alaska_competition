path = '/home/one/data/alaska-tiff/jpg/'

input_name = 'tif_name1.txt'
output_name = 'count_tif1_size.txt'

with open(path + input_name) as f:
    lines = f.readlines()
    size = {}
    for line in lines:
        if line != '\n':
            msg = line.split('|')
            #file_name = msg[0]
            file_size = msg[1].replace("\n", "")
            if size == {}:
                size[file_size] = 1
            else:
                have_key = 0
                for key, value in size.iteritems():
                    if key == file_size:
                        size[key] += 1
                        have_key = 1

                if have_key == 0:
                    size[file_size] = 1
    #print(size)
    with open(path + output_name, 'a+') as f:
        for key, value in size.iteritems():
            f.write(key+': '+str(value)+'\n')