class Status:
    # Pipeline
    PIPELINE_NEW_LEAD = "new_lead"
    PIPELINE_ONBOARDING = "onboarding"
    PIPELINE_TRIAL_ACTIVE = "trial_active"
    PIPELINE_TRIAL_EXPIRED = "trial_expired"
    PIPELINE_SUBS_ACTIVE = "subs_active"
    PIPELINE_SUBS_EXPIRED = "subs_expired"
    PIPELINE_REGISTER_STUCK = "register_stuck"
    PIPELINE_IGNORED = "ignored"

    # Source
    ACQUISITION_ORGANIC = "organic"
    ACQUISITION_PAID_ADS = "paid_ads"
    ACQUISITION_REFERRAL = "referral"

    # Behavior
    BEHAVIOR_QUICK_ADOPTER = "quick_adopter"
    BEHAVIOR_SLOW_STARTER = "slow_starter"
    BEHAVIOR_FEATURE_SPECIFIC = "feature_specific"
    BEHAVIOR_SUPPORT_SEEKER = "support_seeker"

    # Acitivy
    ACTIVITY_HIGH = "high"
    ACTIVITY_MODERATE = "moderate"
    ACTIVITY_INACTIVE = "inactive"
    ACTIVITY_DORMANT = "dormant"

    # Milestone
    MILESTONE_REGISTERED = "registered"
    MILESTONE_TRIAL_ACTIVE = "trial_active"
    MILESTONE_TRIAL_EXPIRED = "trial_expired"
    MILESTONE_SUBS_ACTIVE = "subs_active"
    MILESTONE_SUBS_EXPIRED = "subs_expired"
    MILESTONE_NEW_BRANCH = "new_branch"
    MILESTONE_NEW_TICKET = "new_ticket"
    MILESTONE_TRX_100 = "trx_100"
    MILESTONE_TRX_1K = "trx_1k"
    MILESTONE_TRX_10K = "trx_10k"
    MILESTONE_TRX_100K = "trx_100k"
    MILESTONE_TRX_1M = "trx_1m"

    # Register Step
    REGISTER_STEP_REGISTER = "register"
    REGISTER_STEP_OTP = "otp"
    REGISTER_STEP_REGISTERED = "registered"
    REGISTER_STEP_LOGIN = "login"
    REGISTER_STEP_ACTIVE = "active"

    def __setattr__(self, name, value):
        raise TypeError("Constants can't be modified")
