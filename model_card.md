# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Made by Esmeralda Ruby Martinez, July 2024, .v1

## Intended Use
They are used to categorize an individual's annual income based on various factors. The model assesses whether the individual earns less than $50k annually or $50k or more.

## Training Data
Training data was provided by a third party, Udacity, in which data is split for 80% for training and the rest (20%) for testing. The data file 'census.csv.'

## Evaluation Data
Training data was provided by a third party, Udacity, in which data is split for 80% for training and the rest (20%) for testing. The data file 'census.csv.'

## Metrics
_Please include the metrics used and your model's performance on those metrics._
This is a RandomForestClassifier model with default parameters. The metrics used are Precision, Recall, and F1 (fbeta). The results on the last run were: Precision: 0.7271, Recall: 0.6109, and F1: 0.6640.

## Ethical Considerations
This model is intended for descriptive purposes only and should not be used to determine creditworthiness or similar matters based on protected features such as sex, age, race, etc.

## Caveats and Recommendations
As mentioned, the model used its default parameters. In best practice for more accurate or precise measurement and metrics, one would use hyperparameters.
