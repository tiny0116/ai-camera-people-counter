import re

class NLPEngine:
    """
    A simplistic keyword-based NLP engine
    to demonstrate capturing "鏡頭中人數", "現場人數" or synonyms.
    """

    # 可能我們要擴充更多同義詞
    KEYWORDS_COUNT_PEOPLE = ["現場人數", "鏡頭中人數", "people count"]

    def parse_intent(self, user_input):
        text = user_input.lower()

        # Keyword-based matching
        for kw in self.KEYWORDS_COUNT_PEOPLE:
            if kw.lower() in text:
                return "CountPeopleInFrame"

        return "None"
