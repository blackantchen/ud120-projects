#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated)

        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)

        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        # words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        stemmer = SnowballStemmer("english")

        ### do not using like this: split_words = text_string.split(" "),
        ### if two whitespace between words, it just give one whitespace
        ### using default parameter, it will give up all whitespace that between words
        split_words = text_string.split()
        # print "split_words:", split_words

        stemmed_str = []
        for w in split_words:
            stemmed_w = stemmer.stem(w)
            if(stemmed_w): ### 空格或特殊符合提取后是个空字符"",为了避免在空字符后插入空格，增加此判断
                stemmed_str.append(stemmed_w)
                stemmed_str.append(" ")

        # print "stemmed_str:", stemmed_str

        words = "".join(stemmed_str)


    return words



def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()
