#!/usr/bin/env python

import requests
from pandocfilters import toJSONFilter, Math, Para, Image
def latex_to_image(key, value, format, meta):
    if key == 'Math' and format == "html":
        # QuickLaTeX API endpoint
        service_url = 'https://www.quicklatex.com/latex3.f'

        # Extract LaTeX from the Pandoc JSON
        _, latex = value

        # Prepare data for POST request (adjust as per QuickLaTeX API)
        data = {
            'formula': latex,
            'fsize': '17px',
            'fcolor': '000000',
            'mode': '0',
            'out': '1',
            'errors': '1'
        }

        # Make a POST request to the conversion service
        response = requests.post(service_url, data=data)

        if response.ok:
            # QuickLaTeX response handling
            # The response includes several lines; the image URL is on the first line
            image_url = response.text.split('\n')[0]

            # Replace the Math block with an image in the Pandoc document
            alt_text = "Rendered equation"
            # Ensure the image is created as an Inline element
            return Image(['', [], []], [alt_text, alt_text], [image_url, "equation"])
    # If not a Math block or not HTML format, return the original
    return None


if __name__ == "__main__":
    toJSONFilter(latex_to_image)
