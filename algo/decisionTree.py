import numpy as np

def entropy(data, feature_index):
    cnt = 0
    n = data.shape[0]
    for i in data:
        if i[feature_index] == 1:
            cnt+=1
    per = cnt / n
    if per == 0 or per == 1:
        return 0
    return - per * np.log2(per) - (1-per) * np.log2(1-per)


class DecisionTree(object):
    def __init__(self, data, label, feature, left, right) -> None:
        self.data = data
        self.left = left
        self.right = right
        self.label = label
        self.feature = feature


def split_data(data, label, feature):
    left = []
    left_label = []
    right = []
    right_label = []
    for i in range(data.shape[0]):
        if data[i][feature] == 1:
            left.append(data[i])
            left_label.append(label[i])
        else:
            right.append(data[i])
            right_label.append(label[i])
    left = np.array(left)
    right = np.array(right)
    left_label = np.array(left_label)
    right_label = np.array(right_label)
    return left, left_label, right, right_label


def stop_split(X, y):
    if X[y == 0].shape[0] == X.shape[0] or X[y == 1].shape[0] == X.shape[0]:
        return True
    return False


def construct_decision_tree(root):
    if root.data.shape[0] == 0 or stop_split(root.data, root.label):
        return 
    else:
        en = []
        for i in range(0, root.data.shape[1]):
            en.append(entropy(root.data, i))
        feat = np.argmax(en)
        root.feature = feat
        left_data, left_label, right_data, right_label = split_data(root.data, root.label, feat)
        root.left = DecisionTree(left_data, left_label, None, None, None)
        root.right = DecisionTree(right_data, right_label, None, None, None)
        construct_decision_tree(root.left)
        construct_decision_tree(root.right)


def printTree(root):
    if root == None:
        return
    else:
        
        printTree(root.left)
        printTree(root.right)
        if root.left == None and root.right == None:
            for i in root.data:
                print(i)
            print()

def predictLabel(x, root):
    if stop_split(root.data, root.label):
        return root.label[0]

    if x[root.feature] == 1:
        return predictLabel(x, root.left)

    return predictLabel(x, root.right)   

if __name__ == "__main__":
    X = np.array([
        [1,0,0,1,0,0,1,0],
        [1,0,0,1,0,0,1,1],
        [0,1,0,1,0,0,1,0],
        [0,0,1,0,0,1,1,0],
        [0,0,1,0,1,0,0,0],
        [0,0,1,0,1,0,0,1],
        [0,1,0,0,1,0,0,1],
        [1,0,0,0,0,1,1,0],
        [1,0,0,0,0,1,0,0],
        [0,0,1,0,0,1,0,0],
        [1,0,0,0,0,1,0,1],
        [0,1,0,0,0,1,1,1],
        [0,1,0,1,0,0,0,0],
        [0,0,1,0,0,1,1,1]])

    y = np.array([
        0,0,1,1,1,0,1,0,1,1,1,1,1,0
    ])

    root = DecisionTree(X, y, None, None, None)
    construct_decision_tree(root)
    # printTree(root)
    x = np.array([0,1,0,1,0,0,0,0])

    lab = predictLabel(x, root)
    print(lab)