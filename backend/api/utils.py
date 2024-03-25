from inquiries.constants import (
    CITIZENSHIP,
    EDUCATION,
    EMPLOYMENT_METHOD,
    EMPLOYMENT_TYPE,
    RESUME_OPTIONS,
    SCHEDULE,
    PAYMENT
)


def get_education_key(value):
    for key, label in EDUCATION:
        if label == value:
            return key
    return None


def get_citizenship_key(value):
    for key, label in CITIZENSHIP:
        if label == value:
            return key
    return None


def get_workSchedule_key(value):
    for key, label in SCHEDULE:
        if label == value:
            return key
    return None


def get_workFormat_key(value):
    for key, label in EMPLOYMENT_TYPE:
        if label == value:
            return key
    return None


def get_contractType_key(value):
    for key, label in EMPLOYMENT_METHOD:
        if label == value:
            return key
    return None


def get_paymentType_key(value):
    for key, label in PAYMENT:
        if label == value:
            return key
    return None


def get_resumeFormat_key(value):
    for key, label in RESUME_OPTIONS:
        if label == value:
            return key
    return None
