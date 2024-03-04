import openai
from pdfminer.high_level import extract_text

openai.api_key = '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'

def read_pdf(file_path):
    """Utility function to read and split a PDF file into chapters using pdfminer.six."""
    text = extract_text(file_path)
    chapters = text.split("Chapter")[1:]  # Assuming each chapter starts with 'Chapter'
    return chapters

def create_better_notes(chapter_text):
    """Directly generates a detailed summary from a chapter text using OpenAI's chat API."""
    prompt_text = f"""
    Based on the following text from a chapter: "{chapter_text}" Generate a detailed summary with the following structure:

    1. Analysis: A combined overview of key concepts and critical analysis related to non-linear relationships within complex systems. Discuss their significance in economics, policy-making, and daily life, including ethical considerations and the role of mathematical thinking.

    2. Illustrative Examples: Provide examples demonstrating the application of these concepts in economics, policy-making, and daily life.

    3. Insightful Quotations: Include quotes that encapsulate core lessons or insights from the chapter.

    4. Practical Applications: Suggest how the concepts can be applied in real-life scenarios, including personal decision-making and public policy.

    5. Discussion of Limitations and Pitfalls: Discuss any limitations and challenges associated with the concepts.

    Produce the summary directly without additional commentary or suggestions on the approach.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Ensure to use the correct chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text},
        ],
        temperature=0.5,
        max_tokens=1500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].message['content'].strip()  # Corrected access to response content

def main():
    # Read the contents of the PDF file
    chapters = read_pdf('book.pdf')

    for i, chapter in enumerate(chapters, start=1):
        # Generate better notes for each chapter
        better_notes = create_better_notes(chapter)
        print(f"Chapter {i} Better Notes:\n{better_notes}\n")

if __name__ == "__main__":
    main()
