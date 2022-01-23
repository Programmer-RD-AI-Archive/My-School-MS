from Models.Rock_Paper_Scissors import *


def load_data():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    labels = {}
    labels_r = {}
    data = []
    idx = -1
    for folder in tqdm(os.listdir("./data/")):
        idx += 1
        labels[idx] = folder
        labels_r[folder] = idx
        for file in os.listdir(f"./data/{folder}"):
            img = f"./data/{folder}/{file}"
            img = cv2.imread(img)
            img = cv2.resize(img, (112, 112))
            data.append([img / 255.0, idx])
    np.random.shuffle(data)
    X = []
    y = []
    for d in data:
        X.append(d[0])
        y.append(d[1])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False)
    return X_train, X_test, y_train, y_test, X, y, data, idx, labels, labels_r


def train(epochs, batch_size, model, optimizer, criterion, X_train, y_train, X_test, y_test):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    wandb.init(project=PROJECT_NAME, name="baseline")
    for _ in tqdm(range(epochs)):
        for idx in range(0, len(X_train), batch_size):
            X_batch = X_train[idx : idx + batch_size].view(-1, 3, 112, 112).to(device).float()
            y_batch = y_train[idx : idx + batch_size].to(device)
            preds = model(X_batch)
            loss = criterion(preds, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        wandb.log({"Loss": get_loss(model, X_train, y_train, criterion)})
        wandb.log({"Val Loss": get_loss(model, X_test, y_test, criterion)})
        wandb.log({"Acc": get_accuracy(model, X_train, y_train)})
        wandb.log({"Val Acc": get_accuracy(model, X_test, y_test)})
        get_pred(model)
        for file in os.listdir("./preds/"):
            wandb.log({f"Img/{file}": wandb.Image(cv2.imread(f"./preds/{file}"))})
    wandb.finish()
    return None
