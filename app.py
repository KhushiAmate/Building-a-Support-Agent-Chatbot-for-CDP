from flask import Flask, render_template, request
from models.chatbot import get_answer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cdp_name = request.form.get("cdp_name")
        question = request.form.get("question")
        
        if not cdp_name or not question:
            return render_template("index.html", answer="Please provide both the CDP name and the question.")
        
        # Get the answer from the chatbot model
        answer = get_answer(cdp_name, question)
        
        # If answer contains error or no information
        if "Error" in answer or "Sorry" in answer:
            return render_template("index.html", answer=answer, cdp_name=cdp_name, question=question)
        
        return render_template("index.html", answer=answer, cdp_name=cdp_name, question=question)

    return render_template("index.html", answer=None)

if __name__ == "__main__":
    app.run(debug=True)
