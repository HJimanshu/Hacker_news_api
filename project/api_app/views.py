from django.shortcuts import render
import requests
from django.http import JsonResponse
from datetime import datetime
import logging
# Create your views here.

logger = logging.getLogger(__name__)
def fetch_hackernews_api_data(request):
    try:
        logger.info("Fetching top stories from Hacker News API.")
        response=requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
        story_id=response.json()[:10]
        print(story_id)
        logger.info(f"Fetched top 10 story IDs: {story_id}")
        stories_data=[]
        for i in story_id:
            stories_data_get=requests.get(f'https://hacker-news.firebaseio.com/v0/item/{i}.json')
            data=stories_data_get.json()
            timestamp=data.get('time','xx:xx:xx')
            readable_time=datetime.fromtimestamp(timestamp).strftime("%B %d, %Y - %I:%M %p")
            print(data,"json data")
            story_list=    {  
                'title': data.get('title', 'No Title'),
                'author': data.get('by', 'Unknown'),
                'url': data.get('url', '#'),
                'score': data.get('score', 0),
                'time':readable_time
                }
            stories_data.append(story_list)
            logger.info(f"Fetched story: {story_list}")
        return JsonResponse({'data':stories_data},status=200)
    except requests.RequestException as e:
        logger.error(f"Error fetching top stories: {e}")
        return JsonResponse({'error':str(e)},status=500)
     