# Introduction to AI
## Summary:
This project here was to build and showcase my understanding of how AI works, behaves and performs. Although I have been using free version of ChatGPT and Pro Gemini (as paid by work), this is my first deliberate attempt to dive deeper into the world of AI with a guidance from an online Udemy course. 

**Date Started**: June 13th, 2026
**IDE**: Cursor v3.6.31 (Universal)
**Database**: PostgreSQL 18.4.2
**Plan**: Free tier 
**Initial Plan Usage**: 97%
**Udemy Course**: AI For Developers With GitHub Copilot, Cursor AI & ChatGPT by Maximilian Schwarzmüller (AKA Max)
**Other AI used**: ChatGPT

## Instructions to run:



## Process
My plan for this small project is to follow along the course, step by step before I go beyond the instructions and add in some extra features, assuming that my free plan has not maxxed out by then. Once the project is completed, it will be published on Github and provide them some instructions to run the service. I may alternate between Cursor, Copilot and other AIs, whichever limit is reached before switching over. The goal is to understand the output of each AI and understand the differences of each as well as the cons & pros of them.

Max the instructor wrote out a prompt that asks ChatGPT to design out a high-level plan for building a REST API service. Once a plan was provided, it would be fed into the Cursor's agent. Initially, Max asked AI to assume the role of Node / Express developer. For the sake of my education, I'd adjusted the prompt to match my tech stack. It goes:

```
You are a professional Python / Flask developer 

Give me the structure and key building blocks for a Flask REST API that offers the following features:
- User authentication
- An authenticated user can create, edit and delete events
- An authenticated user can register for events and unregister  
- User can only edit or delete the events they created
- Events are made of a title, description, date, location and image (which is uploaded during creation)

Don’t generate any code, just give me the key building blocks and structure
```

The output was saved in PLAN.md as the AI gave it rather a lengthy, detailed plan. Already there are a few gaps in the plan, such as the lack of details on repositories and utils. We have schemas but wording not as consistent with naming convention of a file system. The upload strategy seems interesting, but it opens up to a malpractice if we let the test (or actual) images upstream without establishing restrictions in place. The same goes for config directory. In other words, ChatGPT didn't really consider the mistakes a developer could make and push them upstream. Perhaps, it's trained to be optimistic or to assume the best of us. Either that, or it didn't know nor have access to the file system we have in our system, so everything was laid out at a root level. 

Interestingly, the outputted plan was somewhat different from what was displayed on the course, particularly on the structure of a file system for a project and some suggestions. This reinforced the fact that AI was not deterministic. One other factor was that the changes have been drastic within short period of time, so the model might have been changed as well. Another factor to consider was that Max had paid for his plan, which enabled him to change the model at will. Or maybe I've chosen Python/Flask instead of NodeJS/Express. However it may be, all of these highlights the need for reviewing and ensure that all details are in correct alignment with each other before passing the plan onto an agent and kick it off from there. 

First thought was to throw in the entire plan as a single prompt to an agent. However, this violates one practice, which was to split a complex task. This implied that a sequence of tasks as a prompt can be too complex of a task itself, and if the result turned out to be entirely unsatisfactory, I'd waste a signficant chuck of a free plan. First task shall focus on user authentication and registration.

### User Authentication & Registration

