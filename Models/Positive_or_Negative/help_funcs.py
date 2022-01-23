from Models.Positive_or_Negative import *


def tokenize(sentence):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_words, all_words):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    tokenized_words = [stem(w) for w in tokenized_words]
    bag = np.zeros(len(all_words))
    for idx, w in enumerate(all_words):
        if w in tokenized_words:
            bag[idx] = 1.0
    return bag


def load_data():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    data = pd.read_csv("./data.csv").dropna()[:10000]
    data = data.sample(frac=1)
    X = data["im getting on borderlands and i will murder you all ,"]
    y = data["Borderlands"]
    words = []
    data = []
    labels = {}
    labels_r = {}
    idx = 0
    for label in y:
        if label not in list(labels.keys()):
            idx += 1
            labels[label] = idx
            labels_r[idx] = label
    for Xb, yb in tqdm(zip(X, y)):
        Xb = tokenize(Xb)
        new_X = []
        for X_batch in Xb:
            new_X.append(stem(X_batch))
        words.extend(new_X)
        data.append([new_X, np.eye(labels[yb] + 1, len(labels))[labels[yb]]])
    words = sorted(set(words))
    np.random.shuffle(data)
    X = []
    y = []
    for sentence, tag in tqdm(data):
        X.append(bag_of_words(sentence, words))
        y.append(tag)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.125, shuffle=False)
    X_train = torch.from_numpy(np.array(X_train)).to(device).float()
    y_train = torch.from_numpy(np.array(y_train)).to(device).float()
    X_test = torch.from_numpy(np.array(X_test)).to(device).float()
    y_test = torch.from_numpy(np.array(y_test)).to(device).float()
    return X_train, y_train, X_test, y_test, words, labels_r, labels


def train(epochs, X_train, y_train, X_test, y_test, model, optimizer, criterion, batch_size):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    wandb.init(project=PROJECT_NAME, name="baseline")
    for _ in tqdm(range(epochs)):
        for i in range(0, len(X_train), batch_size):
            X_batch = X_train[i : i + batch_size]
            y_batch = y_train[i : i + batch_size]
            preds = model(X_batch)
            loss = criterion(preds, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        model.eval()
        torch.cuda.empty_cache()
        wandb.log(
            {
                "Loss": (
                    get_loss(model, X_train, y_train, criterion)
                    + get_loss(model, X_batch, y_batch, criterion) / 2
                )
            }
        )
        torch.cuda.empty_cache()
        wandb.log({"Val Loss": get_loss(model, X_test, y_test, criterion)})
        torch.cuda.empty_cache()
        wandb.log(
            {
                "Acc": (
                    get_accuracy(model, X_train, y_train) + get_accuracy(model, X_batch, y_batch)
                )
                / 2
            }
        )
        torch.cuda.empty_cache()
        wandb.log({"Val Acc": get_accuracy(model, X_test, y_test)})
        torch.cuda.empty_cache()
        model.train()
    wandb.finish()
    torch.cuda.empty_cache()
