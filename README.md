# Expedition-chatgpt

## Overview

My program tells you what you will need to bring on a trip using ChatGPT. It will continue to let the user ask more detailed questions until they type "no", after which the program will stop.

## How it works

There are 3 roles in the ChatGPT API, user, system, and assistant. The program uses first tells ChatGPT what it is doing using the system role. In this case, the program tells ChatGPT to give advice for an expedition.
 
It then asks the user "Tell me where you would like to go." The program then adds the user's response to the list of things to send to ChatGPT. It then does the same thing, but this time asking "Why are you going?" 

It then sends this information to ChatGPT, who responds with the types of vehicles and equipment that may be needed for the trip. It then will enter a loop where it asks the user if there is any additional information they require, and adds the last response and the question asked to the list of messages to send to ChatGPT, and each time, the questions are answered.

## What else?

You could easily modify the questions and the system role to get ChatGPT to do anything, such as make a DnD character backstory for you.
