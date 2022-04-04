# Nicholas Lormand
# njl160030
# imports
import csv
import sys
import math


class Node(object):
    """
    node class for each attribute in the perceptron
    """

    def __init__(self):
        """
        """
        self.name = ''
        self.weight = 0
        self.value = 0

    def update_weight(self, learning_rate, delta_k, sigmoid_prime):
        """
        :param instance: training instance value
        :type: new value for this node
        """
        self.weight = self.weight - learning_rate * delta_k * sigmoid_prime * node.value


    def calculate_sigmoid

class Perceptron(object):
    """
    perceptron class for classifying binary data
    """

    def __init__(self):
        """
        """
        self.node_list = []
        self.learning_rate = 0
        self.num_iterations = 0
        self.output = 0

    def get_output(self, instance_list, class_value):
        """
        :return: output of the node
        """
        count = 0
        while count < len(self.node_list):
            self.node_list[count].value = instance_list[count]
            count += 1
        for node in self.node_list:
            # node.value = instance_list[self.node_list.index(node)]
            dot_product = self.calculate_dot_product()
            sigmoid = self.calculate_sigmoid(node.weight * node.value)
            sigmoid_prime = sigmoid * (1 - sigmoid)
            delta_k = class_value - sigmoid_prime
            node.update_weight(self.learning_rate, delta_k, sigmoid_prime)
        output = self.calculate_dot_product()
        return output

    def calculate_dot_product(self):
        sum = 0
        for node in self.node_list:
            sum += (node.weight * node.value)

        return sum

    def calculate_sigmoid(self, product):
        sigmoid = 1 / (1 + math.pow(math.e, -1 * product))
        return sigmoid


"""def calculate_weight(weight):
#take dot product of perceptron values for iteration i and current set of weights
# weight_i = weight_i + (leaning rate)(delta_k) (x_i ^ k) (derivative of sigmoid of the dot product)
    for x in weight_list:
        dot_product = calculate_dot_product(weight_list, x_values_for_i_iteration)
        sigmoid_value = calculate_sigmoid(dot_product)
        weight_new = weight + p.learning_rate * calculate_delta_value(class_value, signmoid_value) * x_values_for_i_iteration[x] * calculate_sigmoid_prime(sigmoid_value)
    return weight_new


    """

# get args from command prompt
training_file = None
p = Perceptron()
if len(sys.argv) == 5:
    training_file = sys.argv[1]
    testing_file = sys.argv[2]
    p.learning_rate = float(sys.argv[3])
    p.num_iterations = int(sys.argv[4])

    print(training_file)
    print(testing_file)
    # turns training data into 2-D list
    with open(training_file) as f:
        reader = csv.reader(f, delimiter="\t")

        training_list = []
        first = True
        for line in reader:
            temp_list = []
            if first:
                for item in line:
                    temp_list.append(item)
                first = False
            else:
                for item in line:
                    temp_list.append(float(item))
            training_list.append(temp_list)

    for attribute in training_list[0]:
        if attribute is not 'class':
            node = Node()
            node.name = attribute
            p.node_list.append(node)

    instance_list = []
    first = True
    for instance in training_list:
        if not first:
            instance_list.append(instance)
        first = False

    output = ''
    # print('# of instances: ' + str(len(instance_list)))
    for iteration in range(p.num_iterations):
        # output
        if iteration == 0:
            instance = 1
        else:
            instance = (iteration % len(instance_list)) + 1

        print("After iteration %s: " % str(iteration + 1), end='')
        output = p.get_output(instance_list[instance - 1],
                              instance_list[instance - 1][len(instance_list[instance - 1]) - 1])

        # print the weights and output
        for node in p.node_list:
            print("w(%s)=%s, " % (str(node.name), round(node.weight, 3)), end='')
        print("output=%s" % str(round(output, 3)))






else:
    string1 = 'Incorrect Input: : (1) a training file '
    string2 = '(2) a testing file, '
    string3 = '(3) the learning rate, '
    string4 = 'and (4) the number of iterations to run the algorithm.'
    print('%s%s%s%s' % (string1, string2, string3, string4))

# Loop until all examples are correctly predicted or stopping criteria is reached
# Initialize weights to 0's

