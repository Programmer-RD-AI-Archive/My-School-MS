from Models.Positive_or_Negative import *

X_train, y_train, X_test, y_test, words, labels_r, labels = load_data()
model = Model().to(device)
criterion = MSELoss()
optimizer = Adam(model.parameters(), lr=0.001)
epochs = 100
batch_size = 32
train(epochs, X_train, y_train, X_test, y_test, model, optimizer, criterion, batch_size)
torch.save(model, "model.pt")
torch.save(model, "model.pth")
torch.save(model.state_dict(), "model-sd|.pt")
torch.save(model.state_dict(), "model-sd.pth")
torch.save(words, "words.pt")
torch.save(words, "words.pth")
torch.save(labels, "labels.pt")
torch.save(labels, "labels.pth")
torch.save(X_train, "X_train.pt")
torch.save(X_test, "X_test.pth")
torch.save(y_train, "y_train.pt")
torch.save(y_test, "y_test.pth")
