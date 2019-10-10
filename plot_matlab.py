import matplotlib.pyplot as plt
import scipy.io as sio
from datetime import datetime
from utils.utils import makedirs
import os


def plot_matlab(history, plot_png, save_mat, save_path):

    # Prepare folder to save in
    #time = datetime.now()
    #time_str = time.strftime("%Y%m%d-%H:%M")
    #cwd = os.getcwd()
    #save_path = os.path.join (cwd,  time_str)
    #print('save_path: ' + save_path)
    #makedirs(save_path)

    # Check what is all written in history
    debug = False
    if debug:
        print('########################')
        print(history.history.keys()) #'loss', 'yolo_layer_1_loss', 'yolo_layer_2_loss', 'yolo_layer_3_loss', 'lr'


    # Make numpy variables from history
    training_loss = history.history['loss'] # list with #epoch elements
    yolo_layer_1_loss = history.history['yolo_layer_1_loss']
    yolo_layer_2_loss = history.history['yolo_layer_2_loss']
    yolo_layer_3_loss = history.history['yolo_layer_3_loss']
    validation_loss = history.history['val_loss']
    val_yolo_layer_1_loss = history.history['val_yolo_layer_1_loss']
    val_yolo_layer_2_loss = history.history['val_yolo_layer_2_loss']
    val_yolo_layer_3_loss = history.history['val_yolo_layer_3_loss']


    # Save data as .mat file
    data_dict = {
    "training_loss": training_loss,
    "yolo_layer_1_loss": yolo_layer_1_loss,
    "yolo_layer_2_loss": yolo_layer_2_loss,
    "yolo_layer_3_loss": yolo_layer_3_loss,
    "validation_loss": validation_loss,
    "val_yolo_layer_1_loss": val_yolo_layer_1_loss,
    "val_yolo_layer_2_loss": val_yolo_layer_2_loss,
    "val_yolo_layer_3_loss": val_yolo_layer_3_loss,
    }
    save_mat_path = os.path.join (save_path, 'train_data.mat')
    sio.savemat(save_mat_path, data_dict)


    # Printing a figure with loss data
    fig = plt.figure()
    # training
    plt.plot(training_loss, label='train_loss')
    plt.plot(yolo_layer_1_loss, label='yolo_layer_1_loss')
    plt.plot(yolo_layer_2_loss, label='yolo_layer_2_loss')
    plt.plot(yolo_layer_3_loss, label='yolo_layer_3_loss')
    # validation
    plt.plot(validation_loss, label='val_loss')
    plt.plot(val_yolo_layer_1_loss, label='val_yolo_layer_1_loss')
    plt.plot(val_yolo_layer_2_loss, label='val_yolo_layer_2_loss')
    plt.plot(val_yolo_layer_3_loss, label='val_yolo_layer_3_loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    fig.set_size_inches((20,12), forward=False)
    save_fig_path = os.path.join (save_path, 'train_plot.png')
    fig.savefig(save_fig_path, dpi=150, transparent=True)
