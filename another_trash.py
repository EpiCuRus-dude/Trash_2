import matplotlib.pyplot as plt
from IPython.display import clear_output
import time 

# Stupid function to plot loss

def plot_losses(train_losses, val_losses, epoch):
   
    """
    clear_output(wait=True)  # Clear the previous plot
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    
    # Plot training loss
    axs[0].plot(range(1, epoch+1), train_losses, label='Training Loss')
    axs[0].set_xlabel('Epochs')
    axs[0].set_ylabel('Loss')
    axs[0].set_title('Training Loss')
    axs[0].legend()

    # Plot validation loss
    axs[1].plot(range(1, epoch+1), val_losses, label='Validation Loss')
    axs[1].set_xlabel('Epochs')
    axs[1].set_ylabel('Loss')
    axs[1].set_title('Validation Loss')
    axs[1].legend()

    plt.show()


train_losses = []
val_losses = []
