# Blog

## Planning the Project

One day I was thinking about making a project to add to my resume and randomly went on YouTube, discovering a [video](https://www.youtube.com/watch?v=TvlpIojusBE) that I enjoyed a lot, creating Christmas Tree lights that were able to be mapped in 3d space. I was astonished by the work put in as well as the final product. With Christmas coming up, I knew I wanted to do this project and add a little twist. All that I needed to do was to order the parts and then work as hard as I could to complete this project on time. Spoilers... I didn't finish it on time. This blog is the story of that project, what the final result was, and what I plan to add to it in the future.

I'm not very knowledgeable with electronics in general, so when I was going through this project, I learned various things such as soldering and wiring. When ordering the controller for the program I needed it to be small and compact, but yet powerful for it's size. I went through many different processors, but I landed on the [Seeed ESP32 C-3](https://www.seeedstudio.com/Seeed-XIAO-ESP32C3-p-5431.html). It had fitted all of my criteria, and had WiFi. It was WiFi from the board that inspired my twist on the original project in the first place. 

The "twist" I keep mentioning was to create a 3D mappable led tree BUT instead with a website that you can control the LEDs with over the internet. There were to two aspects of this project that I needed to complete within the time frame:

1. The website that hooks into a database with and api for the program to access.
2. The program to check the website, make a GET request and update the led's based on that input. 
