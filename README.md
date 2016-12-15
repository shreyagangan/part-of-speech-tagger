# part-of-speech-tagger
A part-of-speech tagger for Catalan which uses Hidden Markov Model to tag tokenized untagged text (Python) 

# Overview
In this assignment you will write a Hidden Markov Model part-of-speech tagger for Catalan. The training data is provided tokenized and tagged; the test data will be provided tokenized, and your tagger will add the tags. The assignment will be graded based on the performance of your tagger, that is how well it performs on unseen test data compared to the performance of a reference tagger.

# Notes
## Slash character. 
The slash character ‘/’ is the separator between words and tags, but it also appears within words in the text, so be very careful when separating words from tags. To make life easy, all tags in the data are exactly two characters long.
## Smoothing and unseen words and transitions. 
You should implement some method to handle unknown vocabulary and unseen transitions in the test data, otherwise your programs won’t work. The unknown vocabulary problem is familiar from your naive Bayes classifier. The unseen transition problem is more subtle: you may find that the test data contains two adjacent unambiguous words (that is, words that can only have one part-of-speech tag), but the transition between these tags was never seen in the training data, so it has a probability of zero; in this case the Viterbi algorithm will have no way to proceed. The reference solution will use add-one smoothing on the transition probabilities and no smoothing on the emission probabilities; for unknown tokens in the test data it will ignore the emission probabilities and use the transition probabilities alone. You may use more sophisticated methods which you implement yourselves.

