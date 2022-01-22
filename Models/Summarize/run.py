from Models.Summarize import *

X_train, y_train, X_test, y_test, X_words, y_words, data = load_data()
model = Model().to(device)
criterion = MSELoss()
optimizer = Adam(model.parameters(), lr=0.001)
batch_size = 32
epochs = 100
train(epochs, batch_size, model, X_train, y_train, X_test, y_test, y_words, criterion, optimizer)
