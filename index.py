import rinobot_plugin as bot
import numpy as np

def rebin(data, binsize, algo='average', xtime=None):
    col_num = data.shape[1]
    new_data = np.zeros((data.shape[0]// binsize, col_num))

    for index, data_row in enumerate(data.T):
        new_row = np.array([])

        for i in range(0, len(data_row) // binsize):
            sublist = data_row[i*binsize:(i*binsize)+binsize]
            if xtime and index == 0:
                new_row = np.append(new_row, sublist.mean())
            else:
                if not algo or algo == 'average':
                    new_row = np.append(new_row, sublist.mean())
                if algo == 'sum':
                    new_row = np.append(new_row, sublist.sum())
                if algo == 'max':
                    new_row = np.append(new_row, sublist.max())

        new_data[:, index] = new_row
    return new_data


def main():
    # lets get our parameters and data
    filepath = bot.filepath()
    data = bot.loadfile(filepath)

    # now comes the custom plugin logic
    binsize = bot.get_arg('binsize', type=int, required=True)
    algo = bot.get_arg('algo', type=str)
    xtime = bot.get_arg('xtime', type=bool)
    if not algo:
        algo='average'

    new_data = rebin(data, binsize, algo=algo, xtime=xtime)

    outname = bot.no_extension() + '-rebin[%s-%d].txt' % (algo, binsize)
    outpath = bot.output_filepath(outname)
    np.savetxt(outpath, new_data)

if __name__ == "__main__":
    main()
