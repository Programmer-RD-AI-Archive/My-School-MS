from Models.Chat_Bot import *
from Models.Chat_Bot.help_funcs import *

batch_size = 8
X_train, y_train, all_words, tags = load_data()
dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

num_epochs = 1000
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)
model = NeuralNet(input_size, hidden_size, output_size).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
train(num_epochs, train_loader, model, optimizer, criterion)
data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "hidden_size": hidden_size,
    "output_size": output_size,
    "all_words": all_words,
    "tags": tags,
}
FILE = "data.pth"
torch.save(data, FILE)
