import os
os.chdir(os.path.join(os.environ['HOME'], 'mnt', 'bk-portfolio'))

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = """        <p>I build tools that solve real business problems — whether that means an AI-powered pipeline, a purpose-built application, or knowing when an existing product already does the job.</p>
        <p>I come at this from the business side first."""

new = """        <p>I build tools that solve real business problems — whether that means an AI-powered pipeline, a purpose-built application, or knowing when an existing product already does the job.</p>
        <p>A well-designed product solves a real problem without adding new layers of friction. I believe the best tools feel invisible because they match the way people already think and work. Great design is not about decoration or trends. It is about understanding what someone needs to accomplish and removing every obstacle between them and that goal.</p>
        <p>I come at this from the business side first."""

if old in content:
    content = content.replace(old, new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("DONE")
else:
    print("ERROR - old text not found")
