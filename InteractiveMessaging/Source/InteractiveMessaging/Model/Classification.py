"""
Text Classification of emails
"""

import torch
import pandas as pd
import matplotlib.pyplot as plt

import torch.nn as nn 
from transformers import BertTokenizerFast, BertForSequenceClassification, Trainer, TrainingArguments

import torch.optim as optim # for training 

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split

from newsgroup import NewsGroupDataset


# load the tokenizer to convert the text to tokens and switch text to all lower case
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased', do_lower_case=True)

# download the dataset
def prepare_dataset():
    dataset = fetch_20newsgroups(subset='all', shuffle=True, remove=("headers", "footers", "quotes"))
    documents = dataset.data
    labels = dataset.target
    return train_test_split(documents, labels, test_size=0.2), dataset.target_names


(train_texts, valid_texts, train_labels, valid_labels), target_names = prepare_dataset()


# encode the corpus and tokenize 
train_encode = tokenizer(train_texts, truncation=True, padding=True, max_length=512)
valid_encode = tokenizer(valid_texts, truncation=True, padding=True, max_length=512)


# convert the dataset into a torch dataset
train_dataset = NewsGroupDataset(train_encode, train_labels)
valid_dataset = NewsGroupDataset(valid_encode, valid_labels)


# load "bert-base-uncased" and the pre-trained weights
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(target_names))


# function to calculate the accuracy of the model
def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    return accuracy_score(labels, preds)


# model hyperparams
hyperparams = TrainingArguments(
    output_dir                  = './results',
    num_train_epochs            = 10, 
    per_device_train_batch_size = 16,
    per_device_eval_batch_size  = 20, 
    warmup_steps                = 600,
    weight_decay                = 0.01,
    logging_dir                 = './logs',
    load_best_model_at_end      = True,
    logging_steps               = 100, 
    evaluation_strategy         = "steps",
)


trainer = Trainer(
    model           = model,
    args            = hyperparams,
    train_dataset   = train_dataset,
    eval_dataset    = valid_dataset,
    compute_metrics = compute_metrics,
)


# train the model 
trainer.train()


# evaluate the model
trainer.evaluate()


# save the trained model
model_path = "20ng-bert-base-uncased"
model.save_pretrained(model_path)
tokenizer.save_pretrained(model_path)


# function that returns the models prediction 
def prediction(text):
    inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    outputs = model(**inputs)
    probs = outputs[0].softmax(1)
    return target_names[probs.argmax()]
