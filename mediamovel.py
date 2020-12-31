def media_movel(data_frame, value, column, new_name_column):
    for i in range(0, data_frame.shape[0] - (value - 1)):
        fn = 0
        for y in range(0, value):
            fn += data_frame.iloc[i + y, column]
        data_frame.loc[data_frame.index[i+ (value - 1)],
                       new_name_column] = np.round(fn/value, 1)
    return data_frame
