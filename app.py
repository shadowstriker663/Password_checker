import gradio as gr

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
        feedback.append("✔ Pass the password length")
    else:
        feedback.append("❌ Password is too short (min 8 chars)")

    if any(c.isupper() for c in password):
        score += 1
        feedback.append("✔ Upper case detected")
    else:
        feedback.append("❌ Add at least one Upper Alphabet")

    if any(c.isdigit() for c in password):
        score += 1
        feedback.append("✔ Number case detected")
    else:
        feedback.append("❌ Add at least one number")

    if any(c in "':;!?*#$_%&-+()@" for c in password):
        score += 1
        feedback.append("✔ Special characters detected")
    else:
        feedback.append("❌ Add Special character")

    result_text = "Password Strong!" if score == 4 else "Choose another password"
    feedback_text = "\n".join(feedback)

    return f"Score: {score} / 4", result_text, feedback_text

interface = gr.Interface(
    fn=check_password,
    inputs=gr.Textbox(label="Enter Password", placeholder="Type here...", type="password"),
    outputs=[
        gr.Textbox(label="Score"),
        gr.Textbox(label="Result"),
        gr.Textbox(label="Detailed Feedback")
    ],
    title="Password Checker",
    description="Check your password strength directly from your phone browser."
)

if __name__ == '__main__':
    interface.launch()