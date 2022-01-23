from Models.Summarize_V2 import *

X, y = load_data()
model = Model().to(device)
criterion = MSELoss()
optimizer = Adam(model.parameters(), lr=0.001)
epochs = 1000
batch_size = 32
train(epochs, X, y, model, criterion, optimizer, batch_size)
