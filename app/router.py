from app.handlers import (
    tourist_registered,
    employee_activation,
    assignment_created,
    assignment_accepted,
    assignment_rejected,
    assignment_reminder,
    assignment_auto_accepted,
    patrol_created,
    patrol_warning,
    trip_warning,
    participant_invited,
    trip_organizer_assigned,
    trip_cancelled,
)
# 1. Import AsyncSessionLocal from your db file
from app.db import AsyncSessionLocal

EVENT_HANDLER_MAP = {
    "TouristRegistered": tourist_registered.handle,
    "EmployeeActivationTokenCreated": employee_activation.handle,
    "AssignmentCreated": assignment_created.handle,
    "AssignmentAccepted": assignment_accepted.handle,
    "AssignmentRejected": assignment_rejected.handle,
    "AssignmentReminderSent": assignment_reminder.handle,
    "AssignmentAutoAccepted": assignment_auto_accepted.handle,
    "PatrolCreated": patrol_created.handle,
    "PatrolWarningNotificationRequired": patrol_warning.handle,
    "TripWarningNotificationRequired": trip_warning.handle,
    "ParticipantInvited": participant_invited.handle,
    "TripOrganizerAssigned": trip_organizer_assigned.handle,
    "TripCancelled": trip_cancelled.handle,
}


async def route_event(event):
    handler = EVENT_HANDLER_MAP.get(event.event_type)

    if not handler:
        raise ValueError(
            f"No handler for event type: {event.event_type}"
        )

    async with AsyncSessionLocal() as db:
        try:
            await handler(event, db=db)
            await db.commit()
        except Exception:
            await db.rollback()
            raise
