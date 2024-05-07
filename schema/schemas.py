def individual_serial(skill) -> dict:
    return {
        'id': str(skill['_id']),
        'name': skill['name'],
        'range': skill['range']
    }


def list_serial(skills) -> list:
    return [individual_serial(skill) for skill in skills]
