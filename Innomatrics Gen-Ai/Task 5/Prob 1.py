# 1) Social Media  Post Engagement Analyzer 
def analyze_post_engagement(likes_list):
    total_likes = 0

    for like in likes_list:
        total_likes += like

    if total_likes >= 1000:
        status = "Viral Post"
    else:
        status = "Normal Engagement"

    print("Total Likes:", total_likes)
    print("Post Status:", status)


likes = [200, 300, 150, 400]
analyze_post_engagement(likes)