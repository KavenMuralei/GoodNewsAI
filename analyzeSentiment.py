# from textblob import TextBlob
# from dataclasses import dataclass

# @dataclass
# class Mood:
#     sentiment: float


# def get_mood(input_text:str,*,threshold:float) -> Mood:
#     sentiment:float = TextBlob(input_text).sentiment.polarity

#     # Define mood thresholds
#     friendly_threshold: float = threshold
#     hostile_threshold: float = -threshold

#     return Mood(sentiment)

# if __name__ == '__main__':
#     while True:
#         text: str = input('Text: ')
#         mood: Mood = get_mood(text,threshold=0.3)
#         print(f'{mood.sentiment}')

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
import nltk