## playwith_rnn

Hey there!

This repository describes an easy implementation and application of Recurrent Neural Network. I used `keras` as deep learning library "Using Tensorflow Backend" on CPU (yep!). 
So here's what we have: 

#### Names:
This directory mainly contains a `generator.py` file that trains on small LSTM model and simply generates new names. That simple.

* Run `generator.py`.
* It will train the model now. It will take time depending on your CPU/GPU configuration.
* When done, check the generated names in `temp_output.txt`.

#### Text:
The Text directory also contains a `generator.py` file (of course different) that takes **any** text file as an input and trains the LSTM model to generate some more "similar" text. The text to be imported for training can be essays, poems, some kind of code, or even a data-set:). But, please make sure that this file contains at least 1MB of text. Otherwise, you *might* not like the results.

* Write this on terminal: 
```
$ python generator.py your_training_file.txt your_result_file.txt
```
* Again, it will train the model now. 
* When done, check the generated text in `your_result_file.txt`.

##### Notes
* It's not necessary to train a `*.txt` file. You can also use `*.csv`, `*.tsv`etc. 
* You can modify the RNN model as well as adjust its hyperparameters to improve the results. 

Thanks.
