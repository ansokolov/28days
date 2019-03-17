# 28 DAYS: Word Learning APP

The app is based on a word learning method, originally suggested by Anton Brejestovski in this [blog post](https://brejestovski.livejournal.com/52385.html).

## "90 Seconds" Method

* When you come across a new word, you write it down in your notebook. !NB You should write a word in the context, instead of writing it as "word - translation". Meaning, that you should write the whole sentence where you have seen the word. The word should be bold or marked in colour for extra emphasis.
* During 7 days you read the sentence once or twice aloud. You are not trying to hard-code the word into your brain. You just concentrate your attention on it and understand exactly what you are saying. Reading the sentence twice will take about 10 seconds.
* In such a fashion, if you learnt 15 new sentences in a class, then during the next days you will only spend 150 seconds to repeat all the sentences.
* After 7 daily repetitions, you take a 1 week rest. After the rest you repeat the sentence 3 times, concentrating and articulating the word. About 10 seconds
* After 2 more weeks of "resting" you read the sentence three more times. About 10 seconds

That's it. 
In total, about 90 seconds (70+10+10) was spent on word learning. 
Using the method, the sentence will be "cemented" into the memory.

### Prerequisites

Python version:
```
3.6+
```
Packages:
```
os 
datetime
csv
json
```

### How to use the app

App is controlled via Console.
* Create a user from a blank account, or by importing CSV file
CSV file should have a name with which you want to create a profile and be formatted as:
```
word;sentence;translation;learnt_date;last_repeat_date;total_repetitions
```
* Add new words
* Load the app daily to check for repetitions

## Authors

* **Anton Sokolov** - *Python Implementation*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **Anton Brejestovski** - *90 Seconds Method* - [Brejestovski Language School](https://www.brejestovski.com/)
* **Arseny Klinichev** - *Encyklop* - [Youtube Channel](https://www.youtube.com/channel/UCVEmrP-NENJL8lA2HjyG7jA/featured)