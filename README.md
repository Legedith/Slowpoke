# Slowpoke

## Why
If you keep running out of data because of online lectures or because of Netflix consuming too much of your data while streaming, use slowpoke to put brakes on your data consumption. It simulates a slow internet connection so Google meet, zoom and Netflix switches from HD to SD hence reducing your data consumption (and quality). 


## Usage
> $ python3 slowpoke.py

_(300 mb/hour is a good speed limit for Google Meet and Zoom)_

## Demo
Click on the image below to see it in action

[![Demo](https://img.youtube.com/vi/xe7A2ElQ1lc/hqdefault.jpg)](https://www.youtube.com/watch?v=xe7A2ElQ1lc)

## Inspiration
Schools and colleges are re-opening "Virtually" all around the globe. This means that you only need a stable internet connection and a device to stream to attend your classes.

But for students who have limited bandwidth or for students like us in India who have only 1.5GB of internet available to us per day, this posses a problem. 

Having a high speed 4g connection means that a single 1 hour class consumes around 1.25GB of internet. This means that if we have 4 classes on a particular day, we can only take one or two classes before our internet runs out. 

This clearly shows as for most of the morning classes in our college, there are around 50-60 students present and for evening classes, only 15-20 students. 

As there is no option to manually adjust the data consumption rate for platforms such as Zoom or Google meet, we made a hack which lets you do exactly that. 

Slowpoke lets you set data consumption rate which in turn lets you control the streaming quality so you can take more classes with the same amount of data. 

## What it does
It asks you how much internet you would like to use per hour. 

Based on that, it calculates your upload and download speed.

Then using those, it executes a _trickle_ command and opens up a Firefox window with the calculated upload and download speed.

You can now use this to attend lectures on any platform that you like and the data consumption will always be less that your specified max data consumption. 

It also starts up a data monitor using _nload_ so you can see how much data has been used.

P.s. It auto-installs all the packages required when you execute the script. 

## How we built it
We used *_Trickle_* for limiting bandwidth consumption and _*nload*_ for monitoring it. 
