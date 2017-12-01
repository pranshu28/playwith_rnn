## playwith_rnn

Hey there!

This repository describes an easy implementation and application of Recurrent Neural Network. I used `keras` as deep learning library "Using Tensorflow Backend" on CPU (yep!). I experimented on various types of text datasets as input to the model that then generates the probability distribution which is sampled to return the next best output for a given sequence of characters.

So here's what we have: 

#### Names:
This directory mainly contains a `generator.py` file that trains on small LSTM model and simply generates new names. That simple. To run the program:

* Run `generator.py`.
* It will train the model now. It will take time depending on your CPU/GPU configuration.
* When done, check the generated names in `temp_output.txt`.

#### Text - character and Text - word:
The Text directory contains a `main.py` file that calls:

 1. `text_io.py` file handles the input and output functions for LSTM model to generate some more "similar" text. It reads the text file, then splits the content into an character array. The text to be imported for training can be essays, poems, some kind of code, or even a data-set:). But, please make sure that this file contains at least 1MB of text. Otherwise, you *might* not like the results. I also considered word-level (check `Text-word`) training in which vocab consists of unique words in the given dataset. The rest process is similar to that in character-level training.

 2. `model.py` file defines the LSTM model and its training hyper-parameters i.e., units in a layer, dropout, training epochs, batch size etc. With each epoch, it saves the updated weights while training with the lowest error so that we can just load and generate new text without training the model again and again.

 3.  `generate.py` file assumes that the model is trained and is ready to generate new texts. This file takes input as the number of new character that is to be generated. We take a random sequence of length to feed into the model.

##### Execution: 
* Write this on terminal: 
```
$ python main.py [your_training_file]
```
* It will train the model now. 
* When done, check the generated text in `[your_result_file]-out.txt`.

#### Notes
* You can modify the RNN model as well as adjust its hyperparameters to improve the results. 
* It's not necessary to train a `*.txt` file. You can also use `*.csv` or some kind other texts. 
* You can check `wiki.txt` and train the model with it. It contains page contents concatenated into one single file. 

Thanks.