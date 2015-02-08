import praw

user_agent = ("/u/dyingtosaythis's second reddit thing")
r = praw.Reddit(user_agent=user_agent)
r.login()

my_subs = r.get_my_subreddits(limit=None)
subreddits = []
for sub in my_subs:
    sub = str(sub.display_name)
    subreddits.append(sub.lower())

f = open('subreddits.txt','w')
for item in sorted(subreddits):
    f.write("%s\n" % item)
f.close()


