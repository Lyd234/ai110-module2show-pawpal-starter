# PawPal+ Project Reflection

## 1. System Design
Add pet information 
set daily schedule 
ablity to add/change the schedule
**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
I chose four classes owner, pet, task and daily plan. 
The owner can set availanlitu , preferance an st a schedule.
Pet holds the pet information and care needs, and includes methods to add tasks needed for the pet
Task class sets the duration and priority needed for the task
Dailyplan collects and schedules task for a day, add and removes task

**b. Design changes**

- Did your design change during implementation?
yes
- If yes, describe at least one change and why you made it.
There was a get health summary method added by claude which i removed , because it is out of scope for this app and a pet's health can only accurartely be determined by a vet.
I also removed is valid task method from pet class. It seemed redundent as the user can remove a daily plan using the method under daily plan.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
The scheduler picks task by priority first, then uses greedy algorithm to fill the other time 
- Why is that tradeoff reasonable for this scenario?
This treade off is reasonable because it make sure the the most important task that needed to be take care of are completed first before moving to the optional ones.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

debugging, suggestions, refactoring

- What kinds of prompts or questions were most helpful?

the questions with detailed desctiption of what is needed 
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
I didn't accept some of the methods it was suggesting and sometimes it requests massive change when I request something simple, I didn't accept that
- How did you evaluate or verify what the AI suggested?
i asked is it what the task is asking? and does this code work for the app logiv?
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
Time sorting, priority sorting, next occurance, conflict detection, edge conditions
- Why were these tests important?
because they make sure the code handles edge cases,any scheduling conflict. 
**b. Confidence**

- How confident are you that your scheduler works correctly?
somewhat confident 
- What edge cases would you test next if you had more time?
I will test the time validation to see how it will act if inclomplete time string given 
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
the scheduling task

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would improve the UOI

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
how important it is to evaluate what ai suggests and making small changes at a time 