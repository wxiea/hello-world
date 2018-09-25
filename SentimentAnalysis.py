import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw


reddit = praw.Reddit(client_id= 'usC8J2OisZW27g',
                     client_secret= 'YCuh26wmTLJcZsh62ZfXfj46Sh4',
                     user_agent= 'wxiea' 
                     )


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url = url)
    submission.comments.replace_more()

    return submission.comments

def process_comments(each_obj):
        for each_reply in each_obj.replies:
            print(each_reply)
            process_comments(each_reply)      

def main():
    comments = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    for i in range(1):
        for Each in comments:
            print(Each.body)
            process_comments(Each)
        
   # print(comments[0].body)
   # print(comments[0].replies[0].body)

    #neg = get_text_negative_proba(comments[0].replies[0].body)

   # print(neg)

main()
