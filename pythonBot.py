from instapy import InstaPy

session = InstaPy(username="<your_username>", password="<your_password>")
session.login()
#enter tags you'd want to like
session.like_by_tags(["", ""], amount=5)
#enter tags you dont want to like
session.set_dont_like(["", ""])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
#enter comments you'd use
session.set_comments(["", "", ""])
session.end()
