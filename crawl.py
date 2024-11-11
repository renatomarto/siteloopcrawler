import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Website Content', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def crawl_website(base_url, num_pages):
    pdf = PDF()
    pdf.add_page()
    
    for i in range(1, num_pages + 1):
        url = f"{base_url}/{i}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string if soup.title else f'Page {i}'
        body = soup.get_text()
        
        pdf.chapter_title(title)
        pdf.chapter_body(body)
    
    pdf.output('website_content.pdf')

# Example usage
crawl_website('https://www.mysite.com', 114)
