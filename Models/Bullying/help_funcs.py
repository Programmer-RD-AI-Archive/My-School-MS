from Models.Bullying import *


def tokenize(sentence):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return nltk.word_tokenize(sentence.lower())


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
    data = pd.read_csv("./data/data.csv", encoding="unicode_escape")[:5000]
    X = data["Paylaþým"]
    y = data["Tip"]
    X.to_csv("./save/X.csv")
    y.to_csv("./save/y.csv")
    words = []
    data = []
    labels = {}
    idx = 0
    labels_r = {}
    for X_batch, y_batch in tqdm(zip(X, y)):
        if y_batch not in list(labels.keys()):
            idx += 1
            labels[y_batch] = idx
            labels_r[idx] = y_batch
    for X_batch, y_batch in tqdm(zip(X, y)):
        X_batch = tokenize(X_batch)
        new_X = []
        for Xb in X_batch:
            new_X.append(stem(Xb))
        words.extend(new_X)
        data.append([new_X, np.eye(labels[y_batch] + 1, len(labels))[labels[y_batch]]])
    np.random.shuffle(data)
    X = []
    y = []
    for sentence, tag in tqdm(data):
        X.append(bag_of_words(sentence, words))
        y.append(tag)
    words = sorted(set(words))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False)
    X_train = torch.from_numpy(np.array(X_train)).to(device).float()
    y_train = torch.from_numpy(np.array(y_train)).to(device).float()
    X_test = torch.from_numpy(np.array(X_test)).to(device).float()
    y_test = torch.from_numpy(np.array(y_test)).to(device).float()
    return X_train, X_test, y_train, y_test


def train(epochs, X_train, y_train, X_test, y_test, model, criterion, optimizer, batch_size):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    wandb.init(project=PROJECT_NAME, name="baseline")
    for _ in tqdm(range(epochs)):
        torch.cuda.empty_cache()
        for i in range(0, len(X_train), batch_size):
            torch.cuda.empty_cache()
            X_batch = X_train[i : i + batch_size].to(device).float()
            y_batch = y_train[i : i + batch_size].to(device).float()
            model.to(device)
            preds = model(X_batch)
            preds = preds.to(device)
            loss = criterion(preds, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            torch.cuda.empty_cache()
        torch.cuda.empty_cache()
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
    return None
