from Models.Will_Answer_Solve_Issue import *


def tokenize(sentence):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return nltk.word_tokenize(sentence.lower())


print(tokenize("$100"))


def stem(word):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return stemmer.stem(word.lower())


print(stem("organic"))


def bag_of_words(t_words, words):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    t_words = [stem(w) for w in t_words]
    bag = np.zeros(len(words))
    for idx, w in enumerate(words):
        if w in t_words:
            bag[idx] = 1.0
    return bag


print(bag_of_words(["hi"], ["hi", "how", "hi"]))


def train(epochs, X_train, y_train, X_test, y_test, batch_size, model,
          criterion, optimizer):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    wandb.init(project=PROJECT_NAME, name="baseline")
    for _ in tqdm(range(epochs)):
        for i in range(0, len(X_train), batch_size):
            X_batch = X_train[i:i + batch_size]
            y_batch = y_train[i:i + batch_size]
            preds = model(X_batch)
            loss = criterion(preds, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        model.eval()
        torch.cuda.empty_cache()
        wandb.log({
            "Loss": (get_loss(model, X_train, y_train, criterion) +
                     get_loss(model, X_batch, y_batch, criterion) / 2)
        })
        torch.cuda.empty_cache()
        wandb.log({"Val Loss": get_loss(model, X_test, y_test, criterion)})
        torch.cuda.empty_cache()
        wandb.log({
            "Acc": (get_accuracy(model, X_train, y_train) +
                    get_accuracy(model, X_batch, y_batch)) / 2
        })
        torch.cuda.empty_cache()
        wandb.log({"Val Acc": get_accuracy(model, X_test, y_test)})
        torch.cuda.empty_cache()
        model.train()
    wandb.finish()
    return None


def save(model, X_train, X_test, y_train, y_test):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    torch.cuda.empty_cache()
    torch.save(model, "./save/model.pt")
    torch.save(model, "./save/model.pth")
    torch.save(model.state_dict(), "./save/model-sd.pt")
    torch.save(model.state_dict(), "./save/model-sd.pth")
    torch.save(X_train, "./save/X_train.pt")
    torch.save(X_train, "./save/X_train.pth")
    torch.save(X_test, "./save/X_test.pt")
    torch.save(X_test, "./save/X_test.pth")
    torch.save(y_train, "./save/y_train.pt")
    torch.save(y_test, "./save/y_test.pth")
    torch.save(y_train, "./save/y_train.pth")
    torch.save(y_test, "./save/y_test.pt")
    return None
