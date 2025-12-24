"""Base Agent Class for HR Agent System.

This module provides the base class for all HR agents, integrating with
Microsoft 365 Agent SDK and providing common functionality.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from datetime import datetime
import logging

from microsoft.agents import Agent, AgentContext
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from langchain.schema import HumanMessage, SystemMessage

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """Base class for all HR system agents.
    
    This class provides common functionality for agents including:
    - Microsoft 365 integration
    - LLM connectivity
    - Context management
    - Logging and monitoring
    
    Attributes:
        name (str): Agent name
        description (str): Agent description
        kernel (Kernel): Semantic Kernel instance
        context (AgentContext): Current agent context
    """
    
    def __init__(
        self,
        name: str,
        description: str,
        system_prompt: str,
        config: Optional[Dict[str, Any]] = None
    ):
        """Initialize the base agent.
        
        Args:
            name: Unique name for the agent
            description: Description of agent capabilities
            system_prompt: System prompt for LLM
            config: Additional configuration options
        """
        self.name = name
        self.description = description
        self.system_prompt = system_prompt
        self.config = config or {}
        
        # Initialize Semantic Kernel
        self.kernel = self._initialize_kernel()
        
        # Initialize context
        self.context: Optional[AgentContext] = None
        
        # Conversation history
        self.history: List[Dict[str, Any]] = []
        
        logger.info(f"Initialized {name} agent")
    
    def _initialize_kernel(self) -> Kernel:
        """Initialize Semantic Kernel with Azure OpenAI.
        
        Returns:
            Configured Semantic Kernel instance
        """
        kernel = Kernel()
        
        # Add Azure OpenAI chat completion
        kernel.add_chat_service(
            "chat",
            AzureChatCompletion(
                deployment_name=self.config.get("deployment_name", "gpt-4"),
                endpoint=self.config.get("azure_endpoint"),
                api_key=self.config.get("azure_api_key")
            )
        )
        
        return kernel
    
    async def process(self, message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Process a user message and return response.
        
        Args:
            message: User input message
            context: Additional context information
            
        Returns:
            Agent response string
        """
        try:
            logger.info(f"{self.name} processing message: {message}")
            
            # Add message to history
            self._add_to_history("user", message)
            
            # Extract intent and entities
            intent = await self._extract_intent(message)
            entities = await self._extract_entities(message)
            
            # Execute agent-specific logic
            response = await self._execute(message, intent, entities, context)
            
            # Add response to history
            self._add_to_history("assistant", response)
            
            return response
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return f"I encountered an error: {str(e)}"
    
    @abstractmethod
    async def _execute(
        self,
        message: str,
        intent: str,
        entities: Dict[str, Any],
        context: Optional[Dict[str, Any]]
    ) -> str:
        """Execute agent-specific logic.
        
        This method must be implemented by subclasses to provide
        specific agent functionality.
        
        Args:
            message: Original user message
            intent: Extracted intent
            entities: Extracted entities
            context: Additional context
            
        Returns:
            Agent response
        """
        pass
    
    async def _extract_intent(self, message: str) -> str:
        """Extract intent from user message.
        
        Args:
            message: User input
            
        Returns:
            Detected intent
        """
        # Implement intent extraction using LLM or classification model
        # This is a simplified version
        return "general_query"
    
    async def _extract_entities(self, message: str) -> Dict[str, Any]:
        """Extract entities from user message.
        
        Args:
            message: User input
            
        Returns:
            Dictionary of extracted entities
        """
        # Implement entity extraction
        return {}
    
    def _add_to_history(self, role: str, content: str):
        """Add message to conversation history.
        
        Args:
            role: Message role (user/assistant)
            content: Message content
        """
        self.history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.utcnow().isoformat()
        })
    
    def get_history(self) -> List[Dict[str, Any]]:
        """Get conversation history.
        
        Returns:
            List of conversation messages
        """
        return self.history.copy()
    
    def clear_history(self):
        """Clear conversation history."""
        self.history.clear()
        logger.info(f"{self.name} history cleared")
    
    async def invoke_tool(self, tool_name: str, parameters: Dict[str, Any]) -> Any:
        """Invoke an external tool or API.
        
        Args:
            tool_name: Name of the tool to invoke
            parameters: Tool parameters
            
        Returns:
            Tool execution result
        """
        # Implement tool invocation logic
        logger.info(f"Invoking tool: {tool_name}")
        return None
    
    def get_capabilities(self) -> List[str]:
        """Get list of agent capabilities.
        
        Returns:
            List of capability descriptions
        """
        return [
            self.description,
            "Natural language understanding",
            "Context-aware responses",
            "Multi-turn conversations"
        ]
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"
    
    def __repr__(self) -> str:
        return f"BaseAgent(name='{self.name}', description='{self.description}')"
