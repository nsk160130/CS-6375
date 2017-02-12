This file contains the implementation of ID3 algorithm.


To simplify things, you can assume that the data used to test your implementation will contain only Boolean (0 or 1) attributes and Boolean (0 or 1) class values.
You can assume that there will be no missing data or attributes
You can also assume that the first row of the dataset will contain column names and each non-blank line after that will contain a new data instance.
Within these constraints, your program should be able to read and process any dataset containing any number of attributes.
You can assume that the last column would contain the class labels.

A couple of datasets are provided. You have to build your model using the training dataset,
check the model and prune it with the validation dataset, and test it using the testing dataset.

Below is a summary of the requirements:

• Build a binary decision tree classifier using the ID3 algorithm.<br>
• Your program should read three arguments from the command line – complete path of the training dataset, complete path of the test dataset, and the pruning factor (explained later).<br>
• The datasets can contain any number of Boolean attributes and one Boolean class label. The class label will always be the last column.<br>
• The first row will define column names and every subsequent non-blank line will contain a data instance. If there is a blank line, your program should skip it.
