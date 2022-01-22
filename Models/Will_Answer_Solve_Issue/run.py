from Models.Will_Answer_Solve_Issue import *

X_train, X_test, y_train, y_test = load_data()
model = Model().to(device)
criterion = MSELoss()
optimizer = Adam(model.parameters(), lr=0.001)
epochs = 100
batch_size = 32
train(epochs, X_train, y_train, X_test, y_test, batch_size, model, criterion, optimizer)
save(model, X_train, X_test, y_train, y_test)
