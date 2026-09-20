"""
AutoGen GroupChat Demo - Software Architecture Planning

This demonstrates REAL multi-agent collaboration using AutoGen's GroupChat,
where agents converse with each other, respond to each other's contributions,
and the GroupChatManager orchestrates speaker selection via LLM.

This contrasts with CrewAI's task-based approach — here the agents CHAT
rather than execute isolated tasks.
"""

import os
from datetime import datetime
from config import Config

# Try to import AutoGen
try:
    import autogen
except ImportError:
    print("ERROR: AutoGen is not installed!")
    print("Please run: pip install -r ../requirements.txt")
    exit(1)


class GroupChatSoftwareArchitecture:
    """Multi-agent GroupChat workflow for software architecture planning using AutoGen"""

    def __init__(self):
        """Initialize the GroupChat with specialized agents"""
        if not Config.validate_setup():
            print("ERROR: Configuration validation failed!")
            exit(1)

        self.config_list = Config.get_config_list()
        self.llm_config = {"config_list": self.config_list, "temperature": Config.AGENT_TEMPERATURE}

        # Create agents and GroupChat
        self._create_agents()
        self._setup_groupchat()

        print("All AutoGen agents created and GroupChat initialized.")

    def _create_agents(self):
        """Create UserProxyAgent and 5 specialist AssistantAgents"""

        # UserProxyAgent acts as the project lead who kicks off the discussion
        self.user_proxy = autogen.UserProxyAgent(
            name="ProjectLead",
            system_message="A technical project lead who initiates a software architecture discussion and coordinates the team through requirements, design, implementation planning, and risk assessment.",
            human_input_mode="NEVER",
            code_execution_config=False,
            max_consecutive_auto_reply=0,
            is_termination_msg=lambda x: "TERMINATE" in x.get("content", ""),
        )

        # Requirements Agent - starts the conversation with requirements analysis
        self.requirements_agent = autogen.AssistantAgent(
            name="RequirementsAgent",
            system_message="""You are a requirements engineer specializing in cloud-based software systems.
Your role in this group discussion is to START the conversation by defining the system requirements.

Your responsibilities:
- Identify 4-5 functional requirements (what the system must do)
- Identify 3 non-functional requirements covering performance, scalability, and security
- Distinguish must-have requirements from nice-to-haves
- Be specific — avoid vague statements like "the system should be fast"

After presenting your requirements, invite the DesignAgent to propose a system architecture based on your findings.
Keep your response focused and under 400 words.""",
            llm_config=self.llm_config,
            description="A requirements engineer who elicits and documents functional and non-functional system requirements.",
        )

        # Design Agent - proposes system architecture based on requirements
        self.design_agent = autogen.AssistantAgent(
            name="DesignAgent",
            system_message="""You are a software architect with expertise in cloud-native systems.
Your role in this group discussion is to BUILD ON the RequirementsAgent's findings.

Your responsibilities:
- Name the architectural pattern you recommend (e.g. microservices, event-driven, layered) and justify the choice
- Define 4-5 major system components and their responsibilities
- Describe the data flow between components
- Call out one or two key design decisions and the tradeoffs behind them

Reference specific requirements from the RequirementsAgent when justifying your decisions.
After presenting your design, invite the ImplementationAgent to create an implementation plan.
Keep your response focused and under 400 words.""",
            llm_config=self.llm_config,
            description="A software architect who designs the system structure, components, and data flows.",
        )

        # Implementation Agent - produces phased implementation plan
        self.implementation_agent = autogen.AssistantAgent(
            name="ImplementationAgent",
            system_message="""You are an engineering lead experienced in delivering cloud software projects.
Your role in this group discussion is to produce a concrete implementation plan based on the design.

Your responsibilities:
- Recommend a specific tech stack (languages, frameworks, databases, cloud provider) with brief justification
- Break the work into 3 phases: MVP, V1, and V2 — each with key milestones and a rough timeline
- Identify any dependencies or prerequisites between phases

Reference the architectural components from the DesignAgent and requirements from the RequirementsAgent.
After presenting your plan, invite the RiskAgent to assess risks.
Keep your response focused and under 400 words.""",
            llm_config=self.llm_config,
            description="An engineering lead who produces a phased implementation plan and tech stack recommendation.",
        )

        # Risk Agent - identifies and prioritizes risks
        self.risk_agent = autogen.AssistantAgent(
            name="RiskAgent",
            system_message="""You are a technical risk analyst specializing in software delivery and system design.
Your role in this group discussion is to identify and prioritize risks in the proposed architecture and plan.

Your responsibilities:
- Identify 4-5 risks spanning technical, security, scalability, and timeline dimensions
- For each risk, state: the risk description, severity (High / Med / Low), and a concrete mitigation strategy
- Flag any contradictions or weak points between the requirements, design, and implementation plan

Reference specific decisions from the DesignAgent and ImplementationAgent.
After presenting your risk assessment, invite the ArchitectReviewer to provide final recommendations.
Keep your response focused and under 400 words.""",
            llm_config=self.llm_config,
            description="A risk analyst who identifies and prioritizes technical and project risks with mitigation strategies.",
        )

        # Architect Reviewer - synthesizes and concludes with TERMINATE
        self.reviewer_agent = autogen.AssistantAgent(
            name="ArchitectReviewer",
            system_message="""You are a principal architect and technical strategist.
Your role in this group discussion is to REVIEW the full architecture plan and provide final recommendations.

Your responsibilities:
- Validate the overall feasibility of the proposed architecture and plan
- Call out any gaps or contradictions between requirements, design, implementation plan, and risk assessment
- Provide 3 top strategic recommendations for ensuring delivery success
- Be direct — if something is weak, say so and suggest how to fix it

Reference specific contributions from all previous agents.
After your review, conclude the discussion by ending your message with the word TERMINATE.""",
            llm_config=self.llm_config,
            description="A principal architect who reviews the complete plan for coherence, feasibility, and strategic alignment.",
        )

    def _setup_groupchat(self):
        """Create the GroupChat and GroupChatManager"""
        self.groupchat = autogen.GroupChat(
            agents=[
                self.user_proxy,
                self.requirements_agent,
                self.design_agent,
                self.implementation_agent,
                self.risk_agent,
                self.reviewer_agent,
            ],
            messages=[],
            max_round=10,
            speaker_selection_method="auto",
            allow_repeat_speaker=False,
            send_introductions=True,
        )

        self.manager = autogen.GroupChatManager(
            groupchat=self.groupchat,
            llm_config=self.llm_config,
            is_termination_msg=lambda x: "TERMINATE" in x.get("content", ""),
        )

    def run(self):
        """Execute the GroupChat workflow"""
        print("\n" + "=" * 80)
        print("AUTOGEN GROUPCHAT - SOFTWARE ARCHITECTURE PLANNING")
        print("=" * 80)
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Model: {Config.OPENAI_MODEL}")
        print(f"Max Rounds: {self.groupchat.max_round}")
        print(f"Speaker Selection: {self.groupchat.speaker_selection_method}")
        print("\nAgents in GroupChat:")
        for agent in self.groupchat.agents:
            print(f"  - {agent.name}")
        print("\n" + "=" * 80)
        print("MULTI-AGENT CONVERSATION BEGINS")
        print("=" * 80 + "\n")

        # Initiate the group chat conversation
        initial_message = """Team, we need to architect a cloud-based task management platform designed for remote engineering teams.

Let's work through this systematically:
1. RequirementsAgent: Define the functional and non-functional requirements
2. DesignAgent: Propose the system architecture and component design
3. ImplementationAgent: Create a phased implementation plan with tech stack
4. RiskAgent: Identify key risks and mitigation strategies
5. ArchitectReviewer: Review the full plan and provide final recommendations

RequirementsAgent, please begin with the requirements analysis."""

        chat_result = self.user_proxy.initiate_chat(
            self.manager,
            message=initial_message,
            summary_method="reflection_with_llm",
            summary_args={
                "summary_prompt": "Summarize the complete software architecture plan developed through this multi-agent discussion. Include: key requirements, proposed architecture and components, implementation phases, identified risks and mitigations, and final strategic recommendations."
            },
        )

        # Print results
        self._print_summary(chat_result)

        # Save to file
        output_file = self._save_results(chat_result)
        print(f"\nFull results saved to: {output_file}")

        print(f"\nEnd Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)

    def _print_summary(self, chat_result):
        """Print educational summary highlighting GroupChat behavior"""
        print("\n" + "=" * 80)
        print("CONVERSATION COMPLETE")
        print("=" * 80)

        print(f"\nTotal conversation rounds: {len(self.groupchat.messages)}")
        print("\nSpeaker order (as selected by GroupChatManager):")
        for i, msg in enumerate(self.groupchat.messages, 1):
            speaker = msg.get("name", "Unknown")
            content = msg.get("content", "")
            preview = content[:80].replace("\n", " ") + "..." if len(content) > 80 else content.replace("\n", " ")
            print(f"  {i}. [{speaker}]: {preview}")

        if chat_result.summary:
            print("\n" + "-" * 80)
            print("EXECUTIVE SUMMARY (LLM-generated reflection)")
            print("-" * 80)
            print(chat_result.summary)

        print("\n" + "-" * 80)
        print("EDUCATIONAL NOTE: AutoGen vs CrewAI")
        print("-" * 80)
        print("""
This workflow demonstrated AutoGen's CONVERSATIONAL approach to multi-agent systems:
- Agents were placed in a GroupChat and communicated naturally
- The GroupChatManager used LLM-based speaker selection (not hardcoded order)
- Agents referenced each other's contributions in their responses
- The conversation emerged organically through agent-to-agent interaction

Compare with CrewAI (crewai/crewai_demo.py):
- CrewAI assigns discrete Tasks to Agents with expected_output
- Each agent works independently on their assigned task
- Output is passed as context to the next task (not conversational)
- Workflow is strictly sequential with no back-and-forth
""")

    def _save_results(self, chat_result):
        """Save GroupChat conversation and summary to file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_dir = os.path.dirname(os.path.abspath(__file__))
        output_file = os.path.join(output_dir, f"groupchat_output_{timestamp}.txt")

        with open(output_file, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("AUTOGEN GROUPCHAT - SOFTWARE ARCHITECTURE PLAN\n")
            f.write("=" * 80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Model: {Config.OPENAI_MODEL}\n")
            f.write(f"Conversation Rounds: {len(self.groupchat.messages)}\n\n")

            f.write("=" * 80 + "\n")
            f.write("MULTI-AGENT CONVERSATION\n")
            f.write("=" * 80 + "\n\n")

            for i, msg in enumerate(self.groupchat.messages, 1):
                speaker = msg.get("name", "Unknown")
                content = msg.get("content", "")
                f.write(f"--- Turn {i}: {speaker} ---\n")
                f.write(content + "\n\n")

            if chat_result.summary:
                f.write("=" * 80 + "\n")
                f.write("EXECUTIVE SUMMARY\n")
                f.write("=" * 80 + "\n")
                f.write(chat_result.summary + "\n")

        return output_file


if __name__ == "__main__":
    try:
        workflow = GroupChatSoftwareArchitecture()
        workflow.run()
        print("\nGroupChat workflow completed successfully!")
    except Exception as e:
        print(f"\nError during workflow execution: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Verify API key is set in parent directory .env (../.env)")
        print("2. Check your API key has sufficient credits")
        print("3. Ensure pyautogen is installed: pip install -r ../requirements.txt")
        print("4. Verify internet connection")
        import traceback
        traceback.print_exc()
