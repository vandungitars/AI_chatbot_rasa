# Imports
#-----------
# rasa core
import rasa_core
from rasa_core.agent import Agent
from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core import run
from rasa_core.training import interactive

def run_dialogue(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
    rasa_core.run.serve_application(agent, channel='cmdline')
    return agent

def run_online_dialogue(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
    interactive.run_interactive_learning(agent)
    return agent

run_dialogue()