#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    import numpy as np
    from sklearn.metrics import r2_score

    # print 'type of predictions:', type(predictions)

    #err_list = [abs(net_worths[i] - predictions[i]) for i in range(len(net_worths))]
    err_list = abs(predictions - net_worths)
    # print 'err_list:',err_list
    # print type(err_list)

    new_data = zip(ages.tolist(),net_worths.tolist(),err_list.tolist())
    datalist = new_data

    sorted_list = sorted(datalist, key=lambda tuple:(tuple[2]))

    # print 'new data:', datalist
    # print 'sorted list', sorted_list

    new_len = int(len(sorted_list)*0.9)

    cleaned_data = sorted_list[:new_len]
    # print cleaned_data
    # print 'length of cleaned_data:', len(cleaned_data)

    return cleaned_data
