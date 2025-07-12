"""
Generate shields.io badge URLs for README files.

https://shields.io/
"""

from urllib.parse import urlencode, quote


BADGES = [
    {
        "type": "pypi/v",
        "subject": "yokharianpythontemplate",
        "description": "PyPI package",
        "link": "https://pypi.org/project/yokharianpythontemplate/",
        "logo": "python",
        "logo_color": "#CCCCCC",
        "label": "PyPI",
    },
    {
        "type": "badge",
        "subject": "pdm-managed-blueviolet",
        "description": "Managed with PDM",
        "link": "https://pdm.fming.dev",
    },
    {
        "type": "badge",
        "subject": "Visual Studio Code-grey",
        "description": "Visual Studio Code",
        "link": "https://code.visualstudio.com/",
        "logo": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAADv0lEQVR4nO2ZvWsUQRjGZ97VJogfaSSFQbC5bWyUYGMRsbWwsBObgIWFMWBmLid4gtGZBNTOzn9ABEHZGMzsLRo/Ck935hRUSBELQQIKIrkLEjMyG8479T5mde8L7oEpd+f57b4z88wMQn311VfH5FBxDKhY2sZfPXMfFA+jXhIQMQbUXwfqayctNty5ona94suUVzyFshpQNwuoGAcqNoz5cosAKu21ATmQ11tRd0ljTMRstXGoDRC11Nzqsuutjh+4pwc67RyhbLAFE3GrlnmoA/CrecWV1NzqBNIad8j8vQFMhFfPPDQDqIBk2m8+vbgLiHjSyDzYA3xsr/nMoyGgvmpmHmwB5oq6febP+/vMHG9jHloCYAYMD0cQC/fGNj8ZHAQiVmzNQ+IA194MYq4C4EoDU+uYyWl0+7Zj86gzKUaB+F/jmIdEAfibYeDybWS+qhkgNJ0famieiuNARCmWeSJKkM6dTgwAuFr803ylyU8Ok0dqPjeZOwPE/xHvy4t36LzYb55PDoDJz/UBNksKmLxYnVcgLWjcksFE3EF0YUf5HYkBYC4vNwQolxSTD9GVwm5MxPWY5tdMFvqzXzexMaA1xkxdsoEAJktwYTFOySwjIkZqdesmPY0Cl2eByx/NIZSG7HMNNNe4ZKh/F40HO+v155ZiIQMWngSmvlv9jct5Demg1lf/bsZIs77cVq3EDiscBS6/WUFcDTVkHlUDfEAkOGTTj9vSKMHDEeDyixWEadnnGhP/PpqYH7Ttwm0pABEjkAm+RF/YEgKz8L5Z0TsO4KQXjgIR36KSyAQarryyhgAuPyCuOldCQMXJaBBWD8opA5G3hzCTACu0fxADyZ2tGw3Suc1Zx/pPRAvfXXQjbMc0qjGm/qXmi5KBeFGKAwFMLUcRvZUAmPrTVlmG+g/RlNiNubweD0KuAVOtixJA/c9NzK8DFRdRNlsJc6xAY0FsxvM7iOeTD3NA/cf1s7v/yaF+7Tg9o85YRY/f/8Y7NFtINk4jujAMRLz9O/76gdmkN3rUYeFx4DLeuOCyBKyQ3IYm0sT8oDFcLhkzLtAJyy3lTDgKXH2NW1Ju8uuAxmZzji7M70FxNVM4CFytdBjgPzX7eh8wudS7AEbT+SFgUvUugBEr7AKuniQC4LX7aLGsbH4Ac+n9L0DKK051BiCCCLZgrm79E4AXHa+f69zxevWBAZeztgCprrrgqJLJQsDkRgOAbr1iqgi4HIsOybjSDpe9dclXlsPkMeDq/fabS0977pq1r75Qd+gnbk39qO0MuGMAAAAASUVORK5CYII=",
        "logo_color": "#0066b8",
    },
]


def generate_shields_io_url(
    badge_type: str,
    subject: str,
    description: str | None = None,
    link: str | None = None,
    **optional_arguments: str,
) -> str:
    """
    Generate a shields.io badge URL based on the provided parameters.
    """
    base_url = "https://img.shields.io"
    encoded_subject = quote(subject, safe="")
    query_string = "?" + urlencode(optional_arguments) if optional_arguments else ""
    badge_url = f"{base_url}/{badge_type}/{encoded_subject}{query_string}"
    markdown = f"![{description}]({badge_url})" if description else f"![]({badge_url})"

    if link:
        markdown = f"[{markdown}]({link})"

    return markdown


if __name__ == "__main__":
    for badge_definition in BADGES:
        badge_markdown = generate_shields_io_url(**badge_definition)
        print(badge_markdown)
