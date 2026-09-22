import re

source = "Welcome {name}! You have {{count}} alerts and %s pending tasks."
target = "Bienvenue {username} ! Vous avez {{count}} alertes."

def validate_placeholders(source, target):
    source_placeholders = re.findall(r"\{\{[^{}]+\}\}|\{[^{}]+\}|%s", source)
    target_placeholders = re.findall(r"\{\{[^{}]+\}\}|\{[^{}]+\}|%s", target)

    result = set(source_placeholders) - set(target_placeholders)
    result_reverse = set(target_placeholders) - set(source_placeholders)

    if result and result_reverse:
        return "Missing:", result, "Extra:", result_reverse

    elif result:
        return "Missing:", result, "Extra: none"

    elif result_reverse:
        return "Missing: none", "Extra:", result_reverse

    else:
        return "Missing: none", "Extra: none"

result = validate_placeholders(source, target)
print(result)