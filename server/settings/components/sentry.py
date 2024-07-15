import os

import sentry_sdk

SENTRY_DSN = os.getenv("SENTRY_DSN", default="")


sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
