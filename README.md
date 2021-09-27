# Interactive Messaging Environment

ShellHacks 2021 Submission – Interactive Messaging Environment in Unreal Engine

![Cover Image](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/673/481/datas/original.png)

## Inspiration

In a world where digital communication drives innovation, we find ourselves dreading the idea of sending and receiving emails. A study conducted in 2017, reported that the average email user receives and sends a total of 82 emails per day. Our goal is to bring joy back to our work, by creating a humanized environment dedicated to emailing with intelligent prioritization using natural language processing.

## Overview

Interactive Messaging Environment allows communication in an email-like structure through known NPCs (mail couriers). Our natural language processing pipeline extracts important features from message content to assign an emotion rating to each message and categorizes emails into urgency levels, where each courier is responsible for an urgency rating.

The user is able to explore the world (environment) and interact with the mail couriers. The NPCs have programmed personas, which allows the user to get familiar with each courier and what sort of messages they carry. The user is also able to compose a message and/or reply in an interactive streamlined fashion, which can immensely improve productivity.

## Technologies

The application was developed as a 3D game using Unreal Engine 4 (Blueprints and C++). The natural language processing (NLP) pipeline was built using PyTorch for the neural network and Google Cloud TPU for compute resources. The program pipes were built using C (for process communication).

## Accomplishments

We fine-tuned a Bidirectional Encoder Representations from Transformers (BERT) model for a text classification task, which required use of GCP's TPU and built an interactive 3D communication system that does intelligent prioritization using NLP to personalize the experience.

## Future Work

We plan to use a text-to-speech engine to offer courier voices for reading messages which can help increase accessibility, we are exploring Replica AI for this task. We would also like to add extra NPC customizations (i.e. skins and names). Finally, we would like to integrate some components that we weren't able to integrate during the hackathon due to time limitations to make this application more usable.
