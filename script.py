import markdown2
import re

def convert_markdown_to_html(md_file_path):
    # Read the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Convert Markdown to HTML (keeping LaTeX as is)
    html_content = markdown2.markdown(markdown_content)

    # Add MathJax for LaTeX rendering
    mathjax_script = """
    <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
    </script>
    """
    html_content = mathjax_script + html_content

    return html_content

# Usage
html_output = convert_markdown_to_html('/Users/aadi/Code/asridharbaskari.github.io/content/Minimum cuts to divide a rectangle into squares.md')

# Save the result to an HTML file
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(html_output)
