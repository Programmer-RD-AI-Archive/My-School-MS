from Models.Bullying import *

X_train, X_test, y_train, y_test = load_data()
model = Model().to(device)
criterion = MSELoss()
optimizer = Adam(model.parameters(), lr=0.001)
epochs = 100
batch_size = 8
train(epochs, X_train, y_train, X_test, y_test, model, criterion, optimizer,
      batch_size)
torch.save(model, "model.pt")
torch.save(model, "model.pth")
torch.save(model.state_dict(), "model-sd.pt")
torch.save(model.state_dict(), "model-sd.pth")
