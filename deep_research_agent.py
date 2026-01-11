"""
Deep Research Agent with Adaptive Planning and Reflection
Implementation for 'Optimizing Cross-Functional Decision Intelligence'
"""

import os
from openai import OpenAI
import pandas as pd
from typing import Dict, List, Tuple
from dotenv import load_dotenv

load_dotenv()

class DeepResearchAgent:
    """
    Deep Research Agent implementing adaptive planning with reflection mechanisms.
    
    Architecture:
    1. Planning Module: Generates structured query decomposition
    2. Execution Module: Interfaces with data sources
    3. Reflection Module: Evaluates completeness through metacognitive prompting
    """
    
    def __init__(self, model: str = "gpt-4-turbo-2024-04-09", temperature: float = 0.2):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.temperature = temperature
        self.max_iterations = 8
        self.completeness_threshold = 0.85
        
    def analyze(self, query: str, data_path: str) -> Dict:
        """
        Main analysis method implementing iterative refinement loop.
        
        Args:
            query: Business question to analyze
            data_path: Path to data file
            
        Returns:
            Dictionary containing analysis results and metadata
        """
        # Load data
        data = pd.read_csv(data_path)
        
        # Initialize
        conversation_history = []
        iteration = 0
        completeness_score = 0.0
        
        # Initial decomposition
        plan = self._generate_initial_plan(query)
        conversation_history.append({"role": "user", "content": query})
        conversation_history.append({"role": "assistant", "content": plan})
        
        # Iterative refinement loop
        while iteration < self.max_iterations and completeness_score < self.completeness_threshold:
            # Execute information gathering
            actions = self._execute_actions(plan, data)
            
            # Reflect on completeness
            reflection = self._reflect_on_completeness(query, conversation_history, actions)
            completeness_score = reflection['score']
            
            # Update conversation history
            conversation_history.append({"role": "user", "content": f"Results: {actions}"})
            conversation_history.append({"role": "assistant", "content": reflection['analysis']})
            
            # If not complete, identify gaps and update plan
            if completeness_score < self.completeness_threshold:
                gaps = self._identify_gaps(query, conversation_history)
                plan = self._update_plan(plan, gaps)
            
            iteration += 1
        
        # Generate final synthesis
        final_response = self._synthesize_response(query, conversation_history)
        
        return {
            'query': query,
            'response': final_response,
            'iterations': iteration,
            'final_completeness': completeness_score,
            'conversation_history': conversation_history
        }
    
    def _generate_initial_plan(self, query: str) -> str:
        """Generate structured query decomposition."""
        prompt = f"""Given this business question: {query}
        
        Decompose it into key analytical components:
        1. What data sources are needed?
        2. What patterns should be examined?
        3. What metrics should be calculated?
        4. What causal relationships might exist?
        
        Provide a structured plan."""
        
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content
    
    def _execute_actions(self, plan: str, data: pd.DataFrame) -> str:
        """Execute data gathering actions based on plan."""
        # In actual implementation, this would execute SQL queries, 
        # perform calculations, etc.
        # For reproducibility, researchers should implement their specific data access logic here
        
        return "Action results placeholder - implement based on your data structure"
    
    def _reflect_on_completeness(self, query: str, history: List, actions: str) -> Dict:
        """
        Evaluate information completeness using metacognitive prompting.
        
        Scores across 4 dimensions:
        1. Descriptive completeness (patterns documented)
        2. Explanatory completeness (mechanisms identified)
        3. Evidential completeness (data supports claims)
        4. Actionability (recommendations grounded)
        """
        prompt = f"""Query: {query}
        
        Current findings: {actions}
        
        Evaluate completeness on 0-1 scale across these dimensions:
        1. Descriptive: Are observed patterns fully documented?
        2. Explanatory: Are causal mechanisms identified?
        3. Evidential: Do we have supporting data for all claims?
        4. Actionability: Can we make concrete recommendations?
        
        Return scores and analysis."""
        
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Parse response and calculate average score
        # Simplified for demonstration
        score = 0.7  # In actual implementation, parse from GPT response
        
        return {
            'score': score,
            'analysis': response.choices[0].message.content
        }
    
    def _identify_gaps(self, query: str, history: List) -> str:
        """Identify knowledge gaps requiring further investigation."""
        prompt = f"""Given this query: {query}
        
        And current conversation history, what information gaps remain?
        What alternative hypotheses haven't been ruled out?
        What causal mechanisms need further investigation?"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content
    
    def _update_plan(self, current_plan: str, gaps: str) -> str:
        """Update search strategy based on discovered information gaps."""
        prompt = f"""Current plan: {current_plan}
        
        Identified gaps: {gaps}
        
        Update the analytical plan to address these gaps."""
        
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content
    
    def _synthesize_response(self, query: str, history: List) -> str:
        """Generate final integrated response with actionable recommendations."""
        prompt = f"""Query: {query}
        
        Based on this complete investigation, provide:
        1. Root cause analysis
        2. Supporting evidence
        3. Causal mechanisms
        4. Actionable recommendations
        
        Synthesize into coherent narrative."""
        
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content


# Example usage
if __name__ == "__main__":
    agent = DeepResearchAgent()
    
    query = "Why is Technology category profit declining in West region despite increasing sales?"
    
    result = agent.analyze(
        query=query,
        data_path="data/superstore.csv"
    )
    
    print(f"Iterations: {result['iterations']}")
    print(f"Completeness: {result['final_completeness']:.2f}")
    print(f"\nFinal Analysis:\n{result['response']}")
