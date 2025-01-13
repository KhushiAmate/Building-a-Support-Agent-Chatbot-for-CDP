import requests
from bs4 import BeautifulSoup
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import re

# Set up GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# URLs for CDP documentation
documentation_urls = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def fetch_relevant_chunk(url, question):
    """Fetch relevant section of the content based on the question."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract visible text content
        content = soup.get_text(separator="\n", strip=True)

        # Search for the most relevant content
        relevant_content = search_for_relevant_content(content, question)
        return relevant_content

    except Exception as e:
        return f"Error fetching content: {e}"

def search_for_relevant_content(content, question):
    """Search and extract the most relevant portion of content based on the question."""
    question_keywords = re.findall(r'\w+', question.lower())  # Extract keywords from the question
    content_lines = content.splitlines()

    # Look for lines that contain the question keywords
    relevant_content = []
    for line in content_lines:
        if any(keyword in line.lower() for keyword in question_keywords):
            relevant_content.append(line)

    # Combine the found lines into a chunk
    return " ".join(relevant_content[:10])  # Return the first 10 lines of relevant content

def refine_answer(content, question):
    """Refine the fetched content using GPT-2 to generate a concise answer."""
    try:
        input_text = f"Summarize the following content into a brief answer to the question: '{question}'\n\nContent:\n{content}"
        inputs = tokenizer.encode(input_text, return_tensors="pt")

        outputs = model.generate(inputs, max_new_tokens=150, no_repeat_ngram_size=2, top_p=0.9, temperature=0.7)

        refined_answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return refined_answer.strip()

    except Exception as e:
        return f"Error refining answer: {e}"

def get_answer(cdp_name, question):
    """Main function to get the refined answer based on the CDP name and question."""
    url = documentation_urls.get(cdp_name)

    if not url:
        return "Sorry, I don't have information for that CDP."

    # Fetch relevant chunk based on question
    relevant_content = fetch_relevant_chunk(url, question)
    if "Error" in relevant_content:
        return relevant_content

    # Refine the answer using GPT-2
    refined_answer = refine_answer(relevant_content, question)
    return refined_answer

# Example usage
if __name__ == "__main__":
    cdp_name = input("Enter the CDP name (Segment, mParticle, Lytics, Zeotap): ").strip()
    question = input("Enter your question: ").strip()

    answer = get_answer(cdp_name, question)
    print("\nAnswer:")
    print(answer)
