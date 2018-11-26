path = '/home/one/data/alaska-tiff/jpg/'

input_name = 'name5.txt'
output_name = 'list_img_profiles5.txt'

with open(path + input_name) as f:
    lines = f.readlines()
    for line in lines:
        if line != '\n':
            msg = line.split('|')
            file_name = msg[0]
            file_size = msg[1].replace("\n", "")
            #print(msg[0], msg[1].replace("\n", ""))
            s_line = ''
            with open(path + output_name, 'r') as f:
                s = f.readlines()

                for ss in s:
                    if ss != '\n':
                        data = ss.split('|')
                        key = data[0].strip()
                        value = data[-2].replace(' ', '')

                        if file_name == key:
                            ss = ss.replace(data[-2], file_size)

                        s_line += ss

            with open(path + output_name, 'w+') as f:
                f.write(s_line)