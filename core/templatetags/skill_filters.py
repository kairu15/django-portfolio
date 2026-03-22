from django import template

register = template.Library()

@register.filter
def skill_level_remaining(skill):
    remaining = 4 - skill.proficiency_level
    return list(range(remaining))

@register.filter
def skill_level_range(skill):
    return list(range(skill.proficiency_level))
