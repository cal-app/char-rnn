# char-rnn

A fun project to generate text, character by character, after training the model on a corpus. 

## What does it do?

The model is trained on a corpus of text which is split into "sentences" of _N_ characters (including spaces and punctuation). Each sentence corresponds to a training example. The label associated to each training example is the single character that immediately follows the sentence.

As a simple example, consider the following corpus:

_"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."_

Say we set _N = 8_. The first "sentence" in the corpus is then _Lorem ip_ and its label is _s_, since that is the character that comes directly after. Note that sentences can overlap depending on our choice of stride _s_. For instance, with _s = 2_ the next sentence is _rem ipsu_

The set of all sentences and labels constitutes the training data, and the model's goal is to learn which character is likely to follow a given string of _N_ characters.

Once the model has been trained, it can generate text letter by letter based on a small amount of starting text. The nature of the text it generates will, of course, depend on what you trained it on.


## Architecture

RNN with 2 LSTM layers with dropout. Output words are sampled from a softmax distribution.

