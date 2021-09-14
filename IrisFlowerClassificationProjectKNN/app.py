
from utils import *
def main():
    try:
        print('test')
            # Make a prediction with KNN on Iris Dataset
        filename = 'data/iris.csv'
        dataset = load_csv(filename)
        for i in range(len(dataset[0])-1):
            str_data_to_float(dataset, i)
        # convert class column to integers
        str_data_to_int(dataset, len(dataset[0])-1)
        # define model parameter
        num_neighbors = 5
        # define a new record
        row = [5.7,2.9,4.2,1.3]
        # predict the label
        label = predict_classification(dataset, row, num_neighbors)
        print('Data=%s, Predicted: %s' % (row, label))
    except Exception as e:
        print(f'Exception:{e}')

if __name__=='__main__':main()