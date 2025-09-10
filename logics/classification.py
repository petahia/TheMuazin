from decoding import *


class ContentClassification:
    def __init__(self,content: str):
        self.content = str(content)
        self.hostile_list = touple_lists_decoded[0]
        self.non_hostile_list = touple_lists_decoded[1]


    def calculate_danger_percentage(self):
        appearances_hostile = 0
        appearances_non_hostile = 0
        words_of_text = self.content.lower().split(" ")
        amount_of_words = len(words_of_text)

        for word in words_of_text:
            if word in self.hostile_list:
                appearances_hostile += 1
            if word in self.non_hostile_list:
                appearances_non_hostile += 1
        percentage = ( ((appearances_hostile * 2) + (appearances_non_hostile)) /
                       (amount_of_words + appearances_hostile)) * 100
        rounded_percentage = round(percentage, 2)
        return rounded_percentage


    def set_criminal_event(self,percentage):
        threshold = 15
        if percentage >= threshold:
            return True
        else:
            return False

    def segment_danger_levels(self,percentage):
        if percentage < 5:
            return 'none'
        elif 5 < percentage < 10:
            return 'medium'
        else:
            return 'high'






