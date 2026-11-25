const container = document.getElementById("story-container");
const moreBtn = document.getElementById("more-btn");
const submitLink = document.querySelector(".submit");
const loginLink = document.querySelector(".login-btn");

let currentPage = 1;

async function getStory(page){
    const response = await fetch(
        `http://localhost:8000/v1/?page=${page}`
    );
    if(!response.ok){
        throw new Error(`HTTP error: ${response.status}`);
    }
    const data = await response.json();
    data.posts.forEach(story => {
        const article = `
        <article class="story">
            <div class="fix-components">
                <span class="rank">${story.rank}</span>
                <span class="upvote"></span>
            </div>
            <div class="main-components">
                <div class="top">
                    <div class="title">
                        <a href=${story.link} target="_blank" rel="noopener noreferrer">${story.title}</a>
                    </div>
                    <div class="domain">
                        <a href=${story.domain_link} target="_blank" rel="noopener noreferrer">(${story.domain})</a>
                    </div>
                </div>
                <div class="bottom">
                    <span class="score">${story.score} points</span> by
                    <div class="username">
                        <a href=${story.author_info_link} target="_blank" rel="noopener noreferrer">${story.author}</a>
                    </div>
                    <div class="time_ago">
                        ${story.time_ago}
                    </div>
                    |<div class="hide">
                        <a href=#>hide</a>
                    </div>
                    | <div class="comments">
                        <a href=${story.comments_link} target="_blank" rel="noopener noreferrer">${story.comments} comments</a>
                    </div>
                </div>
            </div>
        </article>
                     `;
        container.innerHTML += article
        });
                
    }
                    
moreBtn.addEventListener("click",()=>
    {
        currentPage++;
        container.innerHTML=""
        getStory(currentPage);
    })

submitLink.addEventListener("click",()=>
    {
        // alert("Submissions aren't supported here (this is just a clone!)\nGo to https://news.ycombinator.com/ to submit a post\nThough you have to be logged in first ");
        const userConfirmed = confirm("Submissions aren't supported here (this is just a clone!)\n\nWould you like to go to the official Hacker News?");
        if(userConfirmed){
            window.open("https://news.ycombinator.com/","_blank");
        }
    })
loginLink.addEventListener("click",()=>
    {
        // alert("Submissions aren't supported here (this is just a clone!)\nGo to https://news.ycombinator.com/ to submit a post\nThough you have to be logged in first ");
        const userConfirmed = confirm("Login isn't supported here (this is just a clone!)\n\nWould you like to go to the official Hacker News?");
        if(userConfirmed){
            window.open("https://news.ycombinator.com/","_blank");
        }
    })

container.addEventListener("click",(e)=>
    {
        const hideLink =e.target.closest(".hide");
        if(hideLink){
            const storyCard = hideLink.closest(".story");
            if (storyCard){
                storyCard.remove();
            }

        }
    })

    
getStory(currentPage);