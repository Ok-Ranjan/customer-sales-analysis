import markdown as md

def covertToHTML(source, dist):
    try:
        with open(source,'r') as f:
            md_text = f.read()

        html_text = md.markdown(md_text)

        with open(dist, 'w') as f:
            f.write(html_text)
    except:
        print("Some Error")

covertToHTML('notes.md', 'md.html')