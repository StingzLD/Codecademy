from review_lib import get_next_review, submit_review

review = get_next_review()

if review is not None:
  submit_review(review)