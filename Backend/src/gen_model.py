def _setting_gen_model(provide):
    _setting_default = {
        "openai": "gpt-4o-2024-11-20",
        "gemini": "gemini-2.0-flash"
    }
    return _setting_default[provide]

