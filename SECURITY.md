# Security Policy

## Describing a vulnerability 

### Step 1: What is the severity of the vulnerability?
Is the vulnerability `Low`, `Medium`, `High` or `Severe` in severity.
Here's a quick brief on each level:
- **Low** - Not an immediate threat and doesn't expose access to any internal processes or the database
- **Medium** - If exploited, could lead to access to restricted things
- **High** - Can be discovered on code inspection and could lead to loss of data and access to the bot and/or database 
- **Severity** - Requires almost no skill to exploit and could cause serious damage

### Step 2: How easily can someone discover this issue?
Different people have different levels of knowledge on things like: `discord.py` and `MongoDB`.
This means an apparent security vulnerability to one may be hard to capture for someone else.
Try and estimate what level of expertise someone will need to have in order to exploit the vulnerability.
This means including:
1. Which technology the person should have an understanding of.
2. How well they should be able to use it on a scale of 1-10 or using words such as:
    - Beginner
    - Intermediate
    - Expert

### Step 3: What does this vulnerability allow an exploiter to do?
There are two main things that a vulnerability could let anybody misusing their technological skills do:
1. Control the whole bot or even a part of the bot
2. Gain access to the MongoDB database
Make sure you know the extent of control a certain vulnerability gives to anybody exploiting it.

### Step 4: How can the vulnerability be reproduced?
If possible, please provide **non-breaking** ways in which we could investigate further into the vulnerability.
This could take the form of a simple step-by-step guide.

## Reporting a vulnerability
Here's a simple step by step guide on what to do once you find a vulnerability:
1. Make sure the vulnerability is, indeed a vulnerability, and not a bug
2. If you have discovered a bug, open an issue on the [repository issue tracker](https://github.com/smetch-discord/smetch-bot/issues)
3. Take appropriate action depending on the severity:
    - `Low`: Open an issue on the [issue tracker](https://github.com/smetch-discord/smetch-bot/issues)
    - `Medium`: Contact a member of the Staff or Developer team on the [Discord server](https://discord.gg/5AqVhkWXyQ)
    - `High`: Contact a member of the Admin team on the [Discord server](https://discord.gg/5AqVhkWXyQ)
    - `Severe`: Contact `RickRollingLife#5301` by DMing them
4. When reporting this issue to the correct place, please make sure to list all the things mentioned above in the **Describing a vulnerability** section
5. We will respond and take action as soon as we can.

## What now?
Here is a list of things you can do after reporting a vulnerability 
- Just relax! We'll take care of it.
- Code! Can you help in fixing this vulnerability? Check out our [Contributing guidelines]() for more info.
- Join us! Are you a part of the SMETCH Discord? If not, [join now](https://discord.gg/5AqVhkWXyQ)

**Thank you for taking the time to help SMETCH become safer for everyone!**
