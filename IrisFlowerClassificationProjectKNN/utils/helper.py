
#knn on iris flower data set

from math import sqrt
from csv import reader
 
#calculate the euclidean distance between two vectors

def euclidean_distance(row1,row2):
    distance=0.0
    for i in range(len(row1)-1):
        distance+=(row1[i]-row2[i])**2
    return sqrt(distance)


#load data from csv file

def load_csv(filename):
    dataset=list()
    with open(filename,'r') as file:
        csv_reader=reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

#convert string to float
def str_data_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

#convert string to int
def str_data_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
		print('[%s] => %d' % (value, i))
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup
#find min and max for each column
def dataset_min_max(dataset):
    min_max=list()
    for i in range(len(dataset[0])):
        col_values=[row[i] for row in dataset]
        min_value=min(col_values)
        max_value=max(col_values)
        min_max.append([min_value,max_value])
    return min_max

#normalize the dataset to range 0-1
def normalize_dataset(dataset,min_max):
    for row in dataset:
        for i in range(len(row)):
            row[i]=(row[i]-min_max[i][0])/(min_max[i][1]-min_max[i][0])

 

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors


# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction
