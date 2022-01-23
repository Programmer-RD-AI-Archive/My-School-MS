from Models.Sign_Language_Recognition import *


def other_loading_data_proccess(data):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    X = []
    y = []
    print("going through the data..")
    for d in data:
        X.append(d[0])
        y.append(d[1])
    print("splitting the data")
    VAL_SPLIT = 0.25
    VAL_SPLIT = len(X) * VAL_SPLIT
    VAL_SPLIT = int(VAL_SPLIT)
    X_train = X[:-VAL_SPLIT]
    y_train = y[:-VAL_SPLIT]
    X_test = X[-VAL_SPLIT:]
    y_test = y[-VAL_SPLIT:]
    print("turning data to tensors")
    X_train = torch.from_numpy(np.array(X_train))
    y_train = torch.from_numpy(np.array(y_train))
    X_test = torch.from_numpy(np.array(X_test))
    y_test = torch.from_numpy(np.array(y_test))
    return [X_train, X_test, y_train, y_test]


def load_data(img_size=112):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    data = []
    index = -1
    labels = {}
    for directory in os.listdir("./data/"):
        index += 1
        labels[f"./data/{directory}/"] = [index, -1]
    print(len(labels))
    for label in labels:
        for file in os.listdir(label):
            filepath = label + file
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (img_size, img_size))
            img = img / 255.0
            data.append([np.array(img), labels[label][0]])
            labels[label][1] += 1
    for _ in range(12):
        np.random.shuffle(data)
    print(len(data))
    np.save("./data.npy", data)
    return other_loading_data_proccess(data)


def train(X_train, y_train, X_test, y_test, model, criterion, optimizer, epochs, batch_size):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    wandb.init(project=PROJECT_NAME, name="Final")
    for _ in tqdm(range(epochs)):
        for i in tqdm(range(0, len(X_train), batch_size)):
            X_batch = X_train[i : i + batch_size].view(-1, 1, 112, 112).to(device)
            y_batch = y_train[i : i + batch_size].to(device)
            model.to(device)
            preds = model(X_batch.float())
            loss = criterion(preds, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            wandb.log(
                {
                    "loss": loss.item(),
                    "accuracy": test(model, X_train, y_train) * 100,
                    "val_accuracy": test(model, X_test, y_test) * 100,
                    "val_loss": get_loss(criterion, y_test, model, X_test),
                }
            )
    wandb.finish()
