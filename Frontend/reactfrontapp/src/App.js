
import { useState, useEffect } from "react";
import axios from "axios";
import './App.css';
function HackerNewsApp(){
const [news,setnews]=useState([]);
const [message, setMessage] = useState("");
useEffect(()=>{
async function newsApp(){
  try{
    setMessage("Data loading still in progress..")
    
    const response = await axios.get("http://127.0.0.1:8000/api/fetch_hacker_news/");
    console.log(response)
    setnews(response.data.data);
    setMessage("Data loaded successfully")
  }
  catch (err) {
    setMessage("Data Not loaded")

    console.error("Error fetching user:", err);
  }
}
newsApp();
},[])
  return (
<div className="container">

<h1 className="heading">Top 10 Hacker News Stories</h1>
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
            <br />

            <hr />
            <br />
          </div>
        ))
      ) : (
        <>
        {message && (
          <p style={{ fontSize:"20px",marginTop: "10px", color: message.includes("Error") ? "red" : "green" }}>
              {message}
          </p>
      )}
       <p> Loading Top 10 Hacker News...</p>
       </>
      )}
</div>
  );
}

export default HackerNewsApp;