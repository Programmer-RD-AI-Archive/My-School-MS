from Models.Rock_Paper_Scissors import *

X_train, X_test, y_train, y_test, X, y, data, idx, labels, labels_r = load_data()
X_train = torch.from_numpy(np.array(X_train)).view(-1, 3, 112, 112).to(device).float()
X_test = torch.from_numpy(np.array(X_test)).view(-1, 3, 112, 112).to(device).float()
y_train = torch.from_numpy(np.array(y_train)).to(device)
y_test = torch.from_numpy(np.array(y_test)).to(device)
model = Model().to(device)
criterion = CrossEntropyLoss()
optimizer = Adam(model.parameters(), lr=0.001)
epochs = 100
batch_size = 32
train(epochs, batch_size, model, optimizer, criterion, X_train, y_train, X_test, y_test)
