from django import template

register = template.Library()

@register.filter
def skill_level_remaining(skill):
    remaining = 4 - skill.proficiency_level
    return range(remaining)
