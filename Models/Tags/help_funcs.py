from Models.Summarize_V2 import *


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
    data = pd.read_csv("./data/data.csv")
    X = data["Affirmation"]
    y = data["Tag"]
    all_words_X = []
    all_words_y = []
    data = []
    for X_batch, y_batch in tqdm(zip(X, y)):
        X_batch = tokenize(X_batch)
        y_batch = tokenize(y_batch)
        new_X = []
        new_y = []
        for Xb in X_batch:
            new_X.append(stem(Xb))
        for yb in y_batch:
            new_y.append(stem(yb))
        all_words_X.extend(new_X)
        all_words_y.extend(new_y)
        data.append([new_X, new_y])
    X = []
    y = []
    all_words_X = sorted(set(all_words_X))
    all_words_y = sorted(set(all_words_y))
    for Xb, yb in tqdm(data):
        X.append(bag_of_words(Xb, all_words_X))
        y.append(bag_of_words(yb, all_words_y))
    all_words_X = sorted(set(all_words_X))
    all_words_y = sorted(set(all_words_y))
    X = torch.from_numpy(np.array(X)).to(device).float()
    y = torch.from_numpy(np.array(y)).to(device).float()
    torch.save(X, "./save/X.pt")
    torch.save(X, "./save/X.pth")
    torch.save(y, "./save/y.pt")
    torch.save(y, "./save/y.pth")
    torch.save(all_words_X, "./save/all_words_X.pt")
    torch.save(all_words_X, "./save/all_words_X.pth")
    torch.save(all_words_y, "./save/all_words_y.pt")
    torch.save(all_words_y, "./save/all_words_y.pth")
    return X, y


def train(epochs, X, y, model, criterion, optimizer, batch_size):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    wandb.init(project=PROJECT_NAME, name="baseline")
    for _ in tqdm(range(epochs)):
        for idx in range(0, len(X), batch_size):
            X_batch = X[idx:idx + batch_size].to(device).float()
            y_batch = y[idx:idx + batch_size].to(device).float()
            preds = model(X_batch)
            loss = criterion(preds, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        wandb.log({"Loss": loss.item()})
    #     wandb.log({'Accuracy':accuracy(model,X,y)})
    wandb.finish()
    return None
