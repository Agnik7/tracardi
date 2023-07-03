from typing import Optional
from .flow_graph_data import FlowGraphData
from .flow_response import FlowResponse
from .named_entity import NamedEntity


class FlowGraph(NamedEntity):
    description: Optional[str] = None
    flowGraph: Optional[FlowGraphData] = None
    response: Optional[dict] = {}

    class Config:
        arbitrary_types_allowed = True
