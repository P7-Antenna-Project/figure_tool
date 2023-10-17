import numpy as np

def load_cst_file(data_file, runIds, coordinate_count):
    file_to_load = open(data_file, "r")


    line_count = 0
    file_to_load.readline()
    file_to_load.readline()
    file_to_load.readline()

    flag_hashtag = False
    while(flag_hashtag == False):
        
        x = file_to_load.readline()
        print(x)
        if len(x) == 0:
            break
        elif x[0] == "#":
            break
        else:
            line_count += 1

    file_to_load = open(data_file, "r")

    data = np.zeros((runIds, line_count, coordinate_count))

    for i in range(runIds):
        file_to_load.readline()
        file_to_load.readline()
        file_to_load.readline()
        for k in range(line_count):
            x = file_to_load.readline()
            im = x.split(f"\t")
            data[i][k] = [float(x) for x in im]

    
    return data

if __name__ == "__main__":
    print(load_cst_file("data/2_9ghztest.txt", 1, 3).shape)