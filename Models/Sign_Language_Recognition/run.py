from Models.Sign_Language_Recognition import *

X_train, X_test, y_train, y_test = load_data(img_size=112)
model = Model().to(device)
optimzier = torch.optim.Adadelta(model.parameters())
criterion = nn.CrossEntropyLoss()
epochs = 100
batch_size = 32
train(X_train, y_train, X_test, y_test, model, criterion, optimzier, epochs, batch_size)
