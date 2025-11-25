from app.core.agent import Agent

def main():
    agent = Agent(model_name="gemini-2.0-flash", temperature=0.3)
    agent.start_chat()

if __name__ == "__main__":
    main()

