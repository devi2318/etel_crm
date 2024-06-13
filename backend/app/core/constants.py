from enum import Enum


class TicketStatus(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"


class UserRole(str, Enum):
    SALES = "sales"
    DEVELOPER = "developer"
    SUPPORT = "support"  # support_agent
