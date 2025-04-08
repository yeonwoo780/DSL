import uuid

def _get_uuid(get_str:bool = False)->None:
    """
    # get UUID

    input:
        get_str: bool = False (default)

    output:

        get_str: True
        - str(uuid)
    
        get_str: False
        - uuid
    """
    uid = uuid.uuid1()
    if get_str:
        uid = str(uid)
    return uid