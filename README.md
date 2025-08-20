# 1v1.lol Elo Boosting Script

  This was a tool that automated winning competitive games. It completely broke the elo system. The highest legitimately known elo before the boosters was around ~5000, but afterwards, the highest known elo reached around ~60 million <br />
  
  I created it in early 2021 by figuring out how to send a GET request to the game's database. Doop did the same, since we were in the same clan. By mid 2021, roughly a quarter to a third of the active players had either: 
  1) Paid for a boost
  2) Gotten their ELO boosted because they knew someone with a booster
  3) Been given a booster by someone
  4) Created their own booster <br />
  
  *(sorted from the most common option to the least)* <br />
  
  Here's what the program looked like <br />*(this isn't the actual boosting process, it's just a template, since boosting is impossible nowadays, and I can't find old pictures of me using the booster because my previous Discord account got banned)*: <br />
  
![image](https://github.com/user-attachments/assets/5061add9-7d45-43ae-8e78-544e15cd47f0)

## History

  In late 2020 or early 2021, I was learning about the Python requests library, network activity, and how to manipulate it through coding. I tested these techniques on various websites, and 1v1.lol was no exception. After completing a ranked match, I discovered that a single GET request was sent to the server, so I experimented with replicating and sending that request myself... and it worked. However, I soon realized that auth tokens expire, prompting me to find a method to retrieve the refresh token from the Google account linked to 1v1.lol, which allowed access to a new auth token. At that stage, I had developed a flawless booster that could run indefinitely, all that remained was to visualize the process in the command prompt and explore other requests that could potentially be exploited

## What I Gained From This Script

  1) I achieved 25 million elo on my main account, though I eventually lost interest and was surpassed by one or two others (one confirmed, one unconfirmed) <br />
  
  (this is the highest elo I could find a screenshot of) <br />
 <img width="364" height="454" alt="Screenshot_4" src="https://github.com/user-attachments/assets/a59a732e-0682-4077-ba17-16c315b6f5d9" />

  2) I boosted a few people, earning about $200 worth of Discord Nitros in total, though I didn’t run a boosting server like Doop, since I didn’t care that much at the time <br />

## Explaining The Files
  * ```booster.py``` - The core script of the project, it sends a GET request to the game’s database using the auth token to register a win with 1 kill, then saves the server’s response to header.txt <br />
  * ```derank.py``` - The opposite of booster.py, designed to lower elo, iirc I got an account to around -500k elo, though the process was much slower since you lose elo instead of gaining it <br />
  * ```header.txt``` - Stores the server’s response from booster.py, derank.py, and skin.py. It was used to extract account details like elo and username. **I DIDNT KNOW ABOUT `json.loads` BACK THEN DONT BULLY ME (*please*)** <br />
  * ```locker.py``` - Enabled you to gain millions of positive or negative kills/deaths in the stats tab in a single script run <br />
  * ```nickname.py``` - Used to change the name of the account <br />
  * ```output.py``` -  The main hub of the project, handling refresh token updates, boosting, and displaying all necessary information <br />
  * ```refresh.py``` - Manages updating the refresh token to keep the auth token valid <br />
  * ```skin.py``` - Allows you to see what skins does the account have before starting the boost <br />
  auth-token.txt, person.txt, tokens.json - These are self-explanatory files for storing authentication <br />

## Reflections

  Looking back on this project, I find the code to be notably better than much of my earlier work, though it still appears somewhat unpolished, mainly due to my lack of familiarity with features like json.loads and other best practices at the time. Nevertheless, it fully achieved its intended purpose, and given that I worked on it at age 14 and later 15, I view it with a sense of accomplishment. Of course If I could go back in time, I’d tweak the code and how I used it. For example, output.py had a HWID login because I thought about maybe turning it into an exe to give to others (either my friends, or for profit, or both), but booster.py didn’t have one. Still, I really like this project because it showed me how powerful just three lines of code can be.
