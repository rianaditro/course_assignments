## *Problem  :
chat client from fiverr.com
https://drive.google.com/file/d/16X1KPmPwuoJiNMJIxYpb3l3DlZsZkFRL/view?usp=sharing

Salam Ahmed, Eid Mubarak 
 how are you?

I need someone to scrape data from https://www.airliners.net. Specifically, I’m looking for a dataset containing:
	•	Image URLs of aircraft photos
	•	The corresponding “Aircraft” text (aircraft type/model shown in the image).  EXAMPLE ATTACHED

The output should be in a clean, structured CSV file with two columns:
	1.	Aircraft
	2.	Image URL

I want to gather as many records as possible (targeting around 100,000), ensuring no duplicates. Please let me know if you can help


## *Solution :

Airliners.net have a good antibot feature and  I cannot scrape with beautiful soap and scrapy framework, so I try to scrap it with selenium with Proxy Support: Configure and use proxies to avoid IP bans and Anti-Detection Measures: Randomize user agents, simulate human-like interactions, and use headless browsing. 

https://github.com/rjrizani/selenium_airlanes

https://youtu.be/AB6E7p6MK_A?si=wg_k1lH3tJN7iHeq