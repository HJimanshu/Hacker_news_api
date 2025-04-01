
import { useState, useEffect } from "react";
import axios from "axios";

function HackerNewsApp(){
const [news,setnews]=useState([]);
useEffect(()=>{
async function newsApp(){
  try{
    const response = await axios.get("http://127.0.0.1:8000/");
    console.log(response)
    setnews(response.data.data);
  }
  catch (err) {
    console.error("Error fetching user:", err);
  }
}
newsApp();
},[])
  return (
<div>
<h1>Top 10 Hacker News Stories</h1>
{news.length > 0 ? (
        news.map((story, index) => (
          <div key={index}>
            <h2>
              <a href={story.url} target="_blank" rel="noopener noreferrer">
                {story.title}
              </a>
            </h2>
            <p>Author: {story.author}</p>
            <p>Score: {story.score}</p>
            <p>Published On: {story.time}</p>
            <hr />
          </div>
        ))
      ) : (
        <p>Loading Top 10 Hacker News...</p>
      )}
</div>
  );
}

export default HackerNewsApp;