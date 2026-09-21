with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = """      <div class="about-text">
        <p>My journey into development hasn't been the conventional one. Getting hired by a stockbroking firm after leaving school led to a career in the financial markets as a stock and futures trader spanning about 15 years. Along the way I founded and managed a small retail business in London for 9 years before selling the company and returning to South Africa.</p>
        <p>My interest in coding started in 2019, when I enrolled in Harvard's CS50x online course. My goal wasn't to become a developer. I simply wanted to learn enough about computer science and programming to build better tools for myself as a trader. Once I finished the course, I started building small applications and tools to make parts of my daily workflow more efficient.</p>
        <p>In more recent years, I found myself spending more time building tools that solve problems. And I realised I was enjoying that more than I was enjoying trading, which led me here.</p>
        <p>I don't have a CS degree and I don't write pristine TypeScript from memory. What I do is understand business problems, figure out what needs to be built, and turn an idea into a working, deployed, secure solution in days using the tools available today. Part of that process is understanding the model's weaknesses, implementing measures to mitigate them, and still staying vigilant because they are inevitable.</p>
      </div>"""

new = '''      <div class="about-text">
        <p>I build tools that solve real business problems — whether that means an AI-powered pipeline, a purpose-built application, or knowing when an existing product already does the job.</p>
        <p>I come at this from the business side first. Fifteen years in financial markets and nine years running my own company in London taught me to think in terms of risk, cost, and return — not features. Every build starts with the same question: is the outcome worth more than what it costs to get there?</p>
        <p>I don't have a CS degree and I no longer write code from memory. My focus is on the process that determines whether a solution actually delivers: defining what the real problem is before writing a line of code, choosing architecture that holds up under actual use, and cutting the scope that sounds good but delivers nothing. I use AI where it's strong and stay critical of it where it isn't — because the gap between a demo and a production tool is almost always in the decisions, not the syntax.</p>
      </div>'''

if old in content:
    content = content.replace(old, new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("DONE - replaced about text")
else:
    print("ERROR - old text not found")
