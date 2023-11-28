import numpy as np

def load_cst_file(data_file, runIds, coordinate_count):
    """Returns a data file of the dimension [runids, measurepoints, coordinate count].
    

    Args:
        data_file (string) file path of the cst txt file\n
        runIds (int) amount of run ids in the data file\n
        coordinate_count (int) the amount of axis\n
    """
    
    file_to_load = open(data_file, "r")


    line_count = 0
    file_to_load.readline()
    file_to_load.readline()
    file_to_load.readline()

    flag_hashtag = False
    while(flag_hashtag == False):
        
        x = file_to_load.readline()
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

def load_cst_filePOLAR(data_file, runIds, coordinate_count):
    """Returns a data file of the dimension for polar plots. [runids, measurepoints, coordinate count].
    

    Args:
        data_file (string) file path of the cst txt file\n>
        runIds (int) amount of run ids in the data file\n
        coordinate_count (int) the amount of axis\n
    """
    
    file_to_load = open(data_file, "r")


    line_count = 0
    file_to_load.readline()
    file_to_load.readline()
    file_to_load.readline()
    file_to_load.readline()

    flag_hashtag = False
    while(flag_hashtag == False):
        
        x = file_to_load.readline()
        if len(x) == 0:
            break
        elif x[0] == "#":
            break
        else:
            line_count += 1

    line_count -= 1
    file_to_load = open(data_file, "r")

    data = np.zeros((runIds, line_count, coordinate_count))

    for i in range(runIds):
        #print(i)
        file_to_load.readline()
        file_to_load.readline()
        file_to_load.readline()
        file_to_load.readline()
        for k in range(line_count):
            x = file_to_load.readline()
            im = x.split()
            data[i][k] = [float(x) for x in im]
        file_to_load.readline()


    return data

def load_cst_filePOLARwhenASCIIExport(data_file, runIds, coordinate_count):
    with open(data_file, 'r') as f:
        lines = f.readlines()
    data = []
    current_runid = []
    last_value = 0

    for line in lines:
        if line.startswith('#'):
            if current_runid:
                data.append(np.array(current_runid))
            current_runid = []
            last_value = 0
            
        else:
            values = [float(x) for x in line.split()]
            if values[0] < last_value:  # if the value is decreasing            
                values[0] = values[0] + abs(last_value - 180)  
            last_value = values[0]
            current_runid.append(values)
    if current_runid:
        data.append(np.array(current_runid))
    return data

if __name__ == "__main__":
    print("lets go")
    #print(load_cst_filePOLARwhenASCIIExport("Data/ff75[1].txt", 3, 8).shape)