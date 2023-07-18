from magik.decorators import magik_eval
from magik.evaluators import (
    contains_none,
    contains_link,
    contains_valid_link,
    not_contains_pii,
    is_positive_sentiment,
    length_less_than,
    contains,
    negate,
)


@magik_eval
def custom_function(output_to_test):
    return {
        "result": len(output_to_test) > 1000,
        "reason": f"Custom reason",
    }


# Define tests here
tests = [
    {
        "description": "output passes custom function",
        "eval": custom_function(),
        "prompt_vars": {},
        "failure_labels": ["custom_failure"],
    },
    # {
    #     "description": "output does not contain pii",
    #     "eval": not_contains_pii(),
    #     "prompt_vars": {},
    #     "failure_labels": ["sensitive_data"],
    # },
    # {
    #     "description": "output contains a link",
    #     "eval": contains_link(),
    #     "prompt_vars": {},
    #     "failure_labels": ["bad_response_format"],
    # },
    # {
    #     "description": "output contains a valid link",
    #     "eval": contains_valid_link(),
    #     "prompt_vars": {},
    #     "failure_labels": ["bad_response_format"],
    # },
    # {
    #     "description": "output sentiment is positive",
    #     "eval": is_positive_sentiment(),
    #     "prompt_vars": {},
    #     "failure_labels": ["negative_sentiment"],
    # },
    # {
    #     "description": "output length is less than 280 characters",
    #     "eval": length_less_than(280),
    #     "prompt_vars": {},
    #     "failure_labels": ["negative_sentiment", "critical"],
    # },
    # {
    #     "description": "output does not contain hashtags",
    #     "eval": contains_none(["#"]),
    #     "prompt_vars": {},
    #     "failure_labels": ["bad_response_format"],
    # },
]
