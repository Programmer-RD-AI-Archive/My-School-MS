from Models.Will_Answer_Solve_Issue import *
from Models.Will_Answer_Solve_Issue.help_funcs import *


def load_data():
    data = pd.read_csv("./data/data.csv").dropna()[:1250]
    print(data.columns)
    X = data["blurb"]
    y = data["state"]
    words = []
    labels = {}
    labels_r = {}
    idx = 0
    data = []
    for label in tqdm(list(y.tolist())):
        if label not in list(labels.keys()):
            idx += 1
            labels[label] = idx
            labels_r[idx] = label
    for X_batch, y_batch in zip(tqdm(X), y):
        X_batch = tokenize(X_batch)
        new_X = []
        for Xb in X_batch:
            new_X.append(stem(Xb))
        words.extend(new_X)
        data.append(
            [new_X,
             np.eye(labels[y_batch], len(labels))[labels[y_batch] - 1]])
    words = sorted(set(words))
    np.random.shuffle(data)

    X = []
    y = []
    for d in tqdm(data):
        X.append(bag_of_words(d[0], words))
        y.append(d[1])

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.125,
                                                        shuffle=False)
    X_train = torch.from_numpy(np.array(X_train)).to(device).float()
    y_train = torch.from_numpy(np.array(y_train)).to(device).float()
    X_test = torch.from_numpy(np.array(X_test)).to(device).float()
    y_test = torch.from_numpy(np.array(y_test)).to(device).float()
    return X_train, X_test, y_train, y_test
