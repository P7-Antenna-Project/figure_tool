from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
import numpy as np

# Some example data to display

collection = FigureCollection("Introduction1")


@collection.table(header=["Col 1", "Col 2", "Col 3"], header_spec="l|l|l")
def test_table():
    header = ["Col 1", "Col 2", "Col 3"]
    data = []

    for _ in range(10):
        data_row = {col: np.random.randint(0, 99) for col in header}
        data.append(data_row)

    return data

@collection.plot_figure()
def SAR_test_dipole_S_param():
    fig, ax = plt.subplots(1, 1)
    runids = 4

    file_to_load = open("Data/SAR_test_S_parameters.txt", "r")


    line_count = 0
    file_to_load.readline()
    file_to_load.readline()
    file_to_load.readline()

    flag_hashtag = False
    while(flag_hashtag == False):
        x = file_to_load.readline()
        #print(x)
        if x[0] == "#":
            break
        else:
            line_count += 1
    
    #print(line_count)
    file_to_load = open("Data/SAR_test_S_parameters.txt", "r")

    data = np.zeros((runids, line_count, 2))

    for i in range(runids):
        file_to_load.readline()
        file_to_load.readline()
        file_to_load.readline()
        for k in range(line_count):
            x = file_to_load.readline()
            im = x.split(f"\t")
            data[i][k][0] = float(im[0])
            data[i][k][1] = float(im[1])
    
    distance = ["0 mm", "3 mm","10 mm","Ref"]
    for i in range(runids):
        ax.plot(np.transpose(data[i])[0], np.transpose(data[i])[1], label=f"{distance[i]}")

    ax.grid()
    plt.xlabel("Frequency [GHz]")
    plt.ylabel("S$_{1,1}$-Parameter [dB]")
    fig.legend()
    return fig


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    runids = 4

    file_to_load = open("Data/SAR_test_S_parameters.txt", "r")


    line_count = 0
    print(file_to_load.readline())
    print(file_to_load.readline())
    print(file_to_load.readline())

    flag_hashtag = False
    while(flag_hashtag == False):
        x = file_to_load.readline()
        print(x)
        if x[0] == "#":
            break
        else:
            line_count += 1
    
    print(line_count)
    file_to_load = open("Data/SAR_test_S_parameters.txt", "r")

    data = np.zeros((runids, line_count, 2))

    for i in range(runids):
        print(file_to_load.readline())
        print(file_to_load.readline())
        print(file_to_load.readline())
        for k in range(line_count):
            x = file_to_load.readline()
            im = x.split(f"\t")
            data[i][k][0] = float(im[0])
            data[i][k][1] = float(im[1])
    np.save("Sar_test.npy", data)
    # print(data[0])
    # plt.plot(np.transpose(data[1])[0], np.transpose(data[1])[1])
    # plt.show()
