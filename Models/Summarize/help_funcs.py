from Models.Summarize import *


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
    data = pd.read_csv("./data/data.csv").dropna()
    data = data[:1000]
    X = data["Text"]
    y = data["Summary"]
    X_words = []
    data = []
    y_words = []
    for X_batch, y_batch in tqdm(zip(X, y)):
        X_batch = tokenize(X_batch)
        y_batch = tokenize(y_batch)
        new_X = []
        new_y = []
        for Xb in X_batch:
            new_X.append(stem(Xb))
        for yb in y_batch:
            new_y.append(stem(yb))
        X_words.extend(new_X)
        y_words.extend(new_y)
        data.append([new_X, new_y])
    X_words = sorted(set(X_words))
    y_words = sorted(set(y_words))
    np.random.shuffle(data)
    X = []
    y = []
    for X_batch, y_batch in tqdm(data):
        X.append(bag_of_words(X_batch, X_words))
        y.append(bag_of_words(y_batch, y_words))
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.25,
                                                        shuffle=False)
    X_train = torch.from_numpy(np.array(X_train)).to(device).float()
    y_train = torch.from_numpy(np.array(y_train)).to(device).float()
    X_test = torch.from_numpy(np.array(X_test)).to(device).float()
    y_test = torch.from_numpy(np.array(y_test)).to(device).float()
    torch.save(X_train, "./save/X_train.pt")
    torch.save(X_test, "./save/X_test.pth")
    torch.save(y_train, "./save/y_train.pt")
    torch.save(y_test, "./save/y_test.pth")
    torch.save(X, "./save/X.pt")
    torch.save(X, "./save/X.pth")
    torch.save(y, "./save/y.pt")
    torch.save(y, "./save/y.pth")
    torch.save(X_words, "./save/X_words.pt")
    torch.save(X_words, "./save/X_words.pth")
    torch.save(data, "./save/data.pt")
    torch.save(data, "./save/data.pth")
    torch.save(y_words, "./save/y_words.pt")
    torch.save(y_words, "./save/y_words.pth")
    return X_train, y_train, X_test, y_test, X_words, y_words, data


def matrix_to_words(words, matrix):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    word = []
    for idx, m in enumerate(matrix):
        m = int(torch.argmax(m))
        #         print(m)
        if m == 1:
            word.append(words[idx])
    return word


def train(
    epochs,
    batch_size,
    model,
    X_train,
    y_train,
    X_test,
    y_test,
    y_words,
    criterion,
    optimizer,
):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    wandb.init(project=PROJECT_NAME, name="baseline")
    for _ in tqdm(range(epochs)):
        for i in range(0, len(X_train), batch_size):
            X_batch = X_train[i:i + batch_size].to(device)
            y_batch = y_train[i:i + batch_size].to(device)
            preds = model(X_batch)
            loss = criterion(preds, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        model.eval()
        torch.cuda.empty_cache()
        wandb.log({"Loss": get_loss(model, X_train, y_train, criterion)})
        torch.cuda.empty_cache()
        wandb.log({"Val Loss": get_loss(model, X_test, y_test, criterion)})
        torch.cuda.empty_cache()
        wandb.log({"Acc": get_accuracy(model, X_train, y_train)})
        torch.cuda.empty_cache()
        wandb.log({"Val Acc": get_accuracy(model, X_test, y_test)})
        torch.cuda.empty_cache()
        model.train()
        print(matrix_to_words(y_words, preds[0]))
    wandb.finish()
    torch.save(model, "./save/model.pt")
    torch.save(model, "./save/model.pth")
    torch.save(model.state_dict(), "./save/model-sd.pt")
    torch.save(model.state_dict(), "./save/model-sd.pth")
    return None
