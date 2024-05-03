# Lesson 6: Assignments | Python Strings

# 1. Product Review Analysis
# Objective:The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter
# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.
uppercase_reviews = []
keywords = ["good", "excellent", "bad", "poor", "average"]
for review in python_reviews:
    for word in keywords:
        review = review.replace(word, word.upper())
        review = review.replace(word.title(), word.upper())
    uppercase_reviews.append(review)
    print(review)

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

review_sentiments = []
for review in python_reviews:
    positive_count = 0
    negative_count = 0
    for word in review.split():
        if word.lower() in positive_words:
            positive_count += 1
        elif word.lower() in negative_words:
            negative_count += 1
    review_sentiments.append((positive_count, negative_count))
print(review_sentiments)

# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
review_summaries = []
for review in python_reviews:
    summary = review[:30]
    if len(review) > 30:
        last_space_index = summary.rfind(' ')
        if last_space_index != -1:
            summary = summary[:last_space_index]
    summary += "..."
    review_summaries.append(summary)
print(review_summaries)


# 2. User Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.
# Task 1: Input Length Validator Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.
def print_name():
    user_first_name = input("Enter your first name: ")
    user_last_name = input("Enter your last name: ")
    user_name = user_first_name + " " + user_last_name
    if len(user_first_name) < 2 or len(user_last_name) < 2:
        print("First name and last name must be at least 2 characters long.")
    else:
        print(f"Thank you {user_name}, for providing your name.")

print_name()