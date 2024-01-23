import praw

def get_recent_and_hot_posts(subreddit_name, num_posts=10):
    # Set up your Reddit API credentials
    reddit = praw.Reddit(
        client_id='07ZNeoLjbHABVvA_oQVciA',
        client_secret='eurtdsxdC23qs9tvVagwPP_ToNCoSA',
        user_agent='Automation by Sensitive-Group-8578'
    )

    # Get the subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Get hot posts
    hot_posts = subreddit.hot(limit=50)  # Fetch more to increase the chance of overlap

    # Get recent posts
    recent_posts = subreddit.new(limit=50)  # Fetch more to increase the chance of overlap

    # Find the intersection of hot and recent posts
    hot_post_ids = {post.id for post in hot_posts}
    common_posts = [post for post in recent_posts if post.id in hot_post_ids]

    # Sort common posts by score and limit to num_posts
    common_posts_sorted = sorted(common_posts, key=lambda post: post.score, reverse=True)[:num_posts]

    # Print information about the common posts
    print(f"Most recent and trending {num_posts} posts in r/{subreddit_name}:\n")
    for post in common_posts_sorted:
        full_link = f"https://www.reddit.com{post.permalink}"
        print(f"Title: {post.title}")
        print(f"Reddit Post URL: {full_link}")
        print(f"Score: {post.score}")
        print(f"Number of comments: {post.num_comments}")
        print("\n")

if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    num_posts = int(input("Enter the number of recent and trending posts to retrieve: "))

    get_recent_and_hot_posts(subreddit_name, num_posts)
