# Interactive Messaging Environment

ShellHacks 2021 Submission – Interactive Messaging Environment in Unreal Engine

![Cover Image](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/673/481/datas/original.png)

## Inspiration

In a world where digital communication drives innovation, we find ourselves dreading the idea of sending and receiving emails. A study conducted in 2017, reported that the average email user receives and sends a total of 82 emails per day. Our goal is to bring joy back to our work, by creating a humanized environment dedicated to emailing with intelligent prioritization using natural language processing.

## What it does

Interactive ME is a messaging environment that allows communication in an email-like structure through known NPCs (mail couriers). Our natural language processing pipeline extracts important features from message content to assign an emotion rating to each message and categorizes emails into urgency levels, where each courier (NPC) is responsible for an urgency rating.

The user is able to explore the world (environment) and interact with the mail couriers. The NPCs have programmed personas, which allows the user to get familiar with each courier and what sort of messages they carry. The user is also able to compose a message and/or reply in a streamlined fashion. This can immensely improve productivity.

## How we built it

The application was developed as a 3D game using Unreal Engine 4 (Blueprints and C++). The natural language processing (NLP) pipeline was built using PyTorch for the neural network and Google Cloud TPU for compute resources. The program pipes were built using C (for process communication).
Challenges we ran into

Our goal was to build an experience that can be as human as possible. We approached the creation of player (the user) and NPCs using MetaHuman Creator, we encountered many issues in terms of building the project due to the high hardware utilization requirements. We resolved this problem by finding an alternative editor after extensive research. Also, none of the team members had used Unreal Engine before.

## Accomplishments that we're proud of

We fine-tuned a Bidirectional Encoder Representations from Transformers (BERT) model for a text classification task, which required use of GCP's TPU. We built an interactive 3D communication system that does intelligent prioritization using NLP with a humanized and personalized experience.
What we learned

We learned how to use PyTorch for fine-tuning a model, which is something none of us have previously done. We also learned how Blueprints and C++ can be used for developing games and how multiple languages can be integrated to build an optimal experience. Finally, we learned how to use Unreal Engine-specific features, which is very useful knowledge for developing games or simulations in the future.

## What's next for Interactive Messaging Environment

We plan to use a text-to-speech engine to offer a courier voice for reading messages which can help increase accessibility, we are exploring Replica.AI for this task. We would also like to add extra NPC and user character customizations (i.e. skins and names).
