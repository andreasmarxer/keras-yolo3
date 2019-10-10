import requests


def Telegram_code_started():
    requests.get(
            'https://maker.ifttt.com/trigger/Python_Notification/with/key/bXSrizhTgJGwUIACW3-I3qcmIT5SCgmUpf1ELH3Uiex?value1=MP&value2=Code started!')


def Telegram_training_started():
    requests.get(
            'https://maker.ifttt.com/trigger/Python_Notification/with/key/bXSrizhTgJGwUIACW3-I3qcmIT5SCgmUpf1ELH3Uiex?value1=MP&value2=Training started!')


def Telegram_train_update(user, epoch, loss_prev, loss_best):
    epoch_ = str(epoch)
    loss_prev_ = str(loss_prev)
    loss_best_ = str(loss_best)

    if user == 'andreas':
        requests.get('https://maker.ifttt.com/trigger/Python_Notification/with/key/bXSrizhTgJGwUIACW3-I3qcmIT5SCgmUpf1ELH3Uiex?value1=Epoch: '
                     + epoch_+'&value2=Actual loss: '+loss_best_+'&value3=From last epoch: ' +loss_prev_)
    else:
        print ('No user defined')  # nothing to do here


def Telegram_end(time_str):
    requests.get('https://maker.ifttt.com/trigger/Python_Notification/with/key/bXSrizhTgJGwUIACW3-I3qcmIT5SCgmUpf1ELH3Uiex?value1=MP&value2=Code finished!&value3=' ++' seconds')






def Telegram_val_update(user, val_loss_, val_acc_, secs_per_batch, j):
    val_loss_ = str(val_loss_)
    val_acc_ = str(val_acc_)
    it_str = str(j)
    if user == 'andreas':
        requests.get('https://maker.ifttt.com/trigger/Python_Notification/with/key/bXSrizhTgJGwUIACW3-I3qcmIT5SCgmUpf1ELH3Uiex?value1=Val loss: '
                     + str(val_loss_)+'&value2=Val MPJPE error: ' + val_acc_+'&value3=Iteration:' +it_str +' Seconds per Batch:' + str(secs_per_batch) + 'seconds')
    elif user == 'oliver':
        requests.get('https://maker.ifttt.com/trigger/Machine_Perception/with/key/b3z-sWmM-FNCgMCjIUFsG5?value1=Val loss: '
                     + str(val_loss_)+'&value2=Val MPJPE error: ' + val_acc_+'&value3=Seconds per Batch:' + str(secs_per_batch) + 'seconds')
    else:
        print ('No user defined')  # nothing to do here



def Telegram_lr_update(user, LEARNING_RATE, j):
    learning_rate_str = str(LEARNING_RATE)
    it_str = str(j)
    if user == 'andreas':
        requests.get('https://maker.ifttt.com/trigger/Python_Notification/with/key/bXSrizhTgJGwUIACW3-I3qcmIT5SCgmUpf1ELH3Uiex?value1=MP&value2=Learning rate updated&value3=Actual lr= ' + learning_rate_str, ' Current it: ' + it_str)
    elif user == 'oliver':
        requests.get('https://maker.ifttt.com/trigger/Machine_Perception/with/key/b3z-sWmM-FNCgMCjIUFsG5?value1=MP&value2=Learning rate updated&value3=Actual lr= ' + learning_rate_str)
    else:
        print ('No user defined')  # nothing to do here
