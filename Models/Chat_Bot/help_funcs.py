from Models.Chat_Bot import *

stemmer = PorterStemmer()


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


def bag_of_words(tokenized_sentence, words):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag


def load_data():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    with open("./data/data.json", "r") as f:
        intents = json.load(f)
    all_words = []
    tags = []
    xy = []
    for intent in intents["intents"]:
        tag = intent["tag"]
        tags.append(tag)
        for pattern in intent["patterns"]:
            w = tokenize(pattern)
            all_words.extend(w)
            xy.append((w, tag))
    all_words = [stem(w) for w in all_words]
    all_words = sorted(set(all_words))
    tags = sorted(set(tags))
    print(len(xy), "patterns")
    print(len(tags), "tags:", tags)
    print(len(all_words), "unique stemmed words:", all_words)
    X_train = []
    y_train = []
    for (pattern_sentence, tag) in xy:
        bag = bag_of_words(pattern_sentence, all_words)
        X_train.append(bag)
        label = tags.index(tag)
        y_train.append(label)
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    return X_train, y_train, all_words, tags


class ChatDataset(Dataset):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(
        self,
    ):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        X_train, y_train, _, _ = load_data()
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.n_samples


def train(num_epochs, train_loader, model, optimizer, criterion):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    for epoch in range(num_epochs):
        for (words, labels) in train_loader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)
            outputs = model(words)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        if (epoch + 1) % 100 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")
        print(f"final loss: {loss.item():.4f}")
