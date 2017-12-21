# Word2Image: convert 10000 words to images

## Project steps
1. Find out 10000 most used words in some language
2. Create a basic app to display 4 pictures for any of words
3. Fill the app with default google search images as a starting step
4. Improve the word->image matching with various heuristic and empirical methods
5. Write down all the cool things we learned along the way

We will use German as target language. 10000 most frequent words will be extracted by analyzing text of german wikipedia. You can find it [here](https://dumps.wikimedia.org), or more specifically [here](https://dumps.wikimedia.org/dewiki/20170920/dewiki-20170920-pages-articles.xml.bz2)

## Collaborator setup
Please Click on the __Watch__ button to get notifications from this project
If you have any questions or problems use __Issues__

## 1.1
Download wiki bz2 file in text-analysis directory in this repo but please do NOT add it to the project, it is 6.4 Gigabytes!

## 1.2
* `cd text-analysis`
* `./xml.bz2-to-text.gz.sh dewiki-20170920-pages-articles.xml.bz2` - this will extract raw text from wikipedia with filename `dewiki-20170920-pages-articles.text.gz`
* you can view the content of this file with: `gzcat dewiki-20170920-pages-articles.text.gz | head`
* Note that above processing takes around 20m on mac book pro.
* `./text.gz-to-words.gz.sh dewiki-20170920-pages-articles.text.gz` - convert text into a stream of words, each word on a new line. Also removes some undesired words. This reduces the time for later processing scripts.

## 1.3
* ./words.gz-to-freq.tsv dewiki-20170920-pages-articles.words.gz
* this will create __dewiki-20170920-pages-articles.freq.tsv__ - a list of 10k most frequent words in german.
* Note that previous list was not correct because of wrong handling of uppercase ÄÜÖ

## 1.4
* improved word counter to preserve Title case of German nouns.
